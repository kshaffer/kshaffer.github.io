---
author: KShaffer
comments: true
date: 2012-12-21 16:06:51
layout: post
slug: rock-corpus-comparison
title: Rock corpus comparison
wordpress_id: 637
tags:
- analysis
- corpus studies
- digital humanities
- music theory
- popular music
---

I've been periodically barking up the corpus study methodology tree. It is typical for a corpus analysis of harmonic structures to focus on one or both of two elements: _transitional probability_ and _n-gram analysis_. Transitional probability involves counting how frequently a two-chord progression (such as I–IV or V–VI) occurs in a piece, and comparing that frequency to other two-chord progressions that either start or end with the same chord. _N_-gram analysis entails finding and tallying all of the different kinds of three-chord, four-chord, _n_-chord progressions and comparing the relative frequency of those _n_-grams.

In most recent corpus studies on harmony, transitional probability is calculated by tallying up every instance of a progression type _in the entire corpus_ and dividing that tally by the total number of beginning or ending chords in the entire corpus. However, I've been working on an article on corpus-study methodology that finds fault with this method. 

There are two main problems with this corpus-wide-probability approach. First, the longest songs get the most weight over the final results, simply because there are more chord progressions in them. Second, statistical outliers (songs less representative of the whole) often exert greater influence over the corpus, particularly if a chord that appears seldom throughout the corpus appears frequently in a small number of songs. For instance, in a test corpus I've been playing around with, flat-VII appears only infrequently, but it is _very_ common in one song. 21 of the 25 songs in the test corpus do not contain flat-VII, and 24 of the 25 songs have two or less flat-VII chords in them. That means that the whole-corpus probability values related to the flat-VII chord are almost entirely determined by a single song—one which, by virtue of the preponderance of flat-VII chords, is _atypical_ of the collection, harmonically.

The standard method, then, can lead to some erroneous conclusions about the whole because of the characteristics of certain parts—long songs and statistical outliers, in these cases.

I've started comparing the results of the traditional whole-corpus tally method with a method that calculates probabilities for each song individually and then takes the median of those probabilities as the value for the corpus. This latter method ensures that long songs do not exert stronger influence on the corpus "average" simply because of their length, and that outliers exert _less_ influence on the overall result than the more typical songs.

One study that I've been able to run this comparison on is by Trevor deClercq and David Temperley (_Popular Music_ 2011): "A corpus analysis of rock harmony." They put their data and scripts [online](http://theory.esm.rochester.edu/rock_corpus/), so that others (like myself) can do these kinds of manipulations.

In their article, they tally the chord-to-chord transitions in a 100-song collection of rock songs. The transitional tallies are as follows (click to enlarge):

[![](/uploads/2012/12/Screen-Shot-2012-12-21-at-3.24.57-PM-300x168.png)](/uploads/2012/12/Screen-Shot-2012-12-21-at-3.24.57-PM.png)

However, when I calculated the same transitional values for each song individually and then took the median value for each transition type, I obtained the following transitional probability table (click to enlarge):

[![](/uploads/2012/12/Screen-Shot-2012-12-21-at-3.33.12-PM-300x135.png)](/uploads/2012/12/Screen-Shot-2012-12-21-at-3.33.12-PM.png)

The difference is incredible! Almost every median value is zero!

This is not the case for every corpus I've looked at. In fact, this is the most flat I've seen (though I've only looked at a few so far). I have to do some more study to discover the reasons behind all the zeroes, but I would hypothesize that the main reason is that their corpus is too diverse. It likely represents a number of highly idiosyncratic songs, or representatives from a number of different harmonic practices. (grammars? sub-grammars? dialects?)

Another tool I've been playing around with lately is cluster analysis, which may be able to pick this 100-song collection apart and find if, indeed, there are multiple harmonic practices at work. Once I've had a chance to do that analysis, I'll report back.

In the mean time, what do you all think about this difference?
