---
author: KShaffer
comments: true
date: 2012-07-27 13:02:05
layout: post
slug: averages-clusters-and-hidden-patterns
title: Averages, clusters, and hidden patterns
wordpress_id: 550
tags:
- analysis
- corpus studies
- digital humanities
- harmony
- music
- music theory
- popular music
---

*This is a revision of a previous post on averages and hidden patterns. I have replaced the ad hoc cluster analysis in that post with a standard cluster analysis based on k-means.*

Important information can be lost in averages. I've [written on this blog][CriterionRef] in the past about how using averages when calculating grades can hide important information about a student's performance. A student may have a passing average, but in a class that covers a number of different topics, a passing average may mask solid performance in some areas and serious failures in others. Likewise, when performing an analysis of a large set of works in a musical corpus, averages calculated from the whole corpus can mask significant differences within the corpus. This is the case for a test corpus I've been playing around with lately, and I think it is necessary for music scholars performing corpus analyses to explore this possibility and rule it out before taking averages as representative of an entire corpus.

In the process of developing [a Python module for corpus analysis][GithubModule] (found on [my new github site][GithubSite]—better documentation and a blog post or two coming soon), I used [a test corpus][GithubCorpus] of 25 Protestant worship songs. (This was a corpus I had laying around, so to speak, already encoded from a previous project. It includes the 25 most used non-public-domain songs in Protestant worship services in late 2011, counted by Christian Copyright Licensing International, CCLI. I will refer to it as the CCLI-2011 corpus.) This corpus exhibits a wide range of variance for most characteristics of harmonic progressions. That variance notwithstanding, I was able to use a standard statistical tool, confidence intervals, to find meaningful harmonic trends that supersede that variance. 

For instance, consider the transitional probabilities for the IV chord in this corpus. The median transitional probabilities for progression away from the IV chord are as follows: IV–I has a median probability of 0.64; IV–V 0.21; and all other transitions 0.00 (see Table 1). 

|   IV–I 	|  IV–II 	|  IV–III 	|  IV–IV 	|   IV–V 	|  IV–VI 	| IV–flat-VII 	|
| :-----: 	| :-----: 	| :-----: 	| :-----: 	| :-----: 	| :-----: 	| :-----: 	|
|   0.64 	|   0.00 	|   0.00 	|   0.00 	|   0.21 	|   0.00 	|   0.00 |

**Table 1.** Median transitional probabilities for progressions away from IV in the CCLI-2011 corpus.

Table 2 illustrates the 95%-confidence intervals for each transition. 

|     IV–I 	|     IV–II 	|    IV–III 	|    IV–IV 	|     IV–V 	|     IV–VI 	|    IV–flat-VII 	|
|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|
| 0.52 – 0.76 	| –0.02 – 0.02 	|     0.00 	| –0.02 – 0.02 	| 0.09 – 0.33 	| –0.03 – 0.03 	|     0.00 |

**Table 2.** 95%-confidence intervals for median transitional probabilities for progressions away from IV in the CCLI-2011 corpus.

**Figure 1.** Median transitional probabilities for progressions away from IV in CCLI-2011 corpus. Error bars show 95%-confidence intervals.  
![][TransProbIV]

With these confidence intervals in mind, we cannot conclude that IV progresses to I 64% of the time, but we can say with 95% confidence that the probability that IV progresses to I in the corpus is somewhere between 0.52 and 0.76. We can also say with 95% confidence that the probability that IV will progress to I is greater than the probability that IV will progress to V, and that both are greater than the probability that IV will progress anywhere else. (I will likely discuss variance and confidence intervals at greater length in a future post.)

The same kind of differentiation is not possible for progressions away from the V chord, however. Tables 3 and 4 show the median transitional probabilities and the confidence intervals for those medians for transitions away from the V chord.

|   V–I 	|  V–II 	|  V–III 	|  V–IV 	|   V–V 	|  V–VI 	| V–flat-VII 	
| :----: 	| :----: 	| :----: 	| :----: 	| :----: 	| :----: 	| :----: 	
|   0.25 	|  0.00 	|  0.00 	|  0.22 	|  0.00 	|  0.24 	|  0.00 

**Table 3.** Median transitional probabilities for progressions away from V in the CCLI-2011 corpus.

|      V–I 	|     V–II 	|    V–III 	|     V–IV 	|      V–V 	|     V–VI 	|    V–flat-VII 	
|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	
| 0.13 – 0.37 	| –0.06 – 0.06 	|     0.00 	|  0.11 – 0.33 	| –0.02 – 0.02 	|  0.12 – 0.36 	| –0.08 – 0.08 

