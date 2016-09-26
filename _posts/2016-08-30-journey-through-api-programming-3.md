---
layout: post
title: "A journey through API programming ― Part 3: Retrieving data?"
modified: 2016-08-30 15:01:00 -0400
image:
  feature: apiHeader3.jpg
  teaser: apiHeader3-teaser.jpg
  credit: Kjetil Korslien
  creditlink: https://www.flickr.com/photos/kjetikor/8484119632/
share: true
categories: [coding]
---

*This is part of a series of posts in which I blog through my process of learning API programming in general and* [*the Medium API*](https://medium.com/blog/the-medium-api-is-now-open-to-everyone-3f4642e5c850#.8ehvndx6y) *in particular. For the beginning of this series, see* [*Part 1*](http://kris.shaffermusic.com/2016/08/journey-through-api-programming-1/) *and* [*Part 2*](http://kris.shaffermusic.com/2016/08/journey-through-api-programming-2/)*.*

The basic element of programming with APIs is the API call, a single command in one application that contacts another application with a request to send, receive, edit, or delete data to/from that other application. API calls are particularly powerful when the “data” to send is actually a set of instructions for the app to execute, with instructions for what to do with the results. But we’ll start on the simple end with a simple “GET” request ― an API call that asks the other application to send some data back to the application making the call.

When I first started exploring API programming, I ran into a lot of documentation sites that contained something like this as a “sample request” with no instructions for how to issue such a request within a specific programming language:

~~~
GET /v1/me HTTP/1.1
Host: api.medium.com
Authorization: Bearer 181d415f34379af07b2c11d144dfbe35d
Content-Type: application/json
Accept: application/json
Accept-Charset: utf-8
~~~

Of course, it’s not the job of those writing API documentation to teach users how to make API calls. *But* just about everything I read, including API how-tos, assumed some level of knowledge that I didn’t have, making it very difficult to learn how to make a “simple” API call.

I’m going to try and break it down.

Let’s start with a really simple example. The [hypothes.is API](https://h.readthedocs.io/en/latest/api/) does not require authentication for GET requests, as long as you are okay with the API returning only public data (no private annotations are included in the data it sends back), so that makes it more straightforward than, say, the Medium API.

The hypothes.is API documentation provides the following description of what such a GET request would look like. This API call returns all the annotations by the user gluejar.

~~~
GET /api/search?limit=1000&user=gluejar@hypothes.is
Host: hypothes.is
Accept: application/json
~~~

But this isn’t what we type into our code. We can stitch it together though. Start with the host ― hypothes.is ― then add the GET url ― /api/search?limit=1000&user=gluejar@hypothes.is ― to the end of it, and finally stick https:// in front of it:

~~~
https://hypothes.is/api/search?limit=1000&user=gluejar@hypothes.is
~~~

This is the unauthenticated API call! Notice we’re going to the hypothes.is server, telling it we’re making an API request (notice the /api/, though not all servers do it this way), and then pass an instruction to search for annotations from the user gluejar@hypothes.is and limit the results to 1000 annotations or less.

To try this API call, just put that URL into the address bar of your browser and see what you get. This is a JSON object (JavaScript Object Notation, though it is not limited to JavaScript; many languages use and parse JSON data). If you’ve worked with JSON data before, you likely recognize the format. If not, it may look like nonsense. (Though if you cut and paste it into a [JSON prettifier](https://jsonformatter.curiousconcept.com/), the structure will start to become more apparent.)

For simple GET requests to APIs that don’t require authentication, it’s that easy.

To incorporate such a request into your code, you need a function that will make the request without a browser, and store the results into a data structure.

Here’s the code that will do that in Python (assuming you have installed the requests and json modules):

~~~python
import requests
import json
raw_data = requests.get('https://hypothes.is/api/search?limit=1000&user=gluejar@hypothes.is')
parsed_data = json.loads(raw_data.text)
~~~

Now you have a JSON object called ‘parsed\_data’ containing the same data returned in our browser request above, ready for analysis and manipulation.

## Helper modules

Constructing the exact URL for a request can be tricky, though. It’s easy to see that the above search looks for 1000 or less annotations from gluejar@hypothes.is, but how would we construct a GET request for the five most recent annotations with the tag ‘JavaScript’ from the user kris.shaffer@hypothes.is? Poring over the API docs (when they’re well written) can make that clear. However, they aren’t always as complete or pedagogically sound as we might like. Or the docs may be in good shape, but the API is so robust that the construction of the request will be highly complex by necessity. The same goes for the data we get back ― even with clear documentation, the data structure may be complex, deeply hierarchical, and unituitively structured from the perspective of an end user.

For these reasons, many developers of popular APIs create software development kits (SDKs) or helper modules for common programming languages, to make the construction of requests and the processing of data less burdensome. For example, I created [Pypothesis](https://github.com/kshaffer/pypothesis), a Python module for making and parsing unathenticated GET requests for the hypothes.is API. The Spotify API has [Spotipy](https://spotipy.readthedocs.io/en/latest/) (also, predictably, for Python).

Here’s example code for Pypothesis (assuming the module has been installed, or pasted into the Python script above what follows):

~~~python
s = searchurl(user = 'kris.shaffer@hypothes.is', tag = 'JavaScript')
l = retrievelist(s)
for entry in l:
    e = Annotation(entry)
    print(e.title, e.uri)
~~~

This is all you need to find every annotation by me about JavaScript, and then print to screen the title and URI of each article annotated. (Dig into the code for [Hypothes.is Aggregator](https://github.com/kshaffer/hypothesis_aggregator) to see how to do similar things in PHP.)

## Using the Medium API SDK

But I said this blog series would be about by journey with the Medium API! I went through hypothes.is first, because you can send a GET request *without* authenticating. Not so with Medium. **Every Medium API call requires authentication.** And that adds significant complication. So let’s dig in, using the Medium API’s Python SDK.

First, we need to download and install Medium’s SDK for API calls in Python. You can find it (and SDKs for several other languages) [here](https://github.com/Medium/medium-api-docs/blob/master/SDK.md). Also, I’ll be mostly following Ben Werdmuller’s tutorial for the Medium API ([available here](https://github.com/Medium/medium-api-docs)), but adding more detailed instructions for the less-than-fully-initiated (like I was/am). :)

The first step is to [register a new Medium application](https://medium.com/me/applications) so you can make authenticated calls. It’s fine to name it something like ‘testing’. It will ask you for a callback URL. It doesn’t actually matter what this is. In fact, it doesn’t even need to exist! I recommend putting your website followed by ‘/callback’. When you register successfully, it will provide you with a client ID and a client secret. Treat the client secret like a password and do *not* share it with others.

Then you can run the following code in Python (replacing the X’s with your client ID and client secret, and replacing ‘https://pushpullfork.com/callback’ with the callback URL you provided when you made the app). Because we’re doing this in two parts, I recommend calling Python from the command line or using iPython, which will keep the session open, rather than running code from within a text editor.

~~~python
from medium import Client
import requests
~~~

~~~python
client = Client(application_id="xxxxxxxxxxx", application_secret="xxxxxxxxxxxxxxxxxxxxxxxxx")
auth_url = client.get_authorization_url(“secretstate”, “https://pushpullfork.com/callback", [“basicProfile”, “publishPost”])
print(auth_url)
~~~

If it works, it should print to screen a really long URL.

Visit that URL in your browser. (As far as I can find, there’s no way to spoof the server into thinking that your Python script is a real person and doing this part automatically. If you know how, please leave a comment, and I’ll update the tutorial!)

If, like me, you used a fake URL for your callback, you’ll get a 404 Page Not Found response. *BUT* take a look at the address bar. The URL has changed from what you entered in, and it will end with ‘code=XXXXXXXX’, where the X’s represent your secret code. Copy that code and go back to your Python window.

Now run the following Python code (replacing the X’s with the code you just received, and replacing my callback URL with yours):

~~~python
auth = client.exchange_authorization_code(“XXXXXXXX”, “https://pushpullfork.com/callback")
client.access_token = auth[“access_token”]
user = client.get_current_user()
print(user)
~~~

If it works, you’ll see a small Python dictionary that contains basic data for your Medium user. You can access its internal elements like usual. To get the username, simply enter:

~~~python
user['username']
~~~

Let’s try one more request. Let’s get all the publications that I (or you) have published in on Medium.

Oh, wait! [That’s supported by the Medium API](https://github.com/Medium/medium-api-docs). But [it doesn’t look like it’s supported by the Python SDK](https://github.com/Medium/medium-sdk-python/blob/master/medium/__init__.py)! What to do?

Well, we’ll have to take a step back and hard-code the request ourselves. (And maybe contribute the code to the SDK!)

So in the coming post(s), I’ll dig into making authenticated requests in Python that aren’t supported by the SDK, and/or using JavaScript to make those requests. I haven’t done either before! (Though I’ve done the latter with other APIs.) So I’ll be blogging as I learn. :)

*Header image by* [*Kjetil Korslien*](https://www.flickr.com/photos/kjetikor/8484119632/) *(CC BY-NC).*
