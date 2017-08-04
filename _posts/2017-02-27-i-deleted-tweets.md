---
layout: post
title: "I deleted 40,000 tweets last week. Here's why (and how)."
modified: 2016-12-30 20:12:00 -0500
image:
  feature: bird.jpg
  teaser: bird-teaser.jpg
  credit: Mathias Appel
  creditlink: https://www.flickr.com/photos/mathiasappel/16255827151/
share: true
categories: [digital minimalism, coding]
short_description: "Use Python and the Twitter API do curate your public digital identity."
---

<i>This post is Part 2 in my series on digital minimalism. Check out my first post in this series, <a href="/2016/12/digital-minimalism-being-deliberate-about-digital-identity/">Digital minimalism ― being deliberate about digital identity</a>.</i>

I tweet a lot. Since joining six years ago, I've posted approximately 50,000 tweets, retweets, and replies. Some of it is good stuff. I've used Twitter to share my thoughts-in-progress about a variety of things ― teaching, music, coding, data ― as well as to connect with friends, students, and other scholars, particularly those from fields other than my own. I joke that my blog got me my job in Colorado and Twitter got me my job at UMW, but those statements aren't far from the truth. My work as a public scholar online has been instrumental in gaining me a lot of opportunities to work, write, speak, meet collaborators, and even make friends.

But as I think about curating my public materials, <a href="/2016/12/digital-minimalism-being-deliberate-about-digital-identity/">being deliberate about my digital identity</a>, and keeping myself safe from would-be trolls and harassers, Twitter stands out as a big problem. It's a very useful tool, but it's really easy to get lost in the weeds of old posts, retweets, replies, making it hard to find the good stuff. In fact, most people I know have resigned themselves to the idea that Twitter is ephemeral. The good content is going to quickly flow downstream. While it may be retweeted and brought back into view again, eventually it will go away, and our attention will move on to what's next.

Except it doesn't go away.

In 2013, Twitter introduced a major change to its service, allowing users to search for tweets from the entirety of Twitter's history. Those of us using the service at the time had grown accustomed to tweets disappearing from search results after five days, becoming inaccessible to all but the most tenacious of scrollers and swipers. But when Twitter made their entire history searchable, all of those old tweets we thought had dissipated into the ether were now instantly findable.

I'm not particularly worried about overly embarrassing tweets resurfacing. However, I have changed a lot as a person since I started tweeting. As I remarked to a friend while discussing my purging of Twitter content,

> My professional, spiritual, and political identities (and contexts) have all changed a lot since I started tweeting.

There are a lot of implications in that tweet, but it really boils down to the idea that I'm both the same person and a different person from the Kris who joined Twitter in 2010. If Twitter is truly *social* media, then I want it to be media that helps people get to know me *now*, not me in 2010.

My use of Twitter has also changed. Some of that stems from my own personal changes, but also from ways in which the Twitter service has changed, and from the ways that others use it. Because of the rise of online abuse and harassment, I post less personal and family information on Twitter than I used to. And partly because of the potential for online abuse, or at least <a href="https://en.wikipedia.org/wiki/Parasocial_interaction">parasocial behavior</a>, and partly because of the change in search capabilities, the kinds of conversations I had openly on Twitter in 2011 or 2012 are often the kinds of conversations that I would have on Slack or in private messages in 2016 and 2017.

Ultimately, though, as I think about being deliberate about public digital identity, and as I teach that to my digital studies students, I realize the need to pull some weeds, so to speak. Yes, I want to be more deliberate about what I post, don't post, keep, delete, retweet, etc. But I also want to make it so if someone searched for something from me, they'd be more likely to find my good stuff. I don't want people to get bogged down in old retweets, conversations with friends, and comments about teaching classes I don't teach anymore, or political positions I don't (fully) embrace anymore. And as I increase in visibility and follower count, I don't want to bring potentially unwanted attention to others, particularly former students with whom I conversed back under the old search rules.

So I decided a couple weeks ago to embark on a big tweet-delete campaign. Specifically, I decided to delete the following:

