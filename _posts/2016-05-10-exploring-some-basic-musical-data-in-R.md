---
layout: post
title: "Exploring some basic musical data in R"
modified: 2016-05-10 16:02:00 -0600
image:
  feature: construction.jpg
  teaser: construction-teaser.jpg
  credit: darkday
  creditlink: https://www.flickr.com/photos/drainrat/16550835589/
share: true
categories: [musicology, data science]
---

Learning R? Like music?

I've put together a data set and an R script file with some basic commands to get you started exploring and visualizing musical data in R. The data set is a cleaned up CSV file based on David Temperley's harmonic analyses of 100 'rock' songs for a 2011 article he co-authored with Trevor deClercq: ["A corpus analysis of rock harmony."](http://dx.doi.org/10.1017/S026114301000067X)

Here is [the data file]({{ site.url }}/media/resultsBySong.csv).

And here is [the R script file]({{ site.url }}/media/basicSummariesAndPlots.R).

Assuming you use [RStudio](https://rstudio.com) ― and you should :) ― simply download the two files to the same folder, open the R script in RStudio, and follow the instructions. You can run each individual command by selecting the line and clicking 'run'. Or ― since each command is a single line ― you can simply place your cursor anywhere on the line you want to run, and then press CMD-Return on a Mac or CTRL-Enter on Windows (and probably Linux).

*Note: if you don't use R, you can still download the data and play around with it in Excel, or write your own scripts in Python, Perl, or other language of your choice. It's simply a platform-independent, plain-text spreadsheet file.*
