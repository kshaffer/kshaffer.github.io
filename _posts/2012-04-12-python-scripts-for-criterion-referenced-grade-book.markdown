---
author: KShaffer
comments: true
date: 2012-04-12 13:43:29
layout: post
slug: python-scripts-for-criterion-referenced-grade-book
title: Python scripts for a criterion-referenced grade book
wordpress_id: 322
tags:
- criterion-referenced grading
- teaching
---

When using a criterion-referenced or standards-based grading system, one big question is always how to manage grade records. The issues are that a single assignment may contribute to assessment for a number of different course objectives, a given course objective/grading criterion will reflect multiple assignments, and students may resubmit assignments at least once, sometimes several times. Thus, a traditional electronic grade book either will not fit the system, or it will be huge, slow, and clunky.

I decided that rather than force my model into an unwieldy spreadsheet, I would write some python scripts to do the job for me (<a href="http://kris.shaffermusic.com/media/gradebook.zip">download the scripts and a sample course grade list here</a>). I wrote three scripts: one for grade entry (which I then modified into a version for each class that contained the specific grading categories for that class), one to generate a report for a given assignment (listing student name and score by category), and one to generate a report for a given student (listing assignment title and score by category). The grades go into a CSV file, one per course. 

This has worked pretty well for my system. Every week or so, I go in and generate a report for each student in each class. Looking at that report, I can see their progress in each category over time, and I assign them a current score in that category based on their most recent work and progress. Those current scores go in the grade book on the course website, so they can log in and see their current progress in the dozen or so categories and know where they most need to focus their efforts.

If this sounds like it might work for your system, or if you know python well enough to modify it for your system, feel free to download the scripts and play around with them. Below is a screencast video of me demonstrating how they work. Nothing particularly fancy, but it may give you an idea how I use it and how it might work for you.

<embed src="http://kris.shaffermusic.com/media/PythonGradeBook.mp4" width=662 height=536 autoplay=false controller=true loop=false pluginspage=http://www.apple.com/quicktime/" />