---
layout: post
title: "Introducing Pypothesis ― Part 2: a Python module for the hypothes.is API"
modified: 2016-06-06 14:43:00 -0400
image:
  feature: stormdrain.jpg
  teaser: stormdrain-teaser.jpg
  credit: darkday
  creditlink: https://www.flickr.com/photos/drainrat/15783249894/in/faves-131104016@N08/
share: true
categories: blog
---

Recently I've created two tools to help people make fuller use of hypothes.is in their work as public scholars. This post is the second in a two-part series introducing and explaining those tools, which are based on the hypothes.is API. For Part 1, see [Introducing Pypothesis ― Part 1: hypothes.is to MarkDown](http://kris.shaffermusic.com/2016/06/introducing-pypothesis-1/).


## The hypothes.is API

The hypothes.is API is pretty powerful. [As I've written about previously](http://kris.shaffermusic.com/2016/04/hypothesis-public-research-notebook/), there are a lot of cool things the hypothes.is software can do that their browser plugin cannot (yet). To date, most discussion and marketing has focused around what the browser plugin can do when multiple scholars/students/collaborators are annotating a single web page. However, as a teacher I'm more interested in what it can do when students are sent out to find *a variety* of public resources to annotate and share with each other. As a researcher, I'm more interested in how I can use hypothes.is as a simple tool to collect things I read that I want to come back to or build on in my work. And as a programmer, I'm interested in making it easier for people to use a cool, open-source, non-profit tool like hypothes.is to do those things.

So what follows is my attempt to create a Python module for the hypothes.is API. Not only can I then use it to create scripts and apps that can accomplish some of those goals just mentioned, but others can use it to build their own extensions of hypothes.is more easily.


## Pypothesis ― a Python module for the hypothes.is API

Pypothesis (download from GitHub) is a Python module that provides programmers a simpler interface for the hypothes.is API. Rather than calling the API and parsing the resulting JSON data directly in an application, this module includes object classes and functions that make coding with the hypothes.is API simpler.

Since I am particularly interested in helping (aspiring) public scholars use hypothes.is as an early-stage tool to find, share, and build off of existing work, this module is focused on the GET portion of the hypothes.is API (retrieving data, *not* writing, editing, or deleting existing data). It also does not deal with authentication since, again, I'm focused on *public* work, which does not need authentication to retrieve via the hypothes.is API. If others want to build on my work and augment my code, I'd be more than willing to consider pull requests (GitHub lingo for code other people have written that they'd like me to consider adding to my module). However, at least for now, I'm not planning on adding authentication, writing, editing, or deleting to this module.

I hope this tool is of value to many. If you're interested in checking it out, making use of it, and/or building on it, the information and sample code offered below will help you get started.

Following is a list of classes and functions in this module that Python programmers can use to incorporate hypothes.is functionality in their scripts.

### Annotation()

An object class for a single hypothes.is annotation. Call Annotation(json_data_for_single_annotation) to create a new object. This object has the following attributes:

- title (the title of the annotated article)  
- uri (the uri of the annotated article)  
- highlight (the article text highlighted in the annotation)  
- comment (the annotation comment left by the annotator)  
- user (the hypothes.is user ID of the annotator)  
- created (the date and time the annotation was created)  
- updated (the date and time the annotation was updated)  
- id (the unique ID of the hypothes.is annotation; this ID is included in the URL for the annotation)  
- hypothesisurl (the URL for the annotation)  

### retrieve()

A function that retrieves the JSON data for a single hypothes.is annotation, given the annotation's API URL. Call retrieve(api_url_for_a_single_annotation) to retrieve the JSON data, for passing into the Annotation() class.

### retrievelist()

A function that retrieves the JSON data for a list of hypothes.is annotations, given a well-formed search URL for the hypothes.is API. Call retrievelist(search_url_for_the_hypthes.is_api) to retrieve the JSON data for all annotations in the search results. Each annotation's JSON data is an item in a list. Use a for loop to pass each item returned into the Annotation() class.

### apiurl()

A function that converts a *share* URL (easy to find in the hypothes.is user interface) into an API-friendly URL (difficult to find), for passing to retrieve(). Call apiurl(share_url_for_an_individual_annotation) to return the API-friendly URL.

### searchurl()

A function that takes a hypothes.is user name and/or a tag (or list of tags) and generates a well-formed search URL for the hypothes.is API. The format is:

~~~ python
searchurl(user = '', tag = '', tags = [])
~~~

The searchurl() function requires at least one search term. It can be either a user name, a single tag, or a list of tags (as a well-formed Python list). Use *either* a single tag or a list of tags, not both. If you happen to send it both, it will take the list of tags and ignore the single tag.

Example searches:

~~~ python
# all annotations from a single user
searchurl(user = 'kris.shaffer@hypothes.is')
# or
searchurl('kris.shaffer@hypothes.is')

# all annotations tagged IndieEdTech
searchurl(tag = 'IndieEdTech')

# all annotations from a single user tagged IndieEdTech
searchurl(user = 'kris.shaffer@hypothes.is', tag = 'IndieEdTech')
# or
searchurl('kris.shaffer@hypothes.is', 'IndieEdTech')

# all annotations tagged IndieEdTech AND EdTech (for an OR search, simply perform two searches and combine the results)
searchurl(tags = ['IndieEdTech', 'EdTech'])
~~~

### Example code

~~~ python
# search for all annotations with the tag IndieEdTech and return them in json format.
s = searchurl(tag = 'IndieEdTech')
l = retrievelist(s)

# print the title of each article annotated.
for entry in l:
    e = Annotation(entry)
    print(e.title)
~~~

~~~ python
# Using the hyothes.is annotation share URL, retrieve and parse the JSON data for that annotation, then print it.
t = Annotation(retrieve(apiurl('https://hyp.is/AVOP5R06H9ZO4OKSlTrY/hackeducation.com/2016/03/18/i-love-my-label')))
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
