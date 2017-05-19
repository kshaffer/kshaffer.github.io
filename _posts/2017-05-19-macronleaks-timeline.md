---
layout: post
title: "#MacronLeaks - how disinformation spreads"
modified: 2017-05-19 10:54:16 -0400
image:
  feature: disinfo.jpg
  teaser: disinfo-teaser.jpg
share: true
categories: [data science, propagandalytics]
---

A lot happened online on May 5, 2017. Ben Starling, CE Carey, and I found evidence of <a href="https://medium.com/data-for-democracy/democracy-hacked-a46c04d9e6d1" target="blank_">a massive disinformation campaign taking place on Twitter and 4chan</a>, in an attempt to swing the French presidential election in favor of Marine Le Pen. As we were putting the finishing touches on our article about this campaign, we saw <a href="https://twitter.com/wikileaks/status/860577607670276096" target="blank_">the tweet from WikiLeaks</a>, announcing that a 9GB dump of documents from the Macron campaign (dubbed #MacronLeaks) had been posted online. Then the Macron campaign confirmed that they had been the target of hackers, <a href="http://www.reuters.com/article/us-france-election-macron-leaks-idUSKBN1812AZ?utm_source=twitter&amp;utm_medium=Social" target="blank_">possibly with Russian connections</a>.

We continued to collect tweets related to the French election until two days after the election, in addition to ongoing monitoring of content on 4chan's *politically incorrect* board ― known simply as /pol/. In the aftermath of the election, we analyzed how the #MacronLeaks news spread through 4chan and Twitter. What we found was a pattern that keeps arising in our (and others') study of the spread of disinformation online:

> An anonymous user dumps information on 4chan, and then a small number of "catalyst" accounts bring the disinformation to a more mainstream platform like Twitter, where an army of bots, sockpuppets, "$hitposters", and unsuspecting individuals amplify the signal until it "trends" and a celebrity account brings it to the attention of mainstream media.

**It's this combination of what we're calling *catalyst* accounts and the army of *signal boosters* ― a number of which are bots and botnets ― that allows the disinformation to spread quickly and reach the mainstream.**

## #MacronLeaks timeline

Here is a <a href="https://timeline.knightlab.com/" target="blank_">timeline</a> of how the MacronLeaks campaign progressed, beginning with early signs that a data dump might be coming, through the Macron campaign's announcement confirming a hack.

<iframe src='https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=16WSJUwmVstsjH6R6l1mdext1P9vnXeHu-J88fCWeONs&font=Default&lang=en&initial_zoom=2&height=650' width='150%' height='650' style="margin-left: -25%" webkitallowfullscreen mozallowfullscreen allowfullscreen frameborder='0'></iframe>

There are a few key takeaways from this timeline:

<ul><li>Disobedient Media is a source worth a closer investigation. Not only were they a major early source of information about the leak, but they tweeted that it might be coming before the leak was posted to pastebin.com. <br></li><li>This is not the first time that a false leak has been posted to 4chan before more mainstream (social) media. In previous (unpublished) research, we found the #SyriaHoax campaign also got an early start there before moving to Twitter. <a href="https://twitter.com/JackPosobiec/status/860567142965575681" target="blank_">Jack Posobiec claims</a> that 4chan's /pol/ is "the new Wikileaks". But so far, it seems to be the place to dump <i>false</i> information that someone wants to spread <i>quickly</i> ― likely to have a maximum impact before people have a chance to verify its veracity and authenticity. This is worth keeping in mind for future campaigns.</li><li><a href="https://twitter.com/JackPosobiec/" target="blank_">Jack Posobiec</a> and <a href="https://twitter.com/BasedMonitored" target="blank_">Based Monitored</a> were important links from 4chan to the Twitter community.</li><li>While Jack Posobiec linked to 4chan's thread, Based Monitored linked directly to the leak. This skirting of 4chan may have led to Based Monitored being the most-retweeted account before WikiLeaks?</li><li>It wasn't until WikiLeaks tweeted a link that knowledge of the leak came into the mainstream. Even though Wikileaks claimed it may have been a "<a href="https://twitter.com/wikileaks/status/860577607670276096" target="blank_">4chan practical joke</a>", they brought significant visibility to the leak and were instrumental in its achieving mainstream status.</li></ul>

I think it's also important to note the absence of some more well known players in this narrative: Breitbart, InfoWars, Fox News, ... none of the established media sources on the far-right or center-right played a role in this, including those known for fake-news conspiracy theories. Whoever was behind this disinformation campaign knew how to get the message front-and-center quickly, at a crucial time ― just a few hours before the campaign news blackout in France. 

And while the campaign was not successful in swinging the election in favor of Le Pen, it was absolutely successful in terms of controlling the mainstream media narrative at the most pivotal moment of media attention in advance of the election. They had the last word. And *if* (and that's a big if right now) the architect of this campaign is the same as the one behind #MacronGate, they were also successful in <a href="http://www.telegraph.co.uk/news/2017/05/04/emmanuel-macron-files-defamation-complaint-marine-le-pen-offshore/" target="blank_">shifting the focus of the last French presidential debate</a>. If it's not perpetrated by the same actor(s), then the #MacronLeaks campaign certainly capitalized on the success of #MacronGate, and was likely aided by its priming of media attention.

We're seeing disinformation campaign tactics evolve quickly, but one key trend seems to recur: **use catalysts and amplifiers to bring propaganda to the attention of the public at large, with the goal of getting a major influencer *outside your community* to boost it into mainstream media or campaign activities.** This time that was Wikileaks, in the past it's been <a href="http://www.politico.com/magazine/story/2017/03/memes-4chan-trump-supporters-trolls-internet-214856" target="blank_">the Trump campaign itself</a>.

The UK election is coming soon, as is Germany. We'll keep studying these campaigns, along with our <a href="http://datafordemocracy.org/" target="blank_">Data for Democracy</a> colleagues, and we'll keep you posted.