**Table 4.** 95%-confidence intervals for median transitional probabilities for progressions away from V in the CCLI-2011 corpus.

**Figure 2.** Median transitional probabilities for progressions away from V in CCLI-2011 corpus. Error bars show 95%-confidence intervals.  
![][TransProbV]

Though the median transitional probability for V–I (0.25) is greater than that for V–IV (0.22), the variance among the songs is quite large, and the 95%-confidence intervals overlap substantially. Thus, we cannot say with 95% confidence that V is more or less likely to progress to I, IV, or VI. As far as we can tell from the data, they may be the same. It is a "statistical tie."

It can be tempting, then, to conclude that in this corpus, V chords are equally likely to progress to I, IV, or VI. However, that is not true on a song-by-song basis (see Table 5). There are multiple songs in the corpus where between 90% and 100% of the V chords all progress to the same chord (and for one of those songs, that chord is flat-VII, which had an average probability of 0.00 in the corpus). And few songs actually progress from V to I, IV, or VI an equal number of times. In other words, the average for the corpus doesn't represent the characteristics of any single song, and some are radically different from the average.

|                               Song 	| V-I 	| V-II 	| V-III 	| V-IV 	| V-V 	| V-VI 	| V-flat-VII 	|
| ---------------------------------: 	| :--: 	| :--: 	| :---: 	| :--: 	| :--: 	| :--: 	| :----: 	|
|               How Great Is Our God 	| 1.00 	| 0.00 	|  0.00 	| 0.00 	| 0.00 	| 0.00 	|  0.00 
|                     Mighty To Save 	| 0.24 	| 0.00 	|  0.00 	| 0.53 	| 0.00 	| 0.24 	|  0.00 
|                            Our God 	| 0.00 	| 0.00 	|  0.00 	| 0.00 	| 0.04 	| 0.96 	|  0.00 
|               Blessed Be Your Name 	| 0.00 	| 0.00 	|  0.00 	| 0.28 	| 0.00 	| 0.72 	|  0.00 
|               Here I Am To Worship 	| 0.56 	| 0.22 	|  0.00 	| 0.22 	| 0.00 	| 0.00 	|  0.00 
|                    Revelation Song 	| 0.00 	| 0.00 	|  0.00 	| 0.00 	| 0.00 	| 0.00 	|  1.00 
|                    Everlasting God 	| 0.50 	| 0.00 	|  0.00 	| 0.00 	| 0.00 	| 0.50 	|  0.00 
| Amazing Grace (My Chains Are Gone) 	| 1.00 	| 0.00 	|  0.00 	| 0.00 	| 0.00 	| 0.00 	|  0.00 
|                      Jesus Messiah 	| 0.47 	| 0.07 	|  0.00 	| 0.27 	| 0.20 	| 0.00 	|  0.00 
|               Your Grace Is Enough 	| 0.15 	| 0.00 	|  0.00 	| 0.30 	| 0.00 	| 0.55 	|  0.00 
|                            Forever 	| 0.00 	| 0.00 	|  0.00 	| 1.00 	| 0.00 	| 0.00 	|  0.00 
|          Open The Eyes Of My Heart 	| 0.40 	| 0.00 	|  0.00 	| 0.30 	| 0.10 	| 0.20 	|  0.00 
|                    In Christ Alone 	| 0.78 	| 0.11 	|  0.00 	| 0.11 	| 0.00 	| 0.00 	|  0.00 
|                   Holy Is The Lord 	| 0.44 	| 0.08 	|  0.00 	| 0.00 	| 0.00 	| 0.40 	|  0.08 
|                  Shout To The Lord 	| 0.46 	| 0.00 	|  0.00 	| 0.15 	| 0.00 	| 0.38 	|  0.00 
|                       How He Loves 	| 0.00 	| 0.00 	|  0.00 	| 1.00 	| 0.00 	| 0.00 	|  0.00 
|                    You Are My King 	| 0.75 	| 0.00 	|  0.00 	| 0.25 	| 0.00 	| 0.00 	|  0.00 
|    Come Now Is The Time To Worship 	| 0.25 	| 0.75 	|  0.00 	| 0.00 	| 0.00 	| 0.00 	|  0.00 
|                From The Inside Out 	| 0.08 	| 0.10 	|  0.00 	| 0.50 	| 0.00 	| 0.33 	|  0.00 
|                            Hosanna 	| 0.44 	| 0.00 	|  0.00 	| 0.04 	| 0.00 	| 0.52 	|  0.00 
|               Glory To God Forever 	| 0.17 	| 0.00 	|  0.00 	| 0.42 	| 0.00 	| 0.42 	|  0.00 
|      Lord I Lift Your Name On High 	| 0.25 	| 0.00 	|  0.00 	| 0.63 	| 0.00 	| 0.13 	|  0.00 
|         Hosanna (Praise Is Rising) 	| 0.14 	| 0.00 	|  0.00 	| 0.38 	| 0.00 	| 0.48 	|  0.00 
|                          The Stand 	| 0.00 	| 0.00 	|  0.00 	| 0.09 	| 0.00 	| 0.91 	|  0.00 
|                       We Fall Down 	| 0.40 	| 0.00 	|  0.00 	| 0.20 	| 0.00 	| 0.40 	|  0.00 

