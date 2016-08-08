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

The following is a module created with [Trinket](https://trinket.io). It contains the code to my [Pypothesis](https://github.com/kshaffer/pypothesis) module for the [Python 3](https://www.python.org/) programming language. The module allows users to write simple queries that collect and display information from public annotations on [hypothes.is](https://hypothes.is). We'll use it to learn a little about Python, API calls, and using existing code to do relatively powerful things with just a little code (and coding knowledge).

### Activity

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

## Playing with text in public using JavaScript

Visit [Monkeys writing Shakespeare (or Austen...)](http://kris.shaffermusic.com/monkeyswritingshakespeare). This site takes the opening of Jane Austen's *Pride and Prejudice* and randomly replaces words from the text with other words with the same part of speech. We'll use it (and hack it) to learn a little bit about JavaScript, asynchronous programming, and developing playful web apps.

### Activity

Visit the web app's [project page on GitHub](https://github.com/kshaffer/monkeyswritingshakespeare). Click on the green button to download a zip file containing the code for this web app. Extract that zip file somewhere on your computer. Open the index.html file in a web browser (double-clicking on it should do), and then open both the app.js and index.html files in a plain-text editor (something like Notepad or TextEdit, *not* a word processor like MS Word or Pages ― if you're in the market for a more powerful text editor, I highly recommend TextMate (Mac only) or [Atom](atom.io) (cross-platform)). It will also be helpful to open up your browser's *developer tools* (I'll walk you through this if you can't find it).

Once loaded up, take a look at the code and the web page and see if you can get your bearings. We'll take a couple minutes to get oriented to the code's organization together.

Once we have our bearings, there are a few activities to try. Feel free to tackle any or all of these, on your own or with a partner, depending on how comfortable you feel with each of them.

- Add words to one or more of the *arrays* at the top of the app.js file. The more words from the source text can be found here, the more active the script is. What happens when you add words not in the source text? when you mix up parts of speech? when you insert non-English or non-sensical words?  
- Switch out the source text with something else (a Shakespearean sonnet, a political stump speech, your (least) favorite song's lyrics...). Did it work? Look at the way the Austen source text is entered. What special additions/changes do you need to make to get it to work?  
- Find the timer. What does the number mean? Change the timing and see what happens.  
- Why does the app.js code include "document.getElementById('shakespeare')" when the text is by Austen? What happens if you change *shakespeare* to *austen*?
- More advanced: Create a new array of words (such as places or conjunctions) at the top of the app.js file. Then find the comment 'WORD REPLACEMENT LOOP' in the code. Add the code required to use your new array.

### Reflection

What ideas does this app give you for your own projects?

What differences do you note between Python and JavaScript? If you were to pick one of the two languages to learn first, which would you pick? Why?
