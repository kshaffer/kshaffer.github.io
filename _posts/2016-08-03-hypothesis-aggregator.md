---
layout: post
title: "Hypothes.is Aggregator ― A WordPress Plugin"
modified: 2016-08-03 08:40:00 -0400
image:
  feature: oldtype.jpg
  teaser: oldtype-teaser.jpg
  credit: darkday
  creditlink: https://www.flickr.com/photos/drainrat/16786733075/
share: true
categories: blog
---

*This is a cross-post from the [UMW Division of Teaching and Learning Technologies blog](http://umwdtlt.com/hypothesis-aggregator-wordpress-plugin/).*

I’ve been working and writing a lot lately about using the web annotation tool <a href="https://hypothes.is/">hypothes.is</a> for public scholarship. It has a lot of cool uses ― not only the collaborative annotation of individual web pages, but also the creation of a <a href="http://kris.shaffermusic.com/2016/04/hypothesis-public-research-notebook/">public research notebook</a>, and the possibility of linking hypothes.is with other apps <a href="http://kris.shaffermusic.com/2016/05/getting-started-with-the-hypothesis-api/">through the use of their open API</a>.

Based on that work, I’ve created a few tools to help people make fuller use of hypothes.is in their work as public scholars. The first is <a href="http://kris.shaffermusic.com/2016/06/introducing-pypothesis-1/">a Python script</a> that collects annotations (by user, by tag, or both) and converts them to clean MarkDown text, for use in a blog. The second is <a href="http://kris.shaffermusic.com/2016/06/introducing-pypothesis-2/">Pypothesis</a>, a Python module for writing programs that interact with the hypothes.is API.

More recently, I've created a WordPress plugin called <a href="https://github.com/kshaffer/hypothesis_aggregator">Hypothes.is Aggregator</a>, which will allow WordPress users ― bloggers, teachers, and students alike ― to collect their own annotations, annotations on a topic of interest, or annotations from/about a class, and present them in a page or post on the WordPress platform. It's easy to install, easy to use, and (I hope) will be of value to students, scholars, teachers, and writers.
<h2>How it works</h2>
Hypothes.is aggregator is super-simple. Create a new page or post in WordPress, and as you write, include the following "shortcode":

~~~
[hypothesis]
~~~

Now, that alone won't do anything. You need to feed it some search terms, like one of the following:

~~~
[hypothesis user = 'kris.shaffer']
~~~

~~~
[hypothesis tags = 'IndieWeb']
~~~

~~~
[hypothesis text = "Domain of One's Own"]
~~~

~~~
[hypothesis user = 'kris.shaffer' tags = 'IndieEdTech']
~~~

Hypothes.is Aggregator accepts <em>user</em>, <em>tags</em>, and <em>text</em> search parameters, on their own or in combination with each other. (Currently it does not support lists of users or tags, but that is in the works for a future version.)

After adding one line of this "shortcode," publish the post, and you should see on that page a list of annotations, <a href="http://pushpullfork.com/uncategorized/testing-the-skeleton-of-a-hypothesis-aggregator-plugin-for-wordpress/">like on this sample page</a>. That's it!

(If it doesn't work, please let me know, and I'll do my best to figure it out and release a fix.)

<h2>What it's for</h2>

I envision a number of possible uses for Hypothes.is Aggregator. As I write in my post on hypothes.is as a public research notebook, you can use this plugin to make a public research notebook on your WordPress site. Read something interesting, annotate it, and aggregate those annotations ― perhaps organized by topic ― on your domain. They will automatically update. Just set it and leave it alone.

I also see this as a tool for a class. Many instructors already use hypothes.is by assigning a reading that students will annotate together. Hyopthes.is Aggregator makes it easy to assign a <em>topic</em>, rather than a reading, and ask students to find their own readings on the web, annotate them, and tag them with the course tag. Then Hypothes.is Aggregator can collect all the annotations with the class tag in one place, so students and instructors can see and follow-up on each other's annotations. Similar activities can be done by a collaborative research group or in an unconference session.

<h2>Help me kick the tires</h2>

I've done a lot of small tests, but I could use some help. So if you're interested, please try it out and let me know how it goes. I'll do my best to help you out and/or add fixes and features to future versions.

It's really easy to install and get going. First, go to <a href="https://github.com/kshaffer/hypothesis_aggregator">the project page on GitHub</a>, click "Clone or Download" (the green button on the right), and then "Download to ZIP." Then go to Plugins &gt;&gt; Add New in your WordPress dashboard. Click "Upload Plugin." Then upload the ZIP file you just downloaded. Once it's uploaded and installed, click "Activate," and you're ready to go!

Then try it out, and let me know how it goes.

<h2>Plans for the future</h2>

It can do a lot of things as-is. But I want to add more. Here's my current list (feel free to suggest more):
<ul>
 	<li>Search for all posts from a <em>list</em> of users (for more fool-proof class aggregation).</li>
 	<li>Support multiple tags ― in both AND and OR configurations.</li>
 	<li>Add "class" attributes to the HTML objects, for more flexible visual presentation.</li>
 	<li>The ability to embed a single annotation into a blog post (like you can with a tweet).</li>
</ul>
What else should this plugin do?

<em>Photo by <a href="https://www.flickr.com/photos/drainrat/16786733075/">darkday</a></em> (CC BY 2.0).
