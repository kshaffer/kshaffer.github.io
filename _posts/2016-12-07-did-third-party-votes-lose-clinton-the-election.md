---
layout: post
title: "Did third-party votes lose Clinton the election?"
modified: 2016-12-07 16:22:00 -0500
image:
  feature: arrows.jpg
  teaser: arrows-teaser.jpg
  credit: W H
  creditlink: https://www.flickr.com/photos/wolfgangfoto/2496017650
share: true
categories: [data science, R]
short_description: "In which states did Jill Stein win more votes than the margin of victory? Could a swing in these states be enough to change the election results?"
---

<i>Official results are not yet in from every state, but we have good enough numbers to start to tackle some of the statistical questions surrounding last month's presidential election. <a href="https://en.wikipedia.org/wiki/United_States_presidential_election,_2016" target="_blank">Wikipedia has curated</a> the latest official and unofficial numbers from the <a href="https://interactives.ap.org/2016/general-election/?SITE=NEWSHOURELN" target="_blank">Associated Press</a> in a nice table, which I have cleaned up and assembled into an easy-to-wrangle (even in Excel!) <a href="https://github.com/kshaffer/election2016" target="_blank">dataset</a> for your analytical pleasures. <a href="https://en.wikipedia.org/wiki/Electoral_College_(United_States)" target="_blank">Electoral college</a> and <a href="https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population" target="_blank">population</a> data was also taken from Wikipedia.</i>


In the wake of Trump's victory last month, many liberal voters quickly pointed the finger at Jill Stein and third party voters for stealing the election from Clinton. This is understandable given how close the election was. But is it accurate? And does it apply to all of those who voted for a third-party candidate?

Let's see what the data has to say...


To determine if a third-party candidate played spoiler, we need to start by finding **in which states that candidate's votes exceed the winner's margin of victory.** I imported my <a href="https://github.com/kshaffer/election2016" target="_blank">2016 election results dataset</a> into <a href="https://www.r-project.org/" target="_blank">R</a> to do this analysis. Assuming the dataset is imported into a data frame called electionAnalysis (as it is in my <a href="https://github.com/kshaffer/election2016/blob/master/2016Election.R" target="_blank">sample R script</a>), a single line of code will tell you the states in which the amount of votes cast for third-party candidates exceeds the margin of victory for that state:

~~~R
electionAnalysis[electionAnalysis$thirdParty >
  electionAnalysis$marginOfVictory,]$state
~~~

This tells us that 14 states could conceivably have been swung by third-party voting: Arizona, Colorado, Florida, Maine, Michigan, Minnesota, Nevada, New Hampshire, New Mexico, North Carolina, Pennsylvania, Utah, Virginia, and Wisconsin.

However, the majority of third-party votes in this election went to right-leaning candidates. In fact, Gary Johnson himself brought in more than all other third-party candidates combined. So the real question is: **in which states did Jill Stein win more votes than the margin of victory?**

There were just four: Michigan, New Hampshire, Pennsylvania, and Wisconsin. Since New Hampshire went for Clinton, the question of Jill Stein spoiling the election for Clinton comes down to just three (now very familiar) states: **Michigan, Pennsylvania, and Wisconsin.**

Could a swing in these three states be enough to change the election results?

~~~R
sum(electionAnalysis[election$state %in%
  c('Michigan', 'Pennsylvania', 'Wisconsin'),]$electors2016)*2 >
  sum(electionAnalysis$trumpElectors) -
  sum(electionAnalysis$clintonElectors)
~~~

Yes, if Trump's 306 electors were diminished by the 46 electors from these three states, and Clinton's 232 increased by 46, the electoral votes would favor Clinton. So, it's hypothetically possible. But is it likely?

In Michigan, the margin of victory (based on current counts) is 10,704 votes in favor of Trump. Jill Stein's 51,463 could easily swing this. Let's assume that if Stein were off the ballot, all of her supporters would support Clinton. (This is a *big* if ― after all, if they voted third-party in a state this tight, it's unlikely that either Clinton or Trump was a close second choice. More likely, these were major protest votes from people who simply couldn't vote for the "lesser of two evils.") If Clinton took all of Stein's votes, what would happen to the other third-party votes? Johnson brought in 172,136 votes, and even McMullin brought in 8,177, almost enough to swing the state. If Stein were off the ballot, her supporters are more than numerous enough to win the election for Clinton, even if the majority of them stayed home. However, if there were *no* third-party candidates on the ballot, we cannot say with confidence how the state would have turned out. The right-leaning third-party candidates outnumbered her almost 4:1, and we don't know whom any of those voters would consider their second choice. So there's no way we can say with statistical confidence that removing third-party candidates would change Michigan's result. And without Michigan, Clinton couldn't win the electoral college.

Pennsylvania is the same story. Trump's margin of victory was just 44,121. Stein's share was only slightly larger at 49,941. And Johnson brought in 146,667. Almost every single Stein vote would have to go for Clinton, and then Johnson's supporters would have to split 50/50 (or lean Clinton) for Clinton to take Pennsylvania. Once again, we cannot say with statistical confidence that removing third-party candidates ― or even just Stein! ― would change the results. And like Michigan, Clinton would also need Pennsylvania to win the electoral college.

Likewise Wisconsin. Trump's margin of victory was 22,177. Stein's share was 31,006, and Johnson's 106,585. Taking Stein off the ballot *might* be enough to swing the state for Clinton, but we don't know for sure, and we cannot predict with confidence the effect of removing all third-party candidates from the ballot.

Clinton would have needed all three of these states to win the electoral college, but we can't even come close to predicting with confidence that removing third-party candidates from the ballot ― or even just removing Jill Stein from the ballot ― would send one of these states into Clinton's column, let alone all three.

Third-party voting may have swung the election for Trump. But for all we know, third-party candidates may have *lessened* Trump's victory. We can't make either claim with confidence based on the data. So please don't blame third-party voters, especially in the other 47 states, for losing Clinton the election and move on to more likely problems.

The electoral college and the nullifying of the Voting Rights Act come to mind...

*Header image by [W H](https://www.flickr.com/photos/wolfgangfoto/2496017650).*
