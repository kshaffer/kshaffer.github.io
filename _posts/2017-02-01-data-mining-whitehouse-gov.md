---
layout: post
title: "Data mining whitehouse.gov"
modified: 2017-02-01 11:25:00 -0500
image:
  feature: columns.jpg
  teaser: columns-teaser.jpg
share: true
categories: [data science]
short_description: "What has the Trump administration changed on whitehouse.gov?"
---

When Donald Trump became president of the United States, a lot disappeared from the administration website, <a href="https://whitehouse.gov" target="_blank">whitehouse.gov</a>. This is standard practice for a new administration, and the Obama administration's website is still available, both at <a href="https://obamawhitehouse.archives.gov/" target="_blank">obamawhitehouse.archives.gov</a> and in various snapshots in time via the <a href="https://archive.org/web/web.php" target="_blank">Internet Archive Wayback Machine</a>. Nevertheless, there are some significant changes and omissions, and certainly more to come. So I've decided to spend some time finding and tracking the changes on the Trump administration's official website.

I'm planning on investigating differences between the public statements of the Trump and Obama administrations, as well as tracking emerging changes in language, priorities, and policies over the next four years. All my code and the (pre-processed) data that I download will be made publicly available in the project's <a href="https://github.com/kshaffer/whitehouse" target="_blank">GitHub repository</a>. For those who want to use the code or download the data to do your own analysis, you can find detailed instructions there. I welcome contributions that improve the code or refine the web scraping and data-mining process.

I'm still early in this process, and the Trump administration is still early in the process of building out the site, but here are some high-level findings so far.

## The scope

The Trump administration has a much leaner whitehouse.gov so far. I scraped and downloaded the entirety of whitehouse.gov from January 20 (before the transition), January 25, and again on January 31. The final version of the Obama administration's whitehouse.gov on January 20 constituted **411 MB** of data. Trump's whitehouse.gov on January 25 had just **44 MB** and on January 31 was up to **51 MB.** That's a pretty significant drop in content!

And lest we assume that Obama's website contained a large amount of media that puffed up that total, here is the amount of data contained just in the <a href="https://github.com/kshaffer/whitehouse/tree/master/data" target="_blank">text extracted from the HTML files</a> on the site:

| date | text data |
| --: | :-- |
| January 20 | 28.0 MB |
| January 25 | 1.3 MB |
| January 31 | 1.7 MB |

The drop in text content is even more precipitous. (And it's even greater when you consider that a significant portion of that 1.3 MB involves pages that are on Obama's site, too ― boilerplate administrative pages, biographies of former presidents and first ladies, etc.)

So my first conclusion from comparing Obama's and Trump's websites is that the information on Trump's website is extremely sparse. Some of this is due to the early stage in which the administration finds itself. But not all.

## What pages have appeared and disappeared?

117 pages that existed on the Obama administration's site remain on the Trump administration's site. The bulk of <a href="https://github.com/kshaffer/whitehouse/tree/master/diffs" target="_blank">these pages</a> are biographies of former presidents and first ladies, with some general administrative boilerplate pages (such as "The Executive Branch" or "The Constitution").

124 pages are new with the Trump administration. <a href="https://github.com/kshaffer/whitehouse/blob/master/diffs/pages_new_with_trump.csv" target="_blank">These pages</a> primarily include executive orders, transcripts of phone calls with foreign leaders, press briefings, and other timely announcements. (<a href="https://github.com/kshaffer/whitehouse/blob/master/diffs/pages_new_or_deleted_on_Jan31.csv" target="_blank">59 of these pages were added between January 25 and January 31</a>.)

There are <a href="https://github.com/kshaffer/whitehouse/blob/master/diffs/pages_unique_to_obama.csv" target="_blank">2583 pages</a> that are unique to the Obama administration's site. I haven't looked closely enough to see if any of these are replaced by new pages on the site with different titles, but it's clear from the difference between the size of this list and the 124 pages unique to Trump's site, that much has been removed. A lot of what was deleted involves timely updates from Obama's tenure and makes sense to be moved to an archive site, rather than remaining on whitehouse.gov. However, the deletion of pages referring to the signup deadlines for the Affordable Care Act, pages that summarize and link to federally funded research on climate change, etc. is a significant move from the administration. Time will tell what will be replaced, and in what format. But for now, the omission of some of these specific pages from whitehouse.gov is important to note. And if it's your field, to respond to.

## The Judicial Branch

One page that many people noted missing from whitehouse.gov a few days ago was the page for the Judicial Branch. While The Executive Branch, The Legislative Branch, and (perhaps ironically) The Constitution still retained their pages on the Trump administration's site, the page about the judiciary and the Supreme Court was a notable absence. It is <a href="https://github.com/kshaffer/whitehouse/blob/master/diffs/pages_new_or_deleted_on_Jan31.csv" target="_blank">now back up</a> and contains the same text content, but was absent for several days. Under other circumstances, I would just assume an honest mistake during the process of rebuilding the site from scratch. But given the current disputes between the Executive Branch (including agencies like DHS and CBP) and the federal judiciary, the omission is at the very least more problematic, perhaps even ominous. Again, it's back up now. But these kinds of deletions and omissions are the kinds of things that I hope to track through this project.

## Going forward

I've done some preliminary text mining and content comparison between Trump's and Obama's site, but given how little data is on Trump's site relative to Obama's, there's not much to find there yet. However, as the site gets built up, I'm going to be diving deeper into the specific content of the new administration's site and comparing it to both Obama's site and previous versions of Trump's site. Hopefully this study can reveal emerging trends that might otherwise get missed, and can help us know how best to respond to those trends and any problematic (or missing) language on the site.

If you'd like to join in on this project, visit the <a href="https://github.com/kshaffer/whitehouse" target="_blank">GitHub repository</a> and play around with the code, the data, or even just read the text and see what stands out. If you notice anything, please let me know. And feel free to send a pull request or reach out if you want to collaborate more formally.

I'm hoping that this and some other projects I'm working on (looking at you, Steve Bannon...) can help shed light into the darkness by opening, curating, and analyzing data about the Trump administration and its activities, and providing code and methods for those looking to dive into that data.

Good night, and good luck.

<i>Header image by <a href="https://unsplash.com/photos/X2CxUXFqKcM" target="_blank">Chris Brignola</a>.</i>
