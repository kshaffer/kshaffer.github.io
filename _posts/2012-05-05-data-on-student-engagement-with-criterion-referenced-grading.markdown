---
author: KShaffer
comments: true
date: 2012-05-05 20:17:01
layout: post
slug: data-on-student-engagement-with-criterion-referenced-grading
title: Data on student engagement with criterion-referenced grading
wordpress_id: 365
tags:
- average-based grading
- criterion-referenced grading
- CSU
- data
- grades
- holistic grading
- teaching
---

One objection that often comes up in response to a criterion-referenced or standards-based grading system is that it does not sufficiently motivate students to engage coursework throughout the semester. If students only need to demonstrate mastery by the end of the semester, they can skip homework assignments with impunity (or so they think). And if they don't do the work, they won't engage the material sufficiently to succeed in mastering the material by the end of the semester. This point was raised in response to several of my early [posts on criterion-referenced grading](/tags/criterion-referenced-grading/).

There are two claims here: first, that students are more likely to do assignments that count toward their final grade (as they do in traditional average-based grading); and second, that students are more likely to master the material and accomplish the course objectives if they do more of the assignments.

I now have some data that speaks to both of those claims. 

(Though, I should note that I don't have _much_ data. So while my data may suggest something about the veracity and validity of these claims, I want to be clear up front that my data is not sufficient basis for any conclusions. If others out there have data of their own to contribute, perhaps a collaborative effort may lead to claims of substance.)



## Grades and student incentive to work



I will leave philosophical matters aside here about whether grades should reflect mastery, behavior, or some combination thereof. (I tend toward mastery rather than behavior, as you might guess.) Though that issue is an important one not to overlook in discussions of grading methods, I simply want to focus on the two claims presented above in this post. The first question, then, is do students in an average-based grading system, where each assignment counts towards their final grades, do more coursework than students in a criterion-referenced grading system?

To explore this matter, I took data from my gradebook for the fall semester's Music Theory I class (MUSI 131, holistic and average-based grading) and this semester's Music Theory II class (MUSI 134, criterion-referenced with multiple categorical grades for most assignments). I have data for other courses I taught this year, but these classes are my largest, they have the most assignments, and they have the most similar kinds of assignments. That said, it was still difficult to get an apples-to-apples comparison. The distinction between homework and test became fuzzier in Theory II, for one thing. Once you stop using a grading system that counts homework and tests differently, but groups assessments by course objective, that distinction is bound to diminish. Incorporating inverted-classroom techniques does the same thing. Theory II still had homework, quizzes, and tests, but the distinction between in-class practice work not for a grade, in-class practice work for a grade, quizzes, tests, graded practice tests, homework, and take-home tests/projects becomes messy.

The data-related result is that the quizzes in Theory I have no direct correlate in Theory II. The tests (in-class and take-home) in Theory I are sometimes comparable to Theory II homework and sometimes comparable to Theory II tests. And I don't have data on how many students did in-class assignments in Theory II that were looked at but not graded. (I could compare class activity notes to attendance records, but those activities have no correlate in Theory I, and I'm lazy.) So I decided to count all graded homework and tests for both classes, but not ungraded work or in-class quizzes (since the latter existed in only one class). I think this is a fair comparison, and where any unfairness exists, it will tip things in favor of the claim I hoped was false, so I'm okay with that. Take it for what you will.

Okay, now the data.

For each course, I took the number of assignments submitted (including redoes) and tests taken for each student, and divided that by the number of assignments and tests given to obtain a percentage of work performed. For Theory I (average-based grading, one shot per assignment), the mean amount of work submitted by students that finished the semester was 92%; the 95% confidence range was 86%–98%. For Theory II (criterion-referenced grading, redoes allowed), the mean amount of work submitted by students that finished the semester was 87%; the 95% confidence range was 78%–96%. 

The 95% confidence ranges (represented by error bars on the chart below) are important. They demonstrate that though there is a difference in the mean value for each semester, regular variance from student to student and from semester to semester cannot be ruled out as the cause of that difference. In other words, there is no statistically significant effect of grading system on the amount of work done by students in these courses.

[![](/uploads/2012/05/Assessments-completed.png)](/uploads/2012/05/Assessments-completed.png)

Now some will object that I counted redoes for the criterion-referenced grading system, stacking the deck in my favor. Well, I'll tell you that there is a statistically significant difference between assignments submitted in Theory I and first attempts submitted in Theory II. The mean value there is 69%, with a 95% confidence range of 63%–75%.

