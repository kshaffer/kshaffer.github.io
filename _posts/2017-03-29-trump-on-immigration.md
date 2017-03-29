---
layout: post
title: "Trump on immigration"
modified: 2017-03-29 12:12:00 -0500
image:
  feature: policeLine.jpeg
  teaser: policeLine-teaser.jpeg
  credit:
  creditlink:
share: true
categories: [data science, propagandalytics]
short_description: "Donald Trump talks about immigration in some uniquely horrifying ways."
---

Donald Trump talks about immigration in some uniquely horrifying ways. We're all familiar with his "not sending us their best people" speech from early in his campaign. But how has his language developed over time? And when looking specifically at *official White House materials*, how extreme is his rhetoric?

Following the same methods as <a href="/2017/03/trumping-science/" target="blank_">my earlier post analyzing the Trump administrations language about science and the environment</a>, I analyzed the full text of whitehouse.gov (downloaded on March 1) and compared its language about immigration with the Obama administration's site (as of the morning of January 20). Here's how they compare.

The data
I already had both websites parsed by *bigram* (two-word phrases) with stop words ("a", "an", "the", "of", etc.) removed. To find language about immigration, I searched that parsed archive for bigrams containing the text "migra". This will extract any phrases containing the words "immigration", "immigrant", "immigrants", as well as "migrant" and "migration", verbs like "immigrate" and "migrate", and Spanish-language text like "immigracion".

This search for "migra" returns **624 bigrams on Trump's website** and **12,370 bigrams on Obama's website.** Obama's website is about three times the size of Trump's March 1 site, and yet mentions immigration about 20 times more often than Trump's site.

Here are the ten most frequent immigration bigrams on Obama's site:

| bigram | count |
| --: | :-- |
| immigration action | 5009 |
| deal immigration | 4956 |
| immigration reform | 222 |
| immigration system | 192 |
| security immigration | 191 |
| immigration poverty | 90 |
| broken immigration | 82 |
| care immigration | 72 |
| comprehensive immigration | 60 |
| immigration refinancing | 50 |

A full 80% of the bigrams on immigration on Obama's site are comprised of just two phrases: "immigration action" and "deal immigration". It turns out that these come from a common header on a number of pages on the website, containing links to a page about the "Iran Deal" and "Immigration Action". Skipping those headers brings the Obama-Trump proportion of immigration mentions far closer to the expected 3-to-1, and then the rest of this list confirms what many of us already knew: the Obama administration was concerned about current immigration policy in the US, and they desired to "reform" the current, "broken" immigration system.

Here are the top ten bigrams on Trump's website relating to immigration:

| bigram | count |
| --: | :-- |
| immigration laws | 76 |
| illegal immigration | 37 |
| immigration enforcement | 37 |
| federal immigration | 35 |
| illegal immigrants | 29 |
| immigration law | 23 |
| illegal immigrant | 19 |
| immigration system | 18 |
| immigration reform | 16 |
| undocumented immigrants | 16 |

While the idea of reforming a broken system can also be seen on Trump's site, there seems to be a greater focus on the (negatively judged) status of individual immigrants ― illegal, undocumented ― as well as the enforcement of immigration laws ― think ICE raids, Customs and Border Patrol actions at international airports, travel bans, etc.

Comparing top-10 lists can provide interesting results, but there are statistical measures that can provide a more robust sense of what the most distinctive language of each administration is. Following the procedure described in the previous blog post in this series, here are the most distinctive bigrams containing "migra" in the Trump and Obama administrations' websites, calculated by a <a href="https://en.wikipedia.org/wiki/Odds_ratio" target="blank_">log odds ratio</a>, with phrases removed that were typically (or exclusively) the results of page headers ("immigration iran" was the result of a link for "immigration" preceding one for "Iran deal", similarly for "immigration rural", "immigration climate", "care immigration", and several others).

<a href="/assets/images/migra_Mar1.png" target="blank_"><img src="/assets/images/migra_Mar1.png" alt="Log odds ratio: most distinctive two-word phrases containing 'migra' in Trump and Obama administration websites" /></a>

Comparing the most distinctive immigration-related phrases on these two websites reveals several important trends. First, **the Trump administration is more heavily focused on the enactment and enforcement of immigration law** ― in other words, keeping (and kicking) immigrants out. Second, **the Trump administration is more likely to label immigrants as illegal.** On the other side, we see that **the Obama administration is more focused on speaking to immigrants,** with significant Spanish-language content on the site. Also, **the Obama administration is more focused on reforming a broken system through "commonsense" and "comprehensive" means,** presumably legislative.

This distills into two main realizations:

- The Obama administration saw immigration law as the problem in need of fixing.  
- The Trump administration sees immigrants as the problem that needs fixing.  

The result is a greater emphasis of the Obama administration on the need for changes in the law that help immigrants join American society in meaningful, "commonsense" ways, using legislation as the vehicle for this change, and an emphasis of the Trump administration on getting and keeping certain people out of the country, using various law enforcement agencies to accomplish this.

As with all "distant readings", this is a generalization, and there are a lot of important nuances about the two administrations and their specific actions that cannot be glazed over. However, in this time of non-stop, head-spinning news, I find it incredibly valuable to take a step back and get a broad view of what's going on.

As with science, I find this broad view of Trump's approach to immigration disturbing, even more so when compared with the Obama administration. While I agree with Obama that *immigration policy* is an issue in need of both scrutiny and reform, I find Trump's view reprehensible ― the idea that *immigrants themselves* are the problem that needs to be solved. And as long as Trump keeps talking up immigrants as the problem in need of a solution, people will continue to get hurt, no matter how many laws are passed or court cases are tried.
