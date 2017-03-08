---
layout: post
title: "Trumping science"
modified: 2017-03-08 15:12:00 -0500
image:
  feature: nasa.jpg
  teaser: nasa-teaser.jpg
  credit: NASA
  creditlink: https://unsplash.com/photos/-hI5dX2ObAs
share: true
categories: [data science, propagandalytics]
short_description: "Science policy is clearly not a priority for the Trump administration. Here are some stats."
---

The Trump administration has been drastically changing the way it communicates information with the public. One of the first pages people noticed missing from the Trump administration's website was the page on climate change. Deleting the previous administration's information and rebuilding whitehouse.gov is not unheard of, but this is part of a bigger trend of mis/disinformation from the Trump administration. As <a href="/2017/02/misinformation-trump-administration/" target="blank_">I wrote a couple weeks ago</a>,

> the Trump administration is obfuscating information. Delete important content, make drastic changes to existing content, replace user-friendly web sites with PDFs and Word documents, pull back on social media usage, limit federal employee access to the press, and leave the press’s inquiries unanswered by the press secretary. ... [This] harrowing picture of our current government’s approach to information [is] not surprising given the media history of Trump and several of his top advisors. But it’s incredibly dangerous.

Now that Trump has been in office for over a month, he's had a chance to start replacing content on whitehouse.gov. So what changes has his administration been making?

I've been looking into several areas - science, immigration, Russia, etc. In this post, I'll share what I've found about the Trump administration's approach to science, in particular climate change.

## The data

I started by searching my archives for mentions of the words *science* and *climate*, and the phrase *global warming* (I used snapshots of whitehouse.gov from January 20 and March 1). Once stop words ("a", "an", "the", "of", etc.) were removed, Obama's site had a total of almost **2.5 million words,** while Trump's site had approximately **870,000 words,** about one-third the size. In that context, **the word *science* occurred 7,402 times on Obama's site, but only 116 times on Trump's!** *Sciences* occurred 129 and 15 times, respectively. Even more stark, ***climate* occurs 6,534 times on Obama's site, but only 97 times on Trump's!** Global warming occurs 15 times on Obama's site, and not at all on Trump's.

This is embarrassing.

But raw word counts only tell us so much. *How* do Obama's and Trump's sites talk about science in the speeches, press briefings, executive orders, and other documents they contain? Here are the most phrases containing "science" that are most characteristic of each of the administrations' sites. These are not all the two-word phrases, only those with the strongest difference in relative frequency between the two sites (based on a <a href="https://en.wikipedia.org/wiki/Odds_ratio" target="blank_">log odds ratio</a>).

<a href="/assets/images/science_mar1.png" target="blank_"><img src="/assets/images/science_mar1.png" alt="Top terms containing 'science' on whitehouse.gov, Trump vs. Obama, log odds ratio." /></a>

The terms don't seem all that different until we realize that many of the terms on Trump's list (which occur far less often than the terms on Obama's list) are largely those associated with bios of former presidents, vice presidents, their spouses, and other individuals featured on the site. "Library science", for example, exclusively occurs on Laura Bush's biography (which also occurs on Obama's site). While these bios occur on both sites, the terms in them show up as the science terms most characteristic of Trump's site *because there is so little about science on his site to begin with.* Science policy is clearly not a priority for the beginning of the Trump administration.

*Climate* is a term less frequently occurring on bios, or even historical pages about science, as Americans recently moved from talking about *global warming* to *climate change*. Here are the most common phrases for Trump's and Obama's sites containing the word "climate".

<a href="/assets/images/climate_mar1.png" target="blank_"><img src="/assets/images/climate_mar1.png" alt="Top terms containing 'climate' on whitehouse.gov, Trump vs. Obama, log odds ratio." /></a>

Not only does Trump not use the term climate very often (97 times vs. Obama's 6,534 times), but when he uses the word climate, he's not even talking about science! Oh, and the vast majority of those 97 mentions of climate change come from historical material from past administrations preserved on the current whitehouse.gov. If we remove those historical pages from both archives, Trump only uses the word *climate* 31 times, to Obama's 6,534.

Here are the most characteristic phrases containing *climate* on each site, with historical archives removed.

<a href="/assets/images/climate_non_hist_mar1.png" target="blank_"><img src="/assets/images/climate_non_hist_mar1.png" alt="Top terms containing 'climate' on whitehouse.gov, Trump vs. Obama, log odds ratio, no historically preserved pages." /></a>

*Note: "milder climate" is from Mamie Eisenhower's bio.*

Obama uses *climate* to talk about the environment. Trump uses *climate* to talk about money.

Again, this is embarrassing. Not surprising, but embarrassing. And coupled with the cuts being proposed to NOAA, the EPA, and other agencies conducting climate and other scientific research, it's downright dangerous.

## Coming next...

This isn't all I've examined. In upcoming posts, I'll dive into how Trump talks about immigration, terrorism, Russia, and a strange obsession with topics from the Cold War (?!).

And if you're interested, check out the code and play around with this yourself. Or drop me a line and let me know what else you're interested in seeing.

*All data and code for this analysis can be downloaded from my <a href="https://github.com/kshaffer/whitehouse" target="blank_">whitehouse GitHub repository</a>.*

*Header image by <a href="https://unsplash.com/photos/-hI5dX2ObAs" target="blank_">NASA</a>.*