<ul>
<li>All retweets of other users' posts (about 17k tweets)</li>
<li>All replies more than six months old (about 18k tweets)</li>
<li>Most old Twitter chats (#profchat, #flipclass, etc.)</li>
<li>Tweets containing old conference hashtags</li>
<li>Tweets containing old course hashtags</li>
</ul>

I still have about 10,000 tweets left! And I probably want to go back and cull more. But by deleting these five categories of things, I was able to pull back a lot. And it wasn't that difficult! So if you're thinking about purging some of your old Twitter content, keep reading for a walk-through of how I did it.

<em><strong>Update:</strong> Since writing this post, I have gone and deleted almost all of my tweets. After taking some time off of Twitter completely, I realized that personally, I'm done with Twitter as a service and as a company. However, I also realized, especially at the end of Digital Pedagogy Lab Vancouver, that Twitter is the easiest way to find people I want to connect with in my field(s), and Twitter is what most people (at DPL and the like, anyway) are still using as their primary way of connecting and communicating. So I'm staying on Twitter, posting occasional links to things I write and create (so those who use social media to find those kinds of things can access my work), and connecting with people on the platform (primarily via DM). But I'm not tweeting anymore. And as I connect with people on Twitter, I'm going to bookmark their website/blog, and do my best to build channels of communication and collaboration that extend beyond the bounds of this problematic and proprietary platform ― while also still respecting their preferences, of course. And that's the tough thing to balance. We all have different preferences, and while I can make some decisions for myself, network decisions need to be made by the network.</em>

## Delete some tweets

Because I'm a nerd, and because I don't want to give full control over my Twitter account to a service I don't know or trust, I wrote code in Python using the Twitter API to do the work. Even if you're not much of a coder, if you have *some* experience writing code, I think you should be able to follow the code and make the tweaks that you need. So let's get started!

<b>The first thing to do is <a href="https://support.twitter.com/articles/20170160?lang=en#" style="font-weight: bold;">download your Twitter archive</a></b> and extract the zip file. This not only gives you a copy of all your old tweets ― for posterity sake, and which you can even post on your own independent domain if you want to! ― but we'll use the archive in the deletion process.

Next, <b>create a new app on <a href="https://apps.twitter.com/">apps.twitter.com</a>.</b> Just click "Create New App"; then provide a name for your app ("tweet deleter" is fine), description (same), and website (your website, or even the URL for your Twitter account).

Once you've created your account, you need to get a few **authorization codes** to link your Python script with your Twitter app. Open the "Keys and Access Tokens" tab, where you'll find a *Consumer Key (API Key)* and a *Consumer Secret (API Secret)*. You'll also probably need to click on "Generate My Access Token and Token Secret" to generate the *Access Token* and *Access Secret*. Keep this tab open in your browser so you can copy these codes into your Python script, and be sure not to share these codes with others, or they'll be able to access your account.

Now it's time to start that Python script. I use Python 3, and to interact simply with the Twitter API, I use the <a href="http://tweepy.readthedocs.io/en/v3.5.0/">Tweepy</a> framework, which you can install via

```pip install tweepy```

(If you're new to Python, pip, and tweepy, check out the <a href="https://www.continuum.io/downloads">Anaconda bundle</a> for scientific computing.)

Let's start scripting! First import ```tweepy``` and ```csv```, and declare those API keys (I left mine out).

~~~python
import tweepy
import csv

consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''
~~~

Then create a couple functions. This function will read in the ```tweets.csv``` file from your Twitter archive without a header row into a list of lists.

~~~python
def read_csv(file):
    """
    reads a CSV file into a list of lists
    """
    with open(file, encoding = 'utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        rows = []
        for line in reader:
            row_data = []
            for element in line:
                row_data.append(element)
            if row_data != []:
                rows.append(row_data)
    rows.pop(0)
    return(rows)
~~~

And this function provides what you need for authenticating with Twitter.

~~~python
def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    verify_code = raw_input("Authenticate at %s and then enter you verification code here > " % auth_url)
    auth.get_access_token(verify_code)
    return tweepy.API(auth)
~~~

After creating these functions, perform the authentication.

~~~python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
print("Authenticated as: %s" % api.me().screen_name)
~~~

And read in the downloaded Twitter archive.

~~~python
tweets = read_csv('/path/to/file/tweets.csv')
~~~

Now it's time to decide which tweets to delete and collect them. I've set my script up so that Python will search the downloaded archive to assemble this list, which is much faster than using the API. It also doesn't have any limits on how many tweets you can query at once. And both of these things mean you can do more double-checking before actually deleting anything!

Here's how to build a list of tweets to delete (called ```tweets_marked```) by searching your archive for a specific hashtag.

~~~python
hashtag = '#profchat'
tweets_marked = []
for tweet in tweets:
    if hashtag in tweet[5]:
        tweets_marked.append(tweet)
~~~

This will make a list of all tweets (represented by a list of values) whose ```text``` field in the Twitter archive contain the ```#profchat``` hashtag. It doesn't delete anything just yet, but it does allow you to explore those tweets and make sure you do indeed want to delete them.

To find out how many tweets were found by that search, use

~~~python
print(len(tweets_marked), 'tweets marked for deletion.')
~~~

To print all of the text of those tweets and make sure they're the right ones, use

~~~python
for tweet in tweets_marked:
    print(tweet[5])
~~~

Alternatively, to collect a list of all retweets, use

~~~python
tweets_marked = []
for tweet in tweets:
    if tweet[5][0:3] == 'RT ':
        tweets_marked.append(tweet)
~~~

Or a list of all direct replies:

~~~python
tweets_marked = []
for tweet in tweets:
    if tweet[5][0] == '@':
        tweets_marked.append(tweet)
~~~

Or all direct replies from a specified list of months:

~~~python
tweets_marked = []
month_list = ['2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08']
for tweet in tweets:
    if tweet[5][0] == '@':
        if tweet[3][0:7] in month_list:
        tweets_marked.append(tweet)
~~~

Combine these methods as appropriate (search, date ranges, etc.) for what you want to delete. I found it helpful to do one round of deletion at a time ― e.g., #profchat then #flipclass then retweets all as separate processes ― rather than try to assemble a single master list of every tweet to delete. This makes the deletion process into multiple small steps, rather than one arduous one. It also makes it easier to double-check what you're doing piece-by-piece, leading to quite a bit less stress throughout the process.

Once you've assembled your list of tweets to delete, it's time to delete!

~~~python
# build list of marked status IDs
to_delete_ids = []
delete_count = 0
for tweet in tweets_marked:
    to_delete_ids.append(tweet[0])

# delete marked tweets by status ID
for status_id in to_delete_ids:
    try:
        api.destroy_status(status_id)
        print(status_id, 'deleted!')
        delete_count += 1
    except:
        print(status_id, 'could not be deleted.')
print(delete_count, 'tweets deleted.')
~~~

This code will send an API call to Twitter for each of the tweets in ```tweets_marked```, instructing Twitter to delete the tweet. **THIS IS PERMANENT, SO BE SURE YOU REALLY WANT TO DO THIS!** It will print the ID number of the tweet and whether or not it was able to delete the tweet. Note that if you have tweets in your archive that come up in multiple searches, they will come up in your archive search each time, but will only actually be deleted the first time. The later searches will get more 'could not be deleted' messages as a result, but that will not cause any other problems.

Twitter's API will not allow this process to go particularly fast if run in a single-threaded environment (as this code uses). I've seen a solution for multi-threading, but it didn't work on my setup (it was written for Python 2). It's not super-slow, but it won't be instantaneous. I didn't time it, but you can definitely delete a few thousand tweets in less than an hour.

That's it!

Like I said above, I probably want to go back and delete more content, but this process got me through several very large categories of tweets and deleted 80% of my tweets in just a few hours. You could also use it to "go nuclear" and delete all your tweets ever. Or all your tweets before/after a certain date and time. You can also use Tweepy to delete favorites, private messages, mass block and unblock, and edit your list of whom you follow (with very sensitively named methods like ```destroy_friendship()```). See the <a href="http://tweepy.readthedocs.io/en/v3.5.0/api.html" target="blank_">Tweepy documentation</a> for a complete list of functions and methods.

I still tweet a lot, and retweet a lot, and converse a lot online, but having a tool like this means that I can regularly go through and purge some of those things that were good at the time, but not worth hanging onto in perpetuity. And it means that searches on my profile are at least a little more likely to return things worth finding.

As I tell my students, when you write, *deleting words is just as much progress as writing words*. Maybe more. The same goes for what we write on the web. Curation can be hard work, but it means that what remains is more valuable, easier to find, and has room to grow. Time will tell if that's true for Twitter, too.

<i>This post is Part 2 in my series on digital minimalism. Check out my first post in this series, <a href="/2016/12/digital-minimalism-being-deliberate-about-digital-identity/">Digital minimalism ― being deliberate about digital identity</a>.</i>

<i>Some of the code in this post was based on a Gist in GitHub by <a href="https://gist.github.com/davej/113241">Dave Jeffrey</a>. Header image by <a href="https://www.flickr.com/photos/mathiasappel/16255827151/" target="blank_">Mathias Appel</a> (CC0).</i>