**Table 5.** Transitional probabilities for progressions away from V in each song of the CCLI-2011 corpus.

How, then, do we perform a meaningful analysis of this corpus if averages do not reflect the structures of the individual songs? One way is simply to perform a detailed analysis of each individual song (like I did in [my previous post][JumpLittleChildrenPost] on "Mexico" by Jump, Little Children). But this is not the only option.

Another option is *cluster analysis*, a process by which an analyst mines a corpus for smaller collections within it that exhibit similar properties within those collections. There are a number of ways to perform a cluster analysis, and a proper introduction to cluster analysis could form an entire article in itself. So in this post, I will simply demonstrate the results obtained from one particular method and the implications for analyses of musical corpora.

To divide the CCLI-2011 corpus into sub-corpora, I used the *k-means* clustering algorithm in the software [Cluster 3.0][ClusterApp] (originally developed by Michael Eisen for genetic analysis). In a nutshell, k-means analysis treats each record (in this case, the transitional probability table for each song) as a vector in Euclidean space (each transition type is its own dimension), and tries to find the arrangement of vectors into clusters that produces the least variance within clusters. Cluster 3.0 prompts the user for the total number of clusters and the number of random clustering attempts and returns the clustering arrangement with the tightest clusters—the least variance around the mean vector for each cluster.

For the CCLI-2011 corpus, I directed it to form five clusters and make 10,000 attempts. The result assigned the 25 songs into the following five clusters:

| Song 	| Cluster 	|
| ---: 	| :------ 	|
| Here I Am To Worship 	| 0 
| Jesus Messiah 	| 0 
| Your Grace Is Enough 	| 0 
| We Fall Down 	| 0 
| Revelation Song 	| 1 
| Mighty To Save 	| 2 
| Our God 	| 2 
| Blessed Be Your Name 	| 2 
| From The Inside Out 	| 2 
| Glory To God Forever 	| 2 
| Hosanna (Praise Is Rising) 	| 2 
| The Stand 	| 2 
| How Great Is Our God 	| 3 
| Everlasting God 	| 3 
| Open The Eyes Of My Heart 	| 3 
| Holy Is The Lord 	| 3 
| Shout To The Lord 	| 3 
| You Are My King 	| 3 
| Come, Now Is The Time To Worship 	| 3 
| Hosanna 	| 3 
| Amazing Grace (My Chains Are Gone) 	| 4 
| Forever 	| 4 
| In Christ Alone 	| 4 
| How He Loves 	| 4 
| Lord I Lift Your Name On High 	| 4 

**Table 6.** Five clusters in the CCLI-2011 corpus, based on Euclidean distance and calculated by Michael Eisen's Cluster 3.0 software.

One interesting thing to note from this clustering arrangement is that "Revelation Song," the nearly sole source of flat-VII chords, forms its own cluster. It is the most unique song in the corpus based on its harmonic transitional probability. However, the most important result of this cluster analysis is the differences between each cluster's median transitional probabilities.

| 	|   I 	|  II 	|  III 	|  IV 	|   V 	|  VI 	| flat-VII 	|
| ----: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	|
|     I 	|  0.00 	|  0.00 	|  0.00 	|  0.35 	|  0.33 	|  0.00 	|  0.00 
|    II 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|   III 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|    IV 	|  0.64 	|  0.00 	|  0.00 	|  0.00 	|  0.21 	|  0.00 	|  0.00 
|     V 	|  0.25 	|  0.00 	|  0.00 	|  0.22 	|  0.00 	|  0.24 	|  0.00 
|    VI 	|  0.00 	|  0.00 	|  0.00 	|  0.53 	|  0.00 	|  0.00 	|  0.00 
| flat-VII 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 

**Table 7.** Median transitional probabilities for the entire CCLI-2011 corpus.

