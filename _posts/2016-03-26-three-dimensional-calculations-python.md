---
layout: post
title: "Three-dimensional calculations in Python 3"
modified: 2016-03-26 22:40:00 -0600
image:
  feature: structure.jpg
  teaser: structure-teaser.jpg
  credit:
  creditlink:
share: true
categories: [coding, data science]
---

I have to do some Python coding for [The Lieder Project](http://liederproject.shaffermusic.com) that involves Euclidean distance and variance in three-dimensional space. I'm positive that modules for these things exist out there somewhere, but I couldn't find them quickly. So I wrote the code myself. In case you also need to calculate distances between points in three-dimensional space, and/or the mean locations and standard deviation for points in three-dimensional space, here is the code for Python 3.

First, I created a class for three-dimensional objects.

~~~ python
class threedim(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
~~~

The following function measures the Euclidean distance between two points in three-dimensional space:

~~~ python
def threedimdistance(i, j):
    deltaxsquared = (i.x - j.x) ** 2
    deltaysquared = (i.y - j.y) ** 2
    deltazsquared = (i.z - j.z) ** 2
    return (deltaxsquared + deltaysquared + deltazsquared) ** 0.5
~~~

To use these, declare new points in three-dimensional space:

~~~ python
lineone = threedim(1,1,1)
linetwo = threedim(1,1,0.5)
linethree = threedim(0,0,0)
linefour = threedim(0.5, 0.5, 0.5)
~~~

and use threedimdistance() to measure the Euclidean distance between any two of them:

~~~ python
threedimdistance(lineone, linetwo)
~~~

To find the mean position and standard deviation of a list of points in three-dimensional space, first declare the following functions:

~~~ python
def threedimmean(threedimlist):
    xvalues = []
    yvalues = []
    zvalues = []
    for point in threedimlist:
        xvalues.append(point.x)
        yvalues.append(point.y)
        zvalues.append(point.z)
    xmean = sum(xvalues)/float(len(xvalues))
    ymean = sum(yvalues)/float(len(yvalues))
    zmean = sum(zvalues)/float(len(zvalues))
    return threedim(xmean, ymean, zmean)

def threedimSD(threedimlist):
    squareddistances = []
    listmean = threedimmean(threedimlist)
    for point in threedimlist:
        squareddistances.append(threedimdistance(point, listmean) ** 2)
    return (sum(squareddistances)/float(len(squareddistances)) ** 0.5)
~~~

Then create a list of points in three-dimensional space (from points already created ― see above) and call the above functions on that list:

~~~ python
listoflines = [lineone, linetwo, linethree, linefour]
threedimmean(listoflines)
threedimSD(listoflines)
~~~

That's it!

Unless I missed something?
