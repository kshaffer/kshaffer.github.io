---
layout: post
title: "A journey through API programming ― Part 4: Posting to Medium"
modified: 2016-09-27 14:41:00 -0400
image:
  feature: apiHeader4.jpg
  teaser: apiHeader4-teaser.jpg
  credit: paul bica
  creditlink: https://www.flickr.com/photos/dexxus/5791228117/
share: true
categories: [coding]
---

<p><i>This is part of a series of posts in which I blog through my process of learning API programming in general and <a href="https://medium.com/blog/the-medium-api-is-now-open-to-everyone-3f4642e5c850#.8ehvndx6y">the Medium API</a> in particular. For the beginning of this series, see <a href="http://kris.shaffermusic.com/2016/08/journey-through-api-programming-1/">Part 1</a>, <a href="http://kris.shaffermusic.com/2016/08/journey-through-api-programming-2/">Part 2</a>, and <a href="http://kris.shaffermusic.com/2016/08/journey-through-api-programming-3/">Part 3</a>, as well as my post "<a href="http://kris.shaffermusic.com/2016/09/getting-data-out-of-medium/">Getting data out of Medium</a>".</i>
</p>

<p>In my last couple of posts, I walked through the process of retrieving data from Medium. Medium severely limits the data that is available via the API, and as my "Getting data out of Medium" post discusses, the process of exporting your posts from Medium and importing them into another platform is not as simple as I would like. Nevermind exporting other users' posts, or all the posts of a particular publication.&nbsp;</p>

<p>However, getting data <i>into</i>&nbsp;Medium is very easy. Not only do they have a beautiful, easy-to-use editor for writing posts, but the Medium API makes it very simple to create new posts and drafts on their platform. In this post, I'll walk through that process.</p>


<h2>Authenticating</h2>

<p>We'll start by authenticating, using the Python SDK that Medium provides (and which I describe in <a href="http://kris.shaffermusic.com/2016/08/journey-through-api-programming-3/">Part 3</a>). If you are already authenticated ― from the activities of Part 3, for example ― you can skip this part.&nbsp;</p>

<p>Open a Python terminal, and enter the following (substituting your data for the X's ― see Part 3 if you don't know what those details are):</p>

~~~ python
from medium import Client
import requests
client = Client(application_id="xxxxxxxxxxx", application_secret="xxxxxxxxxxxxxxxxxxxxxxxxx")
auth_url = client.get_authorization_url(“secretstate”, “https://pushpullfork.com/callback", [“basicProfile”, “publishPost”])
print(auth_url)
~~~

<p>This will return a long URL. Copy that URL, paste it into your browser window, and hit enter/return.&nbsp;The URL will change from what you entered in, and it will end with ‘code=XXXXXXXX’, where the X’s represent your secret code. Copy that code and go back to your Python window. (Again, I don't know of a way to automate this part of the process. If you do, please let me know!)</p>

<p>In your Python terminal, enter the following (replacing the X's with the code you just copied):</p>

~~~ python
auth = client.exchange_authorization_code(“XXXXXXXX”, “https://pushpullfork.com/callback")
client.access_token = auth[“access_token”]
user = client.get_current_user()
~~~

<p>Now you're authenticated!</p>


<h2>Posting to Medium</h2>

<p>Authenticating is the hard part, as I'm finding is often the case with APIs. Posting is a piece of cake by comparison. In fact, with the Python SDK, it's only a single line of code.</p>

~~~ python
post = client.create_post(user_id=user["id"], title="Title", content="<h2>Test title</h2><p>Trying to post with the Medium API.</p>", content_format="html", publish_status="draft")
~~~

<p>This line of code will create a draft post that looks a bit like the following:</p>

<blockquote><h2>Test title</h2>Trying to post with the Medium API.</blockquote>

<p>I recommend using publish_status="draft" so that you can look things over on Medium before publishing, especially if you are embedding media. However, if you are confident in your content and formatting, you can change to publish_status="public".</p>

<p>It's easy to add media. Simply include the proper HTML tags. Medium will automatically embed videos, but retrieve images from the linked source and serve them up from their own content delivery network. That means you can import images without worrying about them being deleted from the source. Medium will always have them. But you're at the mercy of whoever is hosting any videos you embed.</p>

<p>You can also add tags in the API call. Here's a bit more substantive call that includes an image (from one of my blog posts) and sample tags:</p>

~~~ python
post = client.create_post(user_id=user["id"], title="Title", content="<h2>Test title</h2><p>Trying to post with the Medium API.</p><p>And testing out an image...<br/><img src=\"http://kris.shaffermusic.com/assets/images/scaffold.jpg\" />", tags=['tag1', 'tag2'], content_format="html", publish_status="draft")
~~~

<p>If you sent this call while authenticated to your own account, you'd see the post in your list of drafts. And if you opened the draft, you could inspect the photo element to see that it indeed has been retrieved from my server and is being served up by Medium's CDN. Click on "Publish" to see (and edit) the list of tags. tag1 and tag2 should already be in the list.
</p>

<p>Pretty simple! Once you're authenticated, the only hard part is coming up with the content for the post!</p>

<h2>API vs. "Import Story"</h2>

<p>Why use the API to post to Medium when you can just go to Medium and import the story? After all, all you need to do is paste in the URL of the original, and Medium does the rest. And in both cases, you'll probably need to do a little fine-tuning.</p>

<p>I see the API's value here in a cross-posting scenario. Suppose you follow the POSSE (Publish on your Own Site, Syndicate Elsewhere) model. You like to create content on your own domain (WordPress, Jekyll, Known, Ghost...), but you want to syndicate to places like Medium and link to your social media accounts in order to boost readership. Medium's API makes it easy to automatically cross-post. Medium already has <a href="https://github.com/Medium/medium-wordpress-plugin">an official WordPress plugin</a>&nbsp;to do just that. But the API can support development of plugins and tools for other platforms. I'll probably add cross-posting capabilities to <a href="https://peasy.pushpullfork.com">Peasy</a>, for example. And I'm working on something that would make it easier to write in one place for both <a href="http://jekyllrb.com/">Jekyll</a> (i.e., <a href="https://pages.github.com/">GitHub Pages</a>) and Medium.</p>

<p>I also imagine that the API would make it easy, or at least possible, to import a large batch of posts from another platform into Medium. Medium already supports <a href="https://help.medium.com/hc/en-us/articles/218572107-How-to-move-to-Medium">importing from a WordPress export file</a>, but I haven't come across tools for other platforms. If you want to move more than a handful of posts from Tumblr or Jekyll to Medium, writing a script around the API is probably the way to go. (And don't forget to share that code so others can use it!)</p>

<p>Of course, as I wrote yesterday, <a href="http://kris.shaffermusic.com/2016/09/getting-data-out-of-medium/">getting your data out of Medium and into another platform is kind of a pain</a>. So personally, I see the value primarily in terms of cross-posting, or moving old posts into Medium so I can sync up a Medium publication with my own site, and then cross-post future additions.</p>

<p>Whatever you want to do with the Medium API, it's really easy to get content into Medium. After authenticating, it's just one line of code!</p>

<p>If you're using the Medium API, especially in conjunction with a Domain of One's Own, please get in touch. I'd love to hear about what you're doing!</p>

*Featured image by [paul bica](https://www.flickr.com/photos/dexxus/5791228117/).*
