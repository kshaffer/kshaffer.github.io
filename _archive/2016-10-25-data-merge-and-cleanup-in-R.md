---
layout: post
title: "Data merging and cleanup in R with apply functions"
modified: 2016-10-25 13:11:00 -0400
image:
  feature: airTraffic.jpg
  teaser: airTraffic-teaser.jpg
  credit: NATS Press Office
  creditlink: https://www.flickr.com/photos/natspressoffice/13085091395/
share: true
categories: [coding, data science]
---

I'm working on a data analytics project for Mary Washington's Domain of One's Own initiative. We've got data from several sources (our signup/admin site, Enom, our student information system, the course catalog, faculty self-reports on DoOO projects, etc.). Some of these sources are SQL databases, some are Google spreadsheets, some are Excel files. And all have missing data of some sort. My job is to merge them together in a way that gives us an accurate picture of who on our campus is using DoOO, what kinds of classes are using DoOO, for what kind of projects, and with what kinds of applications. All, of course, without sneaking spyware onto student and faculty domains when they sign up! (This is Domain of One's Own, after all.)

I'm finding R really helpful for this. In other recent projects, I've done the data assembly and cleanup in Python, then the statistical analysis in R. Partly because I knew Python better, and partly because it seemed the better choice for the text wrangling that the data cleanup process requires. This time, though, I've focused entirely on R because it does a really good job of merging (or joining) data sets. And in this project a good bit of the work required to clean up dataset A is to draw on information in datasets B and C. Since the merging and cleaning are so intertwined, doing everything in R just made the most sense.

I've been pleasantly surprised by one feature in R that is proving far superior to Python for this cleanup process: the ```apply``` functions (```apply```, ```tapply```, ```sapply```, ```lapply```, etc.). To clean a particular stream of data in Python, I would write a ```for``` loop that iterates through each record and makes the appropriate change to that record. However, in R, ```for``` loops are generally discouraged in favor of ```apply``` functions. If I understand correctly, R's ```apply``` functions take advantage of a highly optimized matrix multiplication process in C (the low-level language that R compiles to). So I write a function that accomplishes the cleanup process, and then by "multiplying" a data vector by that function, R is able to apply data cleanup procedures significantly faster than a ```for``` loop in Python or other high-level programming languages. And that's really fun, especially with larger datasets.

Now maybe Python has a corresponding feature that I just don't know about! Regardless, R does this really well, and as a result it integrates the data cleanup process with the merging of multiple databases in a way that is relatively simple, self-contained, and super-fast. And that's just what I need right now!

*Feature photo by [NATS Press Office](https://www.flickr.com/photos/natspressoffice/13085091395/).*
