---
layout: post
title: "A journey through API programming ― Part 1: What is an API?"
modified: 2016-08-30 10:02:00 -0400
image:
  feature: apiHeader1.jpg
  teaser: apiHeader1-teaser.jpg
  credit: r2hox
  creditlink: https://www.flickr.com/photos/rh2ox/
share: true
categories: [musicology, data science]
---

An API is one of the most powerful and essential tools for web programming today. And yet, as I’ve been building my skills as a web developer lately, I’ve had a hard time finding a decent tutorial on how to use APIs, especially when authentication is involved. After a lot of digging ― and banging my head against various metaphorical walls! ― I’ve got a handle on basic API programming. I even built [a WordPress plugin](http://umwdtlt.com/hypothesis-aggregator-wordpress-plugin/) that makes use of [an external API](https://h.readthedocs.io/en/latest/api/) to collect its content.

Now I’m exploring some of the more intermediate and advanced aspects of API programming, and I’ve decided to blog my way through it, in the hopes that it will help others who want to go down this path. (It will also probably help me solidify concepts in my own mind, as well as force myself to document the process in a more organized way, which will help me down the road.)

Specifically, I’m going to explore using [Medium’s public API](https://medium.com/blog/the-medium-api-is-now-open-to-everyone-3f4642e5c850#.tuff77m2s) and integrating it into some of my current/recent ed-tech projects. If that sounds like something you’re interested in exploring, feel free to follow along! And please feel free to annotate these posts (using Medium’s native annotation tools, or the non-profit annotation tool [hypothes.is](https://hypothes.is/) ― also the basis of that plugin I mentioned!), especially if you have links or tips to share!

I’m going to aim this series of posts at readers who are relatively new to programming. APIs, like frameworks, can allow a relatively novice coder to do some really powerful things. In fact, I think APIs are a great way [to introduce some really cool things you can do with code](http://kris.shaffermusic.com/codingforteachers/) to people who are new to coding, while giving them both motivation and a framework of understanding for those foundational concepts like variables, objects, loops, and functions that they may still be working on mastering. I also want to recognize that even people who have been coding for a while may be not be an expert in *my* language of choice. So I don’t want to use examples in Python, JavaScript, or whatever that are way beyond graspability for that PHP master who is still a JavaScript novice. That said, if you’re a coder who is still trying to figure out this API thing, hopefully my tutorials will be of use.

I imagine this will be a several-part series of posts, exploring APIs in general, requesting data from APIs (and doing something with that data), authenticating with an API server, posting data over an API, and putting it all together into an API-based web app. And please feel free to leave a comment if you have suggestions or questions about other topics.

Let’s get started!

## So what is an API, anyway?!

API stands for Application Programming Interface. Let’s use Medium as an example. All of the content on Medium exists on a server (or, probably, a big bank of networked servers), and a server is just a computer that serves up data over the internet. When I want to read something on Medium, I open my browser, go to Medium.com, and use their Graphical User Interface (GUI, often pronounced “gooey”) to interact with the server ― getting, posting, editing, and deleting data.

However, if I write a *program* that I want to interact with my data on Medium, I don’t tell it to open the browser, click here and there, and read/post/edit/publish. Instead, I write code that interacts with the server via the API. The API allows for the same kinds of interactions (“methods”) ― GETting, POSTing, DELETEing, etc. ― but via an interface that is designed for interaction with another app, not with a human user.

<img src="/assets/images/apiIllustration.png" style="width: 100%;" alt="A GUI is for humans, an API is for apps." />

*A GUI is for humans, an API is for apps.*


That’s pretty much it. At least on a conceptual level. All the details about how APIs work just come out of a desire to help apps on different computers/servers talk to each other efficiently. Writing code that makes use of APIs simply requires figuring out how to use an API to connect your app with another that already exists.

Next up, … [**Why APIs?**]()

*Header photo by* [*r2hox*](https://www.flickr.com/photos/rh2ox/) *(CC BY–SA).*
