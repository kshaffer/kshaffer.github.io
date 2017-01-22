---
layout: post
title: "Hypothes.is as a public research notebook"
modified: 2016-04-30 16:25:00 -0600
image:
  feature: trooperbook.jpg
  teaser: trooperbook-teaser.jpg
  credit: Peter Hopper
  creditlink: https://www.flickr.com/photos/whisperwolf/3675980379/
share: true
categories: [coding]
---

Can we do scholarly work in public without relying on for-profit "social" platforms?

This is a big question I've been mulling over lately, especially as my new position at the University of Mary Washington will involve significant work on the [Domain of One's Own](http://umw.domains/) project. I won't tackle all the implications of that question in a single blog post, but I do want to address one aspect of it: can we share things of value we discover ― and our thoughts about them ― without providing free labor or content to for-profit tech corporations? Even better, can we do so without everyone becoming a coder, web designer, and server administrator?

## hypothes.is

One tool that can help us accomplish this is [hypothes.is.](https://hypothes.is) Hypothes.is is an open annotation tool for the web, allowing anyone to highlight, annotate, or comment on any webpage via a Chrome plugin (web developers can also install it on their sites, like I have with my blog). It's similar to how Medium users can annotate and highlight blog posts on that platform, but you can use the hypothes.is plugin on any website. It's important to note that hypothes.is users don't alter the original website. Rather the hypothes.is plugin adds an annotation/highlighting layer *over* the webpage that only hypothes.is users can see, and hypothes.is users can toggle that annotation/highlighting layer on and off as they like. Here's a video intro to the hypothes.is project:

<iframe src="https://player.vimeo.com/video/29633009" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

Most discussion I've seen about hypothes.is has centered around this feature of page annotation, often discussing ways in which, say, [students in a class can collaboratively annotate](https://hypothes.is/quick-start-guide/) a single page [as they study it together](http://acdigitalpedagogy.org/category/hypothes-is/). However, hypothes.is has other, lesser known features that, in my mind, are both more interesting and more powerful.

## The hypothes.is stream

What I think makes hypothes.is really interesting is the [stream.](https://hypothes.is/stream) Here you can find every public annotation in reverse time order (like Twitter). There is even an RSS feed for this stream. Of course, most people don't want to read *every* annotation, so you can limit the results by user, tag, or search content. You can also send it simple queries in the URL. (Read more about these queries [here.](https://hypothes.is/for-publishers/))

For example, here are [all of my public annotations](https://hypothes.is/stream?q=user:kris.shaffer). And here are all public annotations tagged [IndieWeb](https://hypothes.is/stream?q=tag:IndieWeb).

This means that scholars and students working in public can share the online resources they've found valuable, as well as their reactions to it, while using an "indie" tool, and without installing anything more complicated than a browser plugin. (Though, at least for now, that plugin means relying on Google, but one step at a time.) It also means that we can follow each other's work, as well as connect with others working on similar topics (via tags).


## The hypothes.is API

There are some limitations to the hypothes.is stream. Which, of course, is understandable given how young the tool is, and how much focus the annotation of individual pages has received, rather than the potential of the stream.

Users cannot directly download their annotations. As far as I can tell, they all live on the hypothes.is server. It also seems as if it's not possible to combine search queries in the stream... say, all annotations by me *and* tagged IndieWeb. Or all annotations tagged with a class tag and a topical tag. (Someone please correct me if I'm wrong about these things, as I'd love to be able to do them!)

However, since hypothes.is is committed to supporting open work and seems to have an interest in collaborating with other developers and researchers, they have a fairly robust API (application programming interface). While most users will not tap into the API directly, it is possible for other IndieWeb and IndieEdTech developers to create tools that interact with and build on hypothes.is. Perhaps creating a WordPress plugin that will take all of a user's annotations and collect them in a page on their website, integrated with the site's theming. Or creating a program that will automatically publish all of a user's annotations as bookmarks on their [Known](https://withknown.com) site, and maybe even cross-post those to Twitter. Things like these would make it even more powerful for non-coders interested in indie and non-profit tools. (These are some of the projects I hope to work on in my new role at UMW.)

One common drawback to IndieWeb and open-source tools is that they tend to require a significant technological background in order to use. So I like it a lot when someone makes a tool that is easy for most people to use, but also readily "hackable" for those of us who want to get under the hood and see how we might extend it. I'm excited to see what else it can do, and what cool things I can do with its API.

I'll keep you posted... :)

## Update

Since writing this post, I've been digging into the hypothes.is API and doing some work. I've created a Python module called [Pypothesis](https://github.com/kshaffer/pypothesis), which makes for fairly easy interaction with the hypothes.is API in a programming environment ― at least the GET part of the API, which fetches public annotations without needing to authenticate. Also included with Pypothesis is [a script](https://github.com/kshaffer/pypothesis/blob/master/hypothesisToJekyll.py) that will download a user's annotations, annotations with a particular tag, or both, then extract the important information from them and write them to a simple MarkDown format. The output is a well-formed [Jekyll-friendly](https://jekyllrb.com/) page, which makes for easy use if you have [a blog hosted on GitHub](https://pages.github.com/). But the MarkDown can also be converted to HTML with a program like [PanDoc](http://pandoc.org/) or [MultiMarkDown](http://fletcherpenney.net/multimarkdown/), or pasted right into WordPress, [if you enable MarkDown](https://en.support.wordpress.com/markdown/). I'll be blogging in more detail about this Python module and future derivative projects soon, but for now, check it out on GitHub and [read the (fairly detailed) documentation](https://github.com/kshaffer/pypothesis/blob/master/README.md) if you'd like to give it a whirl.