| 	|   I 	|  II 	|  III 	|  IV 	|   V 	|  VI 	| flat-VII 	|
| ----: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	|
|     I 	|  0.00 	|  0.09 	|  0.00 	|  0.45 	|  0.37 	|  0.00 	|  0.00 
|    II 	|  1.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|   III 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|    IV 	|  0.65 	|  0.05 	|  0.00 	|  0.00 	|  0.19 	|  0.00 	|  0.00 
|     V 	|  0.43 	|  0.03 	|  0.00 	|  0.24 	|  0.00 	|  0.20 	|  0.00 
|    VI 	|  0.00 	|  0.00 	|  0.00 	|  0.27 	|  0.10 	|  0.00 	|  0.00 
| flat-VII 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 

**Table 8.** Median transitional probabilities for Cluster 0 of CCLI-2011 corpus.

| 	|   I 	|  II 	|  III 	|  IV 	|   V 	|  VI 	| flat-VII 	|
| ----: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	|
|     I 	|  0.00 	|  0.00 	|  0.00 	|  0.10 	|  0.76 	|  0.14 	|  0.00 
|    II 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|   III 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|    IV 	|  0.97 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|     V 	|  0.08 	|  0.00 	|  0.00 	|  0.38 	|  0.00 	|  0.48 	|  0.00 
|    VI 	|  0.00 	|  0.00 	|  0.00 	|  0.88 	|  0.00 	|  0.00 	|  0.00 
| flat-VII 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 

**Table 9.** Median transitional probabilities for Cluster 2 of CCLI-2011 corpus.

| 	|   I 	|  II 	|  III 	|  IV 	|   V 	|  VI 	| flat-VII 	|
| ----: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	|
|     I 	|  0.11 	|  0.00 	|  0.00 	|  0.49 	|  0.16 	|  0.00 	|  0.00 
|    II 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|   III 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|    IV 	|  0.32 	|  0.00 	|  0.00 	|  0.00 	|  0.68 	|  0.00 	|  0.00 
|     V 	|  0.45 	|  0.00 	|  0.00 	|  0.02 	|  0.00 	|  0.29 	|  0.00 
|    VI 	|  0.00 	|  0.00 	|  0.00 	|  0.56 	|  0.00 	|  0.00 	|  0.00 
| flat-VII 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 

**Table 10.** Median transitional probabilities for Cluster 3 of CCLI-2011 corpus.

| 	|   I 	|  II 	|  III 	|  IV 	|   V 	|  VI 	| flat-VII 	|
| ----: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	| :---: 	|
|     I 	|  0.00 	|  0.08 	|  0.00 	|  0.66 	|  0.14 	|  0.00 	|  0.00 
|    II 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  1.00 	|  0.00 	|  0.00 
|   III 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 
|    IV 	|  0.64 	|  0.00 	|  0.00 	|  0.00 	|  0.27 	|  0.00 	|  0.00 
|     V 	|  0.25 	|  0.00 	|  0.00 	|  0.63 	|  0.00 	|  0.00 	|  0.00 
|    VI 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  1.00 	|  0.00 	|  0.00 
| flat-VII 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 	|  0.00 

**Table 11.** Median transitional probabilities for Cluster 4 of CCLI-2011 corpus.

There are some substantial differences between these five clusters (or four clusters and "Revelation Song"), and between the individual clusters and the whole-corpus averages. Consider the V chord, discussed above. In the whole corpus, it is equally probable that it will progress to I, IV, or VI (see Table 4 and Figure 2 above). In Cluster 0 (Table 12 and Figure 3), there is a similar tendency, but wider variance; in other words, the behavior of V in this cluster is less regular. In Cluster 2 (Table 13 and Figure 4), V progresses equally to IV and VI, less often to I, and not at all to other chord roots. In Cluster 3 (Table 14 and Figure 5), V progresses most often to I and VI, with all other roots overlapping with zero probability. And in Cluster 4 (Table 15 and Figure 6), we can only say with confidence that V progresses with any consistency to IV (though V–I overlaps both V–IV and zero probability).

|      V–I 	|     V–II 	|    V–III 	|     V–IV 	|      V–V 	|     V–VI 	|    V–flat-VII 	|
|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|
| 0.24 – 0.60 	| –0.07 – 0.13 	|     0.00 	|  0.20 – 0.28 	| –0.10 – 0.10 	| –0.08 – 0.48 	|     0.00 

**Table 12.** 95%-confidence intervals for median transitional probabilities for progressions away from V in the CCLI-2011 corpus, Cluster 0.

|      V–I 	|     V–II 	|    V–III 	|     V–IV 	|      V–V 	|     V–VI 	|    V–flat-VII 	|
|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|
| 0.01 – 0.15 	| –0.03 – 0.03 	|     0.00 	|  0.23 – 0.53 	| –0.01 – 0.01 	|  0.27 – 0.69 	|     0.00 

