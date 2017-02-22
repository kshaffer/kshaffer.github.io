---
layout: post
title: "(Mis)information and the Trump administration"
modified: 2017-02-22 11:26:00 -0500
image:
  feature: newspaper.jpg
  teaser: newspaper-teaser.jpg
  credit: Kaboompics
  creditlink: https://www.pexels.com/photo/man-reading-newspaper-6053/
share: true
categories: [data science]
short_description: "The Trump administration has made major changes to federal agency websites. Just how major?"
---

Almost immediately after the election, people started noticing pages disappearing from federal government websites. Some of this is par for the course in a new administration. Of course the Trump administration cleaned out the Obama-specific pages on <a href="https://whitehouse.gov" target="blank_">whitehouse.gov</a> and started with a clean slate. <a href="https://web.archive.org/web/20090122232821/http://www.whitehouse.gov/blog/change_has_come_to_whitehouse-gov/" target="blank_">So did Obama</a>.

But in many ways, this seemed to be different. At the same time that whitehouse.gov was changing, Washington was instituting social media gag orders and <a href="https://www.theguardian.com/us-news/2017/jan/24/epa-department-agriculture-social-media-gag-order-trump" target="blank_">forbidding employees from talking with the public or the press</a> about their agency's research. And then people started noticing pages disappearing from websites that don't usually change much when a new administration takes over: <a href="https://www.washingtonpost.com/news/animalia/wp/2017/02/03/the-usda-abruptly-removes-animal-welfare-information-from-its-website/?utm_term=.b41edb1c581b" target="blank_">usda.gov</a>, ed.gov, ... And one of the more conspicuous deletions ― <a href="http://thememoryhole2.org/blog/ed-idea" target="blank_">idea.ed.gov</a>, a site dedicated to helping teachers, students, and parents navigate the Individuals with Disabilities Education Act (<a href="http://idea.ed.gov" target="blank_">now back up</a>) ― just happened to come a day after Betsy DeVos was confirmed as Secretary of Education. The same Betsy DeVos who <a href="https://www.washingtonpost.com/news/answer-sheet/wp/2017/01/17/betsy-devos-confused-about-federal-law-protecting-students-with-disabilities/?utm_term=.84b1cd5e1044" target="blank_">didn't know that IDEA was federal law</a> and would prefer that states and districts exercise their own judgment when dealing with disability-related issues.

As this news started to break, I was already looking for a new research project. Preferably one that would allow me to use (and hone) my skills as a data scientist in service of the public good. So I decided to start <a href="http://pushpullfork.com/2017/02/data-mining-whitehouse-gov/" target="blank_">scraping, spidering, mining, and analyzing federal government websites</a>, looking for additions, changes, and deletions, and comparing the content of these websites with their Obama-era counterparts. I'm still developing the code for some of that project, and figuring out how I can store and manage all the data that I want to collect. But I've got a good start on whitehouse.gov and ed.gov, with more news on that coming soon.

In the mean time, I found a really great tool from the Internet Archive's <a href="https://archive.org/web/web.php" target="blank_">Wayback Machine</a>. The Wayback Machine allows anyone to view old versions of websites. They crawl and scrape large swaths of the web on a regular basis, and as long as their scraper collected the data, anyone can view it. While for sites like my own blog, a lot of changes go unnoticed by the Wayback Machine, federal government websites have been scraped regularly from the very beginning, often crawled multiple times per day looking for updates, so it's a fairly reliable source, and definitely the best we have.

The ability to go to <a href="https://archive.org" target="blank_">archive.org</a> and search millions of websites from the past 20 years is amazing. But for big-data research, there's an even better tool: <a href="https://archive.org/help/wayback_api.php" target="blank_">their API</a>. In particular, I've found their <a href="https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server" target="blank_">CDX Server API</a> to be an amazing tool when studying changes in a website over time. You feed it a query (just a simple URL string, no authentication needed), and it returns the *entire change history* for all of the snapshots in the Wayback Machine archive for a domain. Want to download a single text file containing all of the additions and changes on ed.gov discovered by the Wayback Machine in the past 20 years? No problem. Just open a browser, type in

    http://web.archive.org/cdx/search/cdx?url=ed.gov&amp;matchType=domain&amp;output=json&amp;collapse=digest

