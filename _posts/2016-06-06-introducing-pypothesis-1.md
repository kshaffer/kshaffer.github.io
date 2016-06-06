---
layout: post
title: "Introducing Pypothesis ― Part 1: hypothes.is to MarkDown"
modified: 2016-06-06 13:58:00 -0400
image:
  feature: oldtype.jpg
  teaser: oldtype-teaser.jpg
  credit: darkday
  creditlink: https://www.flickr.com/photos/drainrat/16786733075/
share: true
categories: blog
---

I've been working and writing a lot lately about using the web annotation tool [hypothes.is](https://hypothes.is) for public scholarship. It has a lot of cool uses ― not only the collaborative annotation of individual web pages, but also the creation of a [public research notebook](http://kris.shaffermusic.com/2016/04/hypothesis-public-research-notebook/), and the possibility of linking hypothes.is with other apps [through the use of their open API](http://kris.shaffermusic.com/2016/05/getting-started-with-the-hypothesis-api/).

Based on that work, I've created two tools to help people make fuller use of hypothes.is in their work as public scholars. This post is the first in a two-part series introducing and explaining those tools.


## hypothes.is to MarkDown

The first tool is for those who like to blog. This tool is [a simple Python script](https://github.com/kshaffer/pypothesis/blob/master/hypothesisToMarkDown.py) that downloads a batch of hypothes.is annotations (from a single user, tagged with a single tag, or both) and formats them into nice, clean MarkDown text. It's based around the Jekyll platform (the basis for GitHub Pages), but if you use the MarkDown editor for WordPress, it will work for you too, with just one extra step than you might be used to ― but it's a small one! (I'm hoping to build a more automated version for WordPress soon.) The script generates a full Jekyll-friendly MarkDown file, complete with header, so you can use the output as a page on your blog. If you use WordPress or another MarkDown-based blog platform, you can simply copy and paste all the text *except the header* and paste it into a new post/page on your site.

To use the script, download it from the link above, open it in a text editor (not a word processor like MS Word or Apple Pages), and go to the following section near the top of the file:

~~~ python
# adjust these variables for different searches
# also be sure to adjust the page title in the YAML header section
user = 'kris.shaffer@hypothes.is'
tags = 'IndieEdTech'
# search string for fetching annotations from a specific user using a specific tag:
#     searchstring = source + usercall + user + conn + tagcall + tags
# search string for fetching all annotations from a specific user:
searchstring = source + usercall + user
# search string for fetching all annotations from any user, but limited to a specific tag (a class hashtag, for example):
#     searchstring = source + tagcall + tags
filename = 'jekyllOutput.md'
~~~

Here's where you define the search you want to perform. For example, if you want to take all of your annotations and add them to a single page on your blog, simply change 'kris.shaffer@hypothes.is' to your user name, and you're done. If you want to gather all of the public annotations *from anyone* marked with a particular tag, change 'IndieEdTech' to the tag in question. Then put a hash symbol (#) at the beginning of the following line:

~~~ python
searchstring = source + usercall + user
~~~

and delete the hash symbol and spaces from the line:

~~~ python
searchstring = source + tagcall + tags
~~~

If you want to include only *your* public annotations *with a particular tag*, then Update

~~~ python
user = 'kris.shaffer@hypothes.is'
tags = 'IndieEdTech'
~~~

to the user and tag you want, then make sure the only 'searchstring' line without a hash in front of it is:

~~~ python
searchstring = source + usercall + user + conn + tagcall + tags
~~~

You also may want to change the output filename, especially if you use Jekyll and want to run the script regularly to create/update the same page.

If you use a programmer's text editor (TextMate, Atom, etc.), you can run the script right from your editor. Otherwise, open a terminal/command-line window, navigate to the folder the script is in, and type

~~~ bash
python hypothesisToMarkDown.py
~~~

If you have a Jekyll blog and updated the file name appropriately, you're good to go! Now just push it to the server. If you run WordPress, open the output file, copy the new MarkDown text, and paste it into the appropriate page. (Again, be sure you have the MarkDown editor enabled.)

The one downside to this script is that you have to run it regularly ― every time you know or suspect it needs to be updated. The page will not auto-update. (That's one thing I plan on looking into soon.) But for now, it does some cool stuff. :)

Please try it out and let me know how it works. I'm sure that as more people use it, they will notice more kinks that need to be worked out. Also, keep checking for updates, as I'll be fixing and enhancing code as things come up. Enjoy!

Check out [Part 2](http://kris.shaffermusic.com/2016/06/introducing-pypothesis-2/) for a description of the full Python module for programmers interested in making use of the hypothes.is API.