However, I included redoes for two reasons. First, the claim to which I am responding is not that average-based grading motivates students to do a large number of assignments and that completing more distinct assignments leads to better understanding. The objection raised is that average-based grading motivates students to engage with the material more regularly and that regular engagement leads to better understanding. Redo assignments certainly contribute to student learning. In fact, that leads to my second reason: as I will argue shortly with data, I believe that redo assignments (following helpful instructor comments—and receiving multiple categorical grades for each assignment is part of that) contribute _more_ to student learning than first-attempt assignments. So let's move on to that data.



## What kind of work helps students learn best?



Assignments where students are not penalized for failure but instead are encouraged to take comments from the instructor and apply them on another attempt at the same assignment before moving on, without any final grade penalty for that first attempt.

Here's the data.

I analyzed a number of parameters for 17 students who took both Music Theory I and Music Theory II: Theory I final grades, Theory II final grades, the difference between those grades (each letter/+/– combination was given an integer rank, and the difference was calculated), the percentage of assignments & tests submitted in Theory I, same for Theory II, percentage of first-attempt assignments (number of first-attempt submissions / number of assignments given—no tests or projects were included) in Theory II, and percentage of redo submissions (number of redo submissions / number of assignments given—no tests or projects were included) in Theory II.

I used Spearman rank correlation to test which of the pieces of information about student engagement most predict student success (Theory II final grade) and student improvement (difference between Theory I and II). I used the SciPy.stats.stats.spearmanr() function in Python (I'm told that the p values may be unreliable for data sets of less than 500 elements, so take them as you wish).

What is the best predictor of student grades for Theory II? Theory I grades. The Spearman coefficient of rank correlation (rho) between Theory I grades and Theory II grades is 0.53, p < 0.03. So a moderate correlation that (as far as I can tell using this tool) is statistically significant. And that makes sense. Good students do well no matter what the grading scheme; poor students poorly; etc. Nothing else had anything near a statistically significant correlation with Theory II grades (and the rho values were low or low and negative anyway). So in this group of students, the amount of work done (overall, redoes, or first attempts) had no significant effect on their final grade.

But what is the best predictor of student _improvement_ from Theory I to Theory II? The best predictor of student improvement was a low score in Theory I! Theory I grades and grade improvement correlated at rho = -0.61, p < 0.01. Of course, that could just be regression to the mean. Students with As in Theory I can only hold steady or go down, and vice versa.

There were no other significant correlations, but there was one other that was very close (and remember that the p values may not be reliable for such a small sample). Student improvement correlated moderately (rho = 0.46, p < 0.06) with number of redo submissions. Not overall work, not number of first-attempts, but redoes. 

This makes sense, and I can think of specific students where this was huge—in one case a student submitting redoes on about a quarter of the assignments improved from a C in Theory I to an A in Theory II. Quality and specificity of instructor comments are important, though, as is student attention to those comments, for redo assignments to effect improvement. I'll save comments on that for another post.



## Conclusion



Again, the data I collected here is minimal, and I don't want to make any strong claims based on it. However, this data suggests that—at least for this group of students—having an assignment count toward the final average does not have a significant effect on student motivation to do the work. This data also suggests that percentage of assigned work submitted during a semester does not predict student outcomes. However, this data _does_ suggest that percentage of assignments re-submitted by students (especially students who struggled previously) may have a significant effect on student improvement.

It should be noted that though my specific take on criterion-referenced grading this semester showed no significant difference in amount of work submitted, that may not always be the case for criterion-referenced grading more generally. I gave my students 23 assessments, for 10 categorical grades, and students were required to pass a minimum of 8 to get a C, 9 to get a B, and 10 to get an A (in addition to weighing the actual scores). Many assignments, tests, and projects counted toward multiple categories, but that didn't leave many assignment students could skip and still cover all the categories. And a few early slackers found that out as we got closer to midterm. We also started many assignments in class, while I walked around the room catching errors and answering questions (office hours for everyone, essentially), which got the ball rolling and got most of them over any initial freeze that might happen were they to start it on their own late the night before the due date. Had we not done those things, results may have been different. So I'm not suggesting that criterion-referenced grading will never lead to students not turning in work until it's too late. But the way I did it this semester did not.

I hope this post has been helpful for some of you thinking through things for next semester. And if you have data to add to mine and are interested in a larger quantitative exploration of the claims discussed here, please let me know. It would be an interesting and valuable project, I think.
