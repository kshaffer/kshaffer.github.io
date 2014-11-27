---
layout: post
title: "Command-line tools on the iPad"
date: 2013-12-28 22:55
comments: true
categories: blog
share: true
tags:
- command-line  
- git  
- GitHub  
- Linux  
- iPad
---

I really like working from my iPad, especially when it means carrying around something lighter than the 15" MacBook Pro that CU gave me for work (something I care about more now that I take the bus to work and walk about 10 minutes each way to the bus stop). However, I do a *lot* of work on the command line and in a text editor, things which are native to a computer, but not the iPad. Fortunately, thanks to inspiration from a friend who works at CERN and [this article](http://m.linuxjournal.com/content/swap-your-laptop-ipad-linode) from *Linux Journal*, I've figured out a way to do a lot of that on the iPad pretty cheaply—nearly free, in fact (apart from things I was already paying for before). Following are some of the tools and workflows I've found helpful.

First, I've found two great text editors for iPad. I write almost all of my text in [Markdown](http://daringfireball.net/projects/markdown/) already, and there are a number of Markdown-friendly editors for the iPad. My favorite is probably [WritingKit](http://getwritingkit.com) ($5). It has a decent preview mode, embedded browser, and an extra line of keys on the keyboard that can be switched between Markdown and other standard tools. It also has an ingenious feature that I always miss in every other iPad program: tapping in the left margin moves the cursor left one space, and tapping in the right margin moves the cursor right one space. This makes typing without a bluetooth keyboard so much more friendly. The second editor is [Textastic](http://www.textasticapp.com) ($9). I just got this and like it so far. It can access (s)ftp servers, DropBox, and has its own WebDAV server for smoother file transfer than a lot of apps. It also has built in snytax highlighting for many programming languages, Markdown, and even [Lilypond](http://www.lilypond.org) music notation files. Like WritingKit, it also has an extra line of keys, though it is designed more for programming than for writing.

These editors are great for manipulating text files, but the iPad still lacks an environment in which to *run* Lilypond, Python, or a Markdown translator. However, I recently switched my website from a shared host to a virtual private server ([DigitalOcean](http://www.digitalocean.com)), which provides me not only a web server but also a place to do command-line work. Using the free app ServerAuditor, I can log into my server on the iPad with full access to the Linux environment (via ssh). I can run Lilypond, use [Octopress](http://www.octopress.org) to update my blog, use [git](http://www.git-scm.com) for version control and to access all of my materials on [GitHub](http://www.github.com), run Python scripts (including the [music21](http://web.mit.edu/music21/) framework for computer-aided musicology)—anything you can do on the command line in Debian Linux.

Though there are limitations, of course, I've really liked this setup. I can carry around a vey light device with very little hard disk space, and between DropBox and my DigitalOcean server, I have access to a fair amount of data and processing power, with most of my daily-use tools available from the command line. If you're a command-line user and an iPad owner, I highly recommend getting a virtual private server (starting at $5/month), ServerAuditor (or something like it), and a decent iPad text editor. It's a lot of power, with very little to carry around.