and wait for a minute. When the page finishes loading, click save. Now you've got it! The entire history of page additions and changes for the domain whitehouse.gov and all its subdomains found by the Wayback Machine, with any duplicate pages found in successive snapshots collapsed into single entries.

There's one catch: the Wayback Machine is focused on finding old versions of pages that have since been changed or deleted. It does *not* preserve an easy-to-query history of page *deletions*. And while it's possible to ascertain that information from a spider crawl of the entire archive, their server (purposefully?) makes that a slow process. Given the size of these archives, it would take days. So an analysis of page deletions will have to happen another way.

With that caveat in mind, I wrote <a href="https://github.com/kshaffer/websitewatcher/blob/master/cdx_downloader.R" target="blank_">an R script</a> that will query the change/addition history for six federal agency websites (whitehouse.gov, ed.gov, fcc.gov, epa.gov, usda.gov, and nps.gov) as well as several retail, journalistic, and non-profit organization websites to serve as a baseline comparison. What I found was mind-blowing. In fact, I'm still not sure I believe it. But here goes...

## The 20-year history

The first thing I did with this data was plot out the changes over time. The following image shows the number of page changes/additions per month for each of the six federal websites I analyzed. Notice anything?

<img src="/assets/images/gov_by_month.png" alt="changes and additions to .gov websites over time, by month" />

That spike at the end? That's January 2017. Wow.

Now, a few things could be happening here. It could be indicative of the changes that usually accompany a new administration. But if we look to January 2001 and 2009, there is no comparable spike. There are local peaks at the beginning of Bush's and Obama's administrations, but nothing like Trump's.

So I thought there might be a change in how the Wayback Machine takes its snapshots. Maybe it's just taking that many more snapshots now, so it catches all the little changes in 2017 that would have been combined into fewer, but more substantive, changes found by the Wayback Machine in 2001 and 2009. When you visit <a href="https://web.archive.org/web/20170222055950/https://www.whitehouse.gov/" target="blank_">a page on the Wayback Machine</a>, there is a discernible increase in snapshots over time. But is it this big and this precipitous?

The simplest way to test that was to examine change histories for non-government websites. So I queried the change history of seven retail, non-profit, and journalistic websites that update at a variety of frequencies ― <a href="https://washingtonpost.com" target="blank_">washingtonpost.com</a>, <a href="https://theguardian.com" target="blank_">theguardian.com</a>, <a href="https://npr.org" target="blank_">npr.org</a>, <a href="https://www.aspca.org/" target="blank_">aspca.org</a>, <a href="https://societymusictheory.org/" target="blank_">societymusictheory.org</a>, <a href="https://www.psychologytoday.com/" target="blank_">psychologytoday.com</a>, and <a href="https://target.com" target="blank_">target.com</a>. Here are their change histories:

<img src="/assets/images/non_gov_by_month.png" alt="changes and additions to commercial and non-profit websites over time, by month" />

These sites actually reflect something more like the general trend of increasing snapshots over time than the .gov websites do (as well as an apparently major site overhaul on Target.com last summer!). But with the exception of *Washington Post* and *The Guardian* (which spend much of their time covering government activity), there is no major spike in early 2017.

So as far as I can tell, the increase in .gov site changes in early 2017 is not an artifact of changes in the way the Wayback Machine crawls the web. And it's huge. But maybe it's not just Trump? Maybe Obama's agencies were making a lot of changes at the end of the administration, too?

Here's a day-by-day breakdown of changes from January 1 to February 15, 2017. It's pretty clear that the bulk of the changes come after the inauguration.

<img src="/assets/images/gov_by_day.png" alt="changes and additions to .gov websites Jan 1-Feb 15, by day" />