**Table 13.** 95%-confidence intervals for median transitional probabilities for progressions away from V in the CCLI-2011 corpus, Cluster 2.

|      V–I 	|     V–II 	|    V–III 	|     V–IV 	|      V–V 	|     V–VI 	|    V–flat-VII 	|
|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|
| 0.29 – 0.61 	| –0.18 – 0.18 	|     0.00 	| –0.07 – 0.11 	| –0.02 – 0.02 	|  0.13 – 0.45 	| –0.02 – 0.02 

**Table 14.** 95%-confidence intervals for median transitional probabilities for progressions away from V in the CCLI-2011 corpus, Cluster 3.

|      V–I 	|     V–II 	|    V–III 	|     V–IV 	|      V–V 	|     V–VI 	|    V–flat-VII 	|
|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|  :--------: 	|
| –0.15 – 0.65 	| –0.04 – 0.04 	|     0.00 	|  0.21 – 1.05 	|     0.00 	| –0.05 – 0.05 	|     0.00 

**Table 15.** 95%-confidence intervals for median transitional probabilities for progressions away from V in the CCLI-2011 corpus, Cluster 4.

**Figure 3.** Median transitional probabilities for progressions away from V in CCLI-2011 corpus, Cluster 0. Error bars show 95%-confidence intervals.  
![][TransProbV-cluster0]

**Figure 4.** Median transitional probabilities for progressions away from V in CCLI-2011 corpus, Cluster 2. Error bars show 95%-confidence intervals.  
![][TransProbV-cluster2]

**Figure 5.** Median transitional probabilities for progressions away from V in CCLI-2011 corpus, Cluster 3. Error bars show 95%-confidence intervals.  
![][TransProbV-cluster3]

**Figure 6.** Median transitional probabilities for progressions away from V in CCLI-2011 corpus, Cluster 4. Error bars show 95%-confidence intervals.  
![][TransProbV-cluster4]

Only one of these clusters (Cluster 0) has a transitional probability for the V chord that resembles that of the entire corpus, and all of them differ from each other. Thus, the averages for the 25-song corpus do not represent a single grammar that exhibits some variance from song to song. Rather, those averages represent a composite of *several different grammars*, which also exhibit variance from song to song.

The idea of multiple grammars being present within a corpus is not at all surprising. Consider, for instance, the difference between blues-based and non-blues-based songs in early rock-and-roll. The blues-based songs follow a distinct pattern of harmonic progression that dominates a significant portion of rock songs in the 1950s and 1960s. However, those harmonic patterns are not a given in non-blues-based songs (especially those songs by musicians like Perry Como and Pat Boone that occupy positions in the Billboard charts right along side Elvis Presley but are not influenced by Presley's blues-heavy sound). However, corpus analysts are usually satisfied to decide which songs do and do not belong to the grammar *before* the analysis, and then taking the averages as representative of the whole corpus. Instead, cluster analysis (whether formally or informally performed) can help determine which songs belong together *after* the analysis is performed, identifying multiple grammars and sub-corpora within a broader collection. And as [a recent study by Joshua Albrecht][Albrecht] demonstrates, cluster analysis can be a helpful tool to identify trends and changes throughout a historical time period. Such an analysis is be much more insightful—and interesting—than calculating static averages for a large corpus.

[TransProbIV]: /media/clusterAnalysisPostGraphics/transProbIV.png
[TransProbV]: /media/clusterAnalysisPostGraphics/transProbV.png
[TransProbV-cluster0]: /media/clusterAnalysisPostGraphics/transProbV-cluster0.png
[TransProbV-cluster2]: /media/clusterAnalysisPostGraphics/transProbV-cluster2.png
[TransProbV-cluster3]: /media/clusterAnalysisPostGraphics/transProbV-cluster3.png
[TransProbV-cluster4]: /media/clusterAnalysisPostGraphics/transProbV-cluster4.png
[Albrecht]: http://musiccog.ohio-state.edu/home/data/_uploaded/pdf/On%20the%20emergence%20of%20the%20major-minor%20system.pdf
[JumpLittleChildrenPost]: /2012/06/problems-with-using-transitional-probability-in-musical-corpus-studies/
[CriterionRef]: /tags/criterion-referenced-grading/
[GithubModule]: https://github.com/kshaffer/corpusAnalysis
[GithubSite]: https://github.com/kshaffer
[GithubCorpus]: https://github.com/kshaffer/CCLI-2011
[ClusterApp]: http://bonsai.hgc.jp/~mdehoon/software/cluster/software.htm#ctv