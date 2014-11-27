---
author: KShaffer
comments: true
date: 2012-06-15 11:06:05
layout: post
slug: problems-with-using-transitional-probability-in-musical-corpus-studies
title: Problems with using transitional probability in musical corpus studies
categories: blog
share: true
wordpress_id: 452
tags:
- analysis
- corpus studies
- digital humanities
- harmony
- music theory
- pop/rock music
- probability
---

Corpus studies are all the rage in music theory these days. This is particularly true in the study of harmonic syntax—the rules according to which chords are put into chord progressions. Corpus studies in harmony typically involve at least one of two modes of analysis:

- Transitional probability—that is, counting how frequently a two-chord progression (such as I–IV) occurs in a song, and comparing that frequency to other two-chord progressions that either start or end with the same chord.

- *N*-grams—that is, finding all of the different kinds of three-chord, four-chord, *n*-chord progressions, tallying them up, and comparing the relative frequency of those *n*-grams.

Such analysis is easy to conduct computationally on large corpora of songs. However, while these two modes of analysis can at times provide us with helpful information, they both miss something critical: the way chord progressions relate to formal structure.

In what follows, I will present the song, "Mexico," by Jump, Little Children as a case study. It is a prime example of how relying on transitional probability or *n*-gram analysis not only provides an incomplete picture of the harmonic structures of a song, but can at times provide an inaccurate picture of the harmonic structures of a song. And when our understanding of the harmonic structures of a whole genre depend on a corpus study that simply performs this type of analysis on a large swath of songs, our understanding of harmony in that genre may be seriously flawed.

## The "sensitive female" chord progression

In "Mexico," Jump, Little Children incorporate a supple, versatile chord progression cycle that has come to be called the "Sensitive Female Chord Progression." (The name came about because the chord progression came to prominence in the 1990s with a number of very successful songs by female singer/songwriters like Joan Osborne, Jewel, and Sarah McLachlan.) The SFCP is a four-chord, cyclical progression. And like some, but not all, cyclical progressions, it can be found in multiple rotations. The definitive rotation begins each four-chord (usually two-bar) unit with VI.

> &#124;&#124;: VI IV I V :&#124;&#124;

It also commonly appears in a rotation that is offset two chords from the definitive version:

> &#124;&#124;: I V VI IV :&#124;&#124;

"With or Without You" by U2 and "Hide and Seek" by Imogen Heap are prime examples of this rotation.

Though there are two other possible rotations, only one other appears with any frequency in pop music:

> &#124;&#124;: IV I V VI :&#124;&#124;

This is far less common than the other two, but it does feature prominently in "Mexico."

## "Mexico," by Jump, Little Children

<iframe width="480" height="360" src="http://www.youtube.com/embed/jo-Yw-7C95E?rel=0" frameborder="0" allowfullscreen></iframe>

The specific uses of the SFCP in different ways at different points in the form of "Mexico" demonstrate the woeful inadequacy of harmonic analysis methods that only account for transitional probability and *n*-gram tallies.

Here is a chordal analysis of "Mexico," divided by formal section. Four-chord (and occasionally three-chord) units—two-bar subphrases—are marked off by a single vertical line. Four-bar phrases are marked off by two vertical lines.

> Intro (I):  
I IV I V &#124; I IV I V &#124;&#124;

> Strophe (A1):  
I IV I V &#124; VI IV I V &#124;&#124; I IV I V &#124; VI IV I V &#124;&#124; IV I V VI &#124; IV I V &#124;&#124;

