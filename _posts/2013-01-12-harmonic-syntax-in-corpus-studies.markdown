---
author: KShaffer
comments: true
date: 2013-01-12 15:39:24
layout: post
slug: harmonic-syntax-in-corpus-studies
title: Harmonic syntax in corpus studies
categories: [musicology, data science]
share: true
wordpress_id: 665
tags:
- analysis
- corpus studies
- digital humanities
- music
- Scholarship
---

I've been conversing with several different music scholars lately about methodology in corpus studies. Some of this has taken place on this blog, some on Twitter, and some over email. I've been talking about the same thing with a bunch of different people in a bunch of different places, when this is a conversation that would be greatly enhanced by all of us discussing it in one place. This post is an attempt to do that.

The discussion has centered around the proper method of calculating chord transition probabilities from a sample of musical works: given a particular chord, what is the relative probability that some other chord will come next. The standard method, which I've discussed in previous posts ([Rock corpus comparison](/2012/12/rock-corpus-comparison/); [Averages, clusters, and hidden patterns](/2012/07/averages-clusters-and-hidden-patterns/), and [Problems with using transitional probabilities in musical corpus studies](/2012/06/problems-with-using-transitional-probability-in-musical-corpus-studies/)), is to count up all the instances of different types of chord-to-chord transitions in the collection of songs/pieces and assign probability according to their frequency of the entire corpus (by percentage). In a previous post, and in a draft of an article I'm working on which I circulated to a small group of people, I noted three problems:


* Long songs that repeat the same chord progression many times exert a disproportionately large influence on the corpus's "average."  
* Songs which are "outliers" (contain lots of non-standard chords and/or progressions) also exert a disproportionately large influence on the average.  
* Song-to-song variance is often not ruled out when discerning "effects" (differences between corpora).


My proposed solution was to calculate each song's own transitional probability table (negating the long-song effect), and use median values for the corpus's songs for each transition as the representative value for the corpus (minimizing the extra influence of outliers), and using confidence intervals to account for variance.

The consensus from the various discussions I've been in are that the problems I point out are legitimate, but some of the solutions I offer have problems. Most notably, the median has some mathematical/statistical drawbacks that are fatal, or nearly so, for these kinds of calculations.

One suggestion was to try using mean values, rather than median values. Another suggested a weighted mean. Still another suggested using the traditional method, but with a much larger corpus. These suggestions come from a music scholar that uses statistical methods frequently, a music scholar with a degree in statistics, and a physicist that uses these methods frequently (though not in that order). This lack of consensus needs addressing, I think, and I'm hoping a big, public, group discussion could help those of us doing corpus studies to reach more of a consensus about sound methods.

I'm hoping that this post, and the comment thread, can help get that big, public discussion going. So what do you think? Is current methodology just fine? Or should we calculate song-by-song and use a mean? Weighted mean? Median? Or should we stop looking for central values in a pre-defined corpus and instead use cluster analysis to find which songs/pieces belong together—in other words, asking which songs are alike, rather than what is alike about a group of songs?