The non-government websites do not show such a change, even the journalistic ones.

<img src="/assets/images/non_gov_by_day.png" alt="changes and additions to commercial and non-profit websites Jan 1-Feb 15, by day" />

So the best explanation I can come up with so far is that the Trump administration is making major additions and changes to federal agency websites. There's still the possibility that these are many *small* changes, rather than large changes. To explore that requires a more detailed study of larger downloads of data from those websites. (And <a href="/2017/02/data-mining-whitehouse-gov/" target="blank_">I'm working on that</a>, too!) But **something has definitely changed about how the federal government communicates information to the public digitally.** And taken together with the gag orders, <a href="https://www.nytimes.com/2017/02/07/us/politics/the-white-house-list-of-terror-attacks-underreported-by-media.html" target="blank_">the misdirection from the press secretary</a>, and the page deletions already documented, this is major. Our federal government is changing the way it communicates with us, it is not being transparent about those changes, and it becomes more likely with each passing day that important information is being withheld.

This is a problem.

## Content types

In addition to adding, deleting, and changing content, the Trump administration is making major changes to the types of content on .gov sites. The most common file types in the .gov dataset overtime are HTML (regular web pages), PDF documents, plain text, JPEG images, and Microsoft Word documents, with HTML documents comprising 60% of the pages in the .gov dataset. When it comes to engaging information on the web, HTML and plain text are the most accessible and the most versatile, with Word documents and especially PDFs being more difficult to work with. (You may think everyone has MS Word and a PDF reader, but the added layers of browser plugins, downloads, and the tax-form-like formatting of many of these PDFs make them significantly less user-friendly than a well designed web page. Think <a href="https://irs.gov" target="blank_">IRS.gov</a>.)

Not surprisingly, the past few weeks have seen a significant change in file type. Here is a change history of these six .gov websites, separated by file type instead of by site.

<img src="/assets/images/gov_file_types.png" alt="changes and additions to .gov websites over time, by file type" />

While HTML files go up in January 2017, they are far outstripped by PDFs, and their rate of increase is outstripped by Word docs. In fact, January 2017 brought 134,733 of the 185,468 PDFs in the history of these websites (73%!) and 17,149 of the 26,772 Word docs in the sites' history (64%). On the other hand, January 2017 saw 38,881 new or changed HTML pages, just 5% of the 725,119 in the whole dataset.

This is further evidence that the Trump administration is obfuscating information. Delete important content, make drastic changes to existing content, replace user-friendly web sites with PDFs and Word documents, pull back on social media usage, limit federal employee access to the press, and leave the press's inquiries unanswered by the press secretary.

## A harrowing picture

In the weeks to come, I'll be refining my software and statistical models to look in more depth at specific content changes on some of these sites. But even this "distant read" paints a harrowing picture of our current government's approach to information. It's not surprising given the media history of Trump and several of his top advisors. But it's incredibly dangerous.

What can we do? To start, we can support the efforts of the Internet Archive, especially as they pursue <a href="http://blog.archive.org/2016/11/29/help-us-keep-the-archive-free-accessible-and-private/" target="blank_">plans for a mirror outside the United States</a>. We can keep a close eye on these government sites, looking at which domains, subdomains, and pages are changing the most frequently. We can draw attention to particularly problematic deletions, additions, and changes. We can mirror and share data elsewhere on the web. And we can demand transparency from others in government who are in position to counter this trend from the Executive Branch.

I've decided to spend time and energy setting up tools to accomplish some of these things, particularly the watching and the analyzing. It's something I can do to help, and hopefully it will prove valuable. I'll keep posting regular updates, and please check out my <a href="https://github.com/kshaffer/whitehouse" target="blank_">whitehouse</a> and <a href="https://github.com/kshaffer/websitewatcher" target="blank_">websitewatcher</a> repositories on GitHub if you want to run the code for yourself or contribute to the project.

<i>Header image by <a href="https://www.pexels.com/photo/man-reading-newspaper-6053/" target="blank_">Kaboompics</a>.</i>