> Janus (Jay Summach's term for an intro with overlap from previous strophe):  
I IV I V &#124; I IV I V &#124;&#124;

> Strophe (A2):  
I IV I V &#124; VI IV I V &#124;&#124; I IV I V &#124; VI IV I V &#124;&#124; IV I V VI &#124; IV I V &#124;&#124;

> Janus (J):  
I IV I V &#124;

> Bridge (B):  
IV – I V &#124; VI IV I V &#124;&#124; IV – I V &#124;

> Janus (J):  
I IV I V &#124;

> Strophe (A3):  
I IV I V &#124; VI IV I V &#124;&#124; IV I V VI &#124; IV I V &#124;&#124;

> Janus (J):  
I IV I V &#124;

> Bridge (B):  
IV – I V &#124; VI IV I V &#124;&#124; IV – I V &#124;

> Strophe (Ai, instrumental):  
I IV I V &#124; VI IV I V &#124;&#124; IV I V VI &#124; IV I V &#124;&#124;

> Bridge (B):  
IV – I V &#124; VI IV I V &#124;&#124; IV – I V &#124;

> Strophe (A4):  
IV I V VI &#124; IV I V VI &#124; IV I V – &#124;&#124;

> Outro (O):  
I IV I V &#124; I – – – &#124;&#124;

## Transitional probability analysis

Following is a tally of chord transitions. Each number represents the total number of progressions from a chord on the left to a chord on the top.

| 	|  I 	| IV 	|  V 	| VI 	|
|:-:|:-:|:-:|:-:|
|  I 	| —	| 14 	| 40 	| —
| IV 	| 40 	| —	| —	| —
|  V 	| 14 	| 11 	| —	| 15 
| VI 	| —	| 15 	| —	| —
{: rules="groups"}

**Table 1.** Total number of progressions from chord in left-side column to chord in top row in "Mexico," by Jump Little Children.

According to a transitional probability analysis of this song, we would say that IV always goes to I, VI always goes to IV, I usually goes to V, and V has quite a bit of freedom, only minimally preferring to go to VI over I. Likewise, we would say that V always comes from I, VI always comes from V, I usually comes from IV (sometimes V), and IV comes from pretty much anywhere, with a slight preference for VI over I. In all cases, the preferred progressions are those found in the "sensitive female" progression: I–V, V–VI, VI–IV, and IV–I.

An *n*-gram analysis shows that 64 of the 137 4-grams (four-chord progressions) in the song are "sensitive female" progressions in some rotation: 47%.

However, this is far from a complete understanding of harmony in this song.

Take the V chord, for example. According to the transitional probability analysis, the V chord has quite a bit of freedom. While the other three chords are significantly, if not absolutely, constrained to progress according to the norms of the "sensitive female" progression types, the V chord seems immune to those constraints. It progresses to I almost as often as it goes to VI, and it progresses to IV a fair number of times, as well. However, many instances of the V chord are what music theorists call *back-relating dominants*—that is, chords that end phrases or larger formal units and function as points of *arrival*. These chords, we tell our harmony students, do not relate to the chord that follows but to the chords that came before. The *cadence* (or point of arrival) sets expectation for what might happen at the end of the subsequent formal unit, but the following chord is a new beginning and can start on any chord that works as a beginning to that new unit, *even if the progression from the cadential V to the subsequent chord starting the new phrase violates grammatical rules or stylistic norms for good chord progressions*. Such a theoretical principle would imply that a study of harmony in a corpus would ignore chord progressions across phrase boundaries, since those progressions involve back-relating chords and are exempt from the grammar being studied.

Interestingly, in this song *every single V–IV progression is across a phrase boundary*. That is, the V chord is an arrival, and the IV chord a new beginning, either of a phrase or of a "module" (Jay Summach's term for formal units on the level of strophe, bridge, verse, chorus, etc.). Likewise, 11 out of 14 V–I progressions cut across phrase or module boundaries. That means that only 3 V chords progress to something other than VI within the phrase.

Now, let's ignore the rule about back-relating dominants for the moment. I can picture a music theorist (and I have a specific one in mind) saying that the rule about back-relating dominants isn't real; it's just a cheap way to tell our students how to write grammatical music, or a leftover from Schenkerian theory (if you don't know what that is, don't worry!), and it isn't necessary if we have a robust enough theory of harmonic progression. Fair enough. However, even if we count chord progressions that cut across formal boundaries, this song demonstrates some significant differences in the way chords progress in different parts of the form.

Again, take the V chord. On the whole, it looks like the V chord progresses in relative freedom, judging by the small differences in transitional probability for progressions to I, IV, or VI (35%, 28%, and 38%, respectively). However, consider how it behaves in different formal units.

| 	|  I 	| IV 	| VI 	|
|:-:|:-:|:-:|:-:|
| I/J/O 	|  6 	|  2 	| —
|   A 	|  6 	|  5 	| 12 
|   B 	|  2 	|  4 	|  3 
{: rules="groups"}

**Table 2.** Total number of progressions from V to the chord in the top row in the formal modules given in the left column.

In what Summach calls "auxiliary modules" (intros, outros, codas, and "Janus" modules), the V chord overwhelmingly goes to I. In strophes, V goes to VI the majority of the time. And in bridges, though it is relatively even, V–IV is privileged. Thus, V has a different privileged place to go in each type of formal unit.

Now consider the tallies obtained when we leave out progressions that cross module boundaries (the last chord of a strophe to the first chord of the following bridge, for example).

| 	|  I 	| IV 	| VI 	|
|:-:|:-:|:-:|:-:|
| I/J/O 	|  4 	| —	| —
|   A 	|  2 	|  4 	| 12 
|   B 	| —	|  3 	|  3 
{: rules="groups"}

**Table 3.** Total number of progressions from V to the chord in the top row in the formal modules given in the left column, progressions across module boundaries omitted.

Now the preference for V–I in the auxiliary modules and V–VI in the strophes are even more pronounced, with V progressing evenly to IV and VI in bridges.

## Summary

Transitional probability and *n*-gram analysis can provide helpful information about the harmonic structure of a piece of music. It can do so with great ease, as well, when using computational tools. However, therein lies the temptation. Stopping with the easy—or more accurately, using easy tools so we can apply them to a lot more music at once—misses something important. In "Mexico," by Jump, Little Children, transitional probability and 4-gram analysis both tell us that this song is dominated by chord progressions characteristic of the "sensitive female" progression cycle. However, both types of analysis fail to account for some important characteristics of the harmonic structure of this song. In particular, a transitional probability analysis would lead us to the conclusion that the V chord exhibits great freedom relative to the other chords, which are significantly constrained in where they progress. However, a more detailed analysis shows that in this song, the V chord is highly constrained in its motion *within each module type*. The perception of freedom comes from an unfair averaging of these different constraints over the whole song. Further, the V chord's common role as a phrase- or module-ending chord, combined with the diversity of places in which phrases and modules begin harmonically, add to the false sense of "freedom" for the V chord. Rather than being "free," the V chord obeys a fairly strict grammar that is tied to the form of the song.

Speaking generally, harmony and form are inextricably linked. Neither can be wholly accounted for without the other. While transitional probability and related analytical tools can assist us in some measure in our endeavor to comprehend the harmonic grammar of different musical styles, any analysis that does not account for the relationship of harmonic progression to formal structure is likely to produce an incomplete if not an incorrect understanding of that harmonic grammar.