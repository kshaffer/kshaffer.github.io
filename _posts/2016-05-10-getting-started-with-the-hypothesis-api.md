---
layout: post
title: "Getting started with the hypothes.is API"
modified: 2016-05-10 20:51:00 -0600
image:
  feature: path.jpg
  teaser: path-teaser.jpg
  credit: Mohamed Sahnoun
  creditlink: https://www.flickr.com/photos/mohsan/1148848830/in/faves-131104016@N08/
share: true
categories: blog
---

[As I blogged last week](http://kris.shaffermusic.com/2016/04/hypothesis-public-research-notebook/), I am playing around with the [API](https://h.readthedocs.io/en/latest/api.html) for open-source web annotation tool, [hypothes.is](https://hypothes.is). It makes a lot of cool thing possible, including things that their own browser plugin does not (yet).

I'm new to API programming, but it turns out that it's not that difficult, if you're already comfortable in a scripting/programming environment. Following is a short Python script that returns a list of hypothes.is users who have applied the tag IndieEdTech to a public highlight or annotation. As you can imagine, you can simply trade out the tag for another search. You can limit the search to a single user ― for instance, if you want to retrieve all of *your* annotations on a particular topic. The [hypothes.is API documentation](https://h.readthedocs.io/en/latest/api.html) can give you an idea of all the things you can do.

```python
import requests
import json

source = 'https://hypothes.is/api/search?'
conn = '&'
user = ''
tags = 'tags=IndieEdTech'

searchstring = source + tags

h = requests.get(searchstring)
d = json.loads(h.text)

accounts = []
i = 0
for row in d['rows']:
    accounts.append(d['rows'][i]['user'])
    i += 1

accountset = sorted(set(accounts))

for account in accountset:
    print(account)
```

My initial goal is to write a program that will do exactly what I hinted at above: retrieve all of my own annotations on a particular topic, and export the pertinent data in MarkDown or html, so I can auto-generate a page on my website containing all of (the latest of) those annotations. But I'm teaching Maymester and [packing for a move](http://kris.shaffermusic.com/2016/03/slac-ing-off-to-virginia/), so it might be a while. I'll keep you posted.
