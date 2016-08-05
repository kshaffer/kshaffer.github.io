---
layout: page
title: "Coding for Teachers"
modified: 2016-05-31 13:37:00 -0500
image:
  feature: pw2.jpg
  teaser: pw2-teaser.jpg
  credit: Christiaan Colen
  creditlink: https://www.flickr.com/photos/132889348@N07/20971563620/
---

## Playing with Python and Pypothesis

The following is a module created with [Trinket](https://trinket.io). It contains the code to my [Pypothesis](https://github.com/kshaffer/pypothesis) module for the [Python 3](https://www.python.org/) programming language. The module allows users to write simple queries that collect and display information from public annotations on [hypothes.is](https://hypothes.is).

Ignore the first 100 lines of code for now. (If you installed this module on your computer, you wouldn't have to look at it. It would be embedded in the system.) There are two blocks below the line that says [code]\# test[/code]:

~~~python
# search for all annotations with the tag IndieEdTech and return them in json format.
s = searchurl(tag = 'IndieEdTech')
l = retrievelist(s)
# print the title of each article annotated.
for entry in l:
    e = Annotation(entry)
    print(e.title)
    print(e.user)
    print('\n')
~~~

and

~~~python
# Using the hyothes.is annotation share URL, retrieve and parse the JSON data for that annotation, then print it.
t = Annotation(retrieve(apiurl('https://hyp.is/s43Svk2xEeaKmptcVb4Svg/kris.shaffermusic.com/2015/03/sustainable-pedagogy/')))
print(t.title)
print(t.uri)
print(t.highlight)
print(t.comment)
print(t.user)
print(t.created)
print(t.updated)
print(t.id)
print(t.hypothesisurl)
~~~

Choose one of these blocks, and delete the three quotation marks at the beginning and end of the block. (These quotation marks tell Python to leave the code in place, but not to run it. Removing it runs that code, after loading the module in the first 100 lines.) Then click "Run" (it may just look like a play button) at the top of the Trinket window.

Now put the quotation marks back. Then try the same thing with the other block.

What do these blocks of code do? What alterations can you make? What else would you search for?

<iframe src="https://trinket.io/embed/python3/ac6183e555" style="indent: -200px" width="1000" height="800" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

### Reflection

After you've played around a bit, take a peek at the code in lines 1-100. Can you figure out what the difference is between the search code in the two blocks? Why does one require a URL? Why does the [code]searchURL()[/code] function not contain a URL?

## Analyzing and visualizing data with R



### Reflection
