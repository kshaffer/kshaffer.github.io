---
layout: post
title: "Text mining the new whitehouse.gov"
modified: 2017-01-25 11:35:00 -0500
image:
  feature:
  teaser:
  credit:
  creditlink:
share: true
categories: [data science, coding]
short_description: "What is (and isn't) on the new whitehouse.gov?"
---

[Whitehouse.gov](https://whitehouse.gov) has changed a lot since the inauguration. Many have noted specific things that have disappeared recently, such as pages on climate change, Spanish-language content, etc. I thought I'd put my web-scraping and text-mining skills to work and investigate it more thoroughly.

## What I've found so far

The first, and most staggering, thing I've found so far is the vast difference in the amount of data contained in Trump's and Obama's whitehouse.gov sites. As of January 25, 2017, Trump's whitehouse.gov contains **44 megabytes** of data. After several hours of downloading, the January 20, 2017, snapshot of Obama's whitehouse.gov is **9.6 *giga*bytes** and counting. While I can understand a new administration wanting to rebuild the website from scratch, that's a lot of content to delete and not replace immediately, and it's not all information specific to the Obama administration. I'll write more about the details of the content that was deleted when the scrape finishes, but for now, I want to point out just how much was deleted by the new administration. Over 9 gigabytes of data, and most of the files are plain text. That's a lot of data.

Since so little is on the current site, and I don't have a full download of the Obama site yet, there's not much to mine and analyze just yet. But at least one important insight emerges. Take a look at the most common (non-stop) words in Trump's site.

<img src="/assets/images/trump_whitehouse_words.png" alt="Most common non-stop words in Trump's whitehouse.gov site as of Jan 25, 2017" />

We'd expect white, house, president, etc. to be at the top of the list, but hardly anything on this list is indicative of any specific policies or positions. They are the boilerplate words we would expect from the site skeleton.

The same is true for the most common bigrams (two-word phrases) and trigrams (three-word phrases).

<img src="/assets/images/trump_whitehouse_bigrams.png" alt="Most common bigrams in Trump's whitehouse.gov site as of Jan 25, 2017" />

<img src="/assets/images/trump_whitehouse_trigrams.png" alt="Most common trigrams in Trump's whitehouse.gov site as of Jan 25, 2017" />

In fact, these tables seem even more boilerplate than the top single words. What that means to me, in conjunction with the large drop in total amount of data on the site from January 20 to January 25, is that the site is more-or-less empty. While there are some policy pages and information releases, a large amount of the content is boilerplate and site-architectural (even after removing as many of the page headers and footers as I could), rather than providing specifics about how the administration is governing and plans to govern going forward.

I'm hopeful that going forward, we'll get a lot more information. But the way things have gone this week, I'm not sure *transparency* is this administration's watchword.



*If you're interested in how I scraped the content and/or want to download my script to do it yourself, keep reading. Otherwise, feel free to stop here, but stay tuned for updates as I get more data and do more analysis!*

## Scraping and pre-processing

To start, I wanted to download the current whitehouse.gov site, as well as the last version of whitehouse.gov from the Obama administration. Then I could extract text content and make some comparisons. Downloading the current version is really easy. Assuming you have wget installed (if not, I highly recommend [homebrew](http://brew.sh/) for Mac), you can download the entire website in just a few seconds with a single line of code pasted into the command line.

~~~bash
wget -r -e robots=off --convert-links -nd https://www.whitehouse.gov
~~~

This will tell whitehouse.gov that your computer isn't a script (\*wink\*), follow the links on the homepage to other pages on the domain, follow those pages' links, and so on..., download all content from whitehouse.gov that it finds, put them in a single folder on your computer, and convert the links in those files to refer to the newly downloaded files on your computer (so you can click on the links in the site you downloaded and navigate the site locally).

Next, I created a bunch of folders for different file types: ```css```, ```docs```, ```fonts```, ```html```, ```images```, and ```scripts```. I moved all the downloaded files to the respective folders for those file types. (```mv *.png ./images/``` to move all ```png``` files to the ```images``` folder, for example.) Now all the text is in one folder, making it easier to analyze, and leaving images, PDFs, etc. in easily findable for future analyses.

I created a [Python script](https://github.com/kshaffer/whitehouse/blob/master/make_the_soup.py) that uses the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) package to take all the files in a single folder and extract their titles and their main page content (following the back-end formatting used by whitehouse.gov). If you are going to use this script, make sure to edit the ```source_folder``` and ```output_file``` variables at the beginning of the script to point to the input and output you want to analyze. Then just run ```python make_the_soup.py``` to run the script and convert the folder full of html pages into a single CSV file that can be used for data analysis.

Things are a bit more tricky for archives of whitehouse.gov than for the current version, for two reasons. First, you have to download it from the [Internet Archive's Wayback Machine](https://archive.org/web/), which is slower and a bit more complex on the backend than whitehouse.gov. Second, and more importantly, the latter versions of the Obama administration's website contained a *lot* more information than the Trump administration includes in their website to date. After several hours, wget is still downloading content! When it's finished, I'll have more to report, but for now, here's the wget code for downloading an Internet Archive snapshot (the timestamp of the snapshot will change depending on which snapshot you want to download):

~~~bash
wget -r -e robots=off --convert-links -nd http://web.archive.org/web/201701200112330/https://www.whitehouse.gov
~~~

## Mining and analyzing

Because there is very little data to mine (until the Obama website is downloaded), the [text mining script](https://github.com/kshaffer/whitehouse/blob/master/mine_the_text.R) is still fairly sparse. Like in my [New York Philharmonic study](/2017/01/data-mining-the-new-york-philharmonic-performance-history/), I use TidyVerse tools in R to do the mining and analysis. So far what's included is code to unnest the CSV file created above by word, bigram, and trigram, and then to plot the most common words, bigrams, and trigrams (with stop words removed) from the website's text. This file will grow as I get more data and do more with it.
