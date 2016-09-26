---
layout: post
title: "Getting data out of Medium"
modified: 2016-09-26 10:45:00 -0400
image:
  feature: wishbone.jpg
  teaser: wishbone-teaser.jpg
  credit: paul bica
  creditlink: https://www.flickr.com/photos/dexxus/5794905716/
share: true
categories: [coding, public scholarship]
---

Controlling my data is important to me. It’s also important that my students (and the faculty that I support) have the ability to control their own data, as well. That doesn’t mean that *everything* needs to live on a Domain of One’s Own. But it does mean that I want my data to be as flexible as possible, and as easy to move around as possible.

It’s really easy to [download an archive](https://help.medium.com/hc/en-us/articles/214043918-Export-content-from-Medium) of your Medium posts. Like your Twitter archive, you can just unzip the archive and upload it to your domain, and you’ve got it up and running. 

However, if you want to incorporate those posts into a different platform — like WordPress, Jekyll, Known, etc. — it is more of a challenge.

I wrote my posts on the Medium API directly in Medium. Partly as an experiment, and partly because I love the Medium post editor. (It’s why I incorporated a [Medium editor clone](https://yabwe.github.io/medium-editor/) into [Peasy](https://peasy.pushpullfork.com/).) But after writing three posts —  complete with feature images, inline images, and code blocks — in Medium, I decided to import them into [my Jekyll/GitHub Pages site](http://kris.shaffermusic.com/). That’s turned out to be a challenge. Not an insurmountable one, but one that I’d rather avoid going through.

I downloaded my Medium archive, used [Pandoc](http://pandoc.org/) to convert the posts from HTML to MarkDown, and then copied and pasted the MarkDown into new posts on my Jekyll site. There was more post-processing than I anticipated, or would like. And it doesn’t look as easy to automate the cleanup as I would like. 

Even more frustrating was my discovery a couple weeks ago that the Medium API supports *posting* to Medium, but not *retrieving* posts from Medium. It is easy to write code that cross-posts from another platform to Medium, but Medium makes it more difficult to go the other way.

Why?

My guess is that their focus is on content. They want to be the place where we go to find ALL THE CONTENT. So they make it really easy to get content in. Harder to get content out. And by making a beautiful, easy-to-use editor, the temptation is strong to just use Medium from the start. 

If we just want to write, get our writings read, and have a permanent record of what we wrote. Medium can be great. But if we want to write content that we keep coming back to, content that keeps evolving, content that’s part of a long-term project … *and if we don’t want that long-term project to be locked into a single platform* … then Medium may be a problem.

I say as I write this post on Medium.

Because I just can’t resist this editor.

Time to go add some code to Peasy so I can get it ready for prime-time sooner.

*Featured image by [paul bica](https://www.flickr.com/photos/dexxus/5794905716/) (CC BY).*
