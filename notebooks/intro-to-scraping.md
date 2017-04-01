---
layout: page
title: Intro to Scraping
description: Intro to Scraping
---

# Intro to Scraping

This is just a test of functionality as I explore Jupyter Notebooks. First we'll import:


{% highlight python %}
from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request
{% endhighlight %}

That imports the things we need. Now we will set the URL that we need. 


{% highlight python %}
url = "https://github.com/humanitiesprogramming/scraping-corpus"
{% endhighlight %}

Now that we have that link saved as a variable, we can call it up again later. 


{% highlight python %}
print(url)
{% endhighlight %}

    https://github.com/humanitiesprogramming/scraping-corpus


We can also modify the URL if we want to use that URL as a base but we need to use a variation on it.


{% highlight python %}
print(url + "/subdomain")
{% endhighlight %}

    https://github.com/humanitiesprogramming/scraping-corpus/subdomain


We will use that URL to grab the basic HTML for the URL. The following code uses a Python package named "request" to go out and visit that webpage. The following two lines say, "Take the link stored at the variable 'url'. Visit it, read back to me what you find, and store that result in a new variable named HTML.


{% highlight python %}
html = request.urlopen(url).read()
print(html[0:2000])
{% endhighlight %}

    b'\n\n\n\n\n\n<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="utf-8">\n\n\n\n  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-80206cf5276e283a2a42e750a19cfc777c5bc184c6509b5db88bac96930c339f.css" media="all" rel="stylesheet" />\n  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-e37787f054128b693988d66147a56af54ed8c479fa4abd1a183d787453cc90a6.css" media="all" rel="stylesheet" />\n  \n  \n  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-f4fa6ace91e5f0fabb47e8405e5ecf6a9815949cd3958338f6578e626cd443d7.css" media="all" rel="stylesheet" />\n  \n\n  <meta name="viewport" content="width=device-width">\n  \n  <title>GitHub - humanitiesprogramming/scraping-corpus</title>\n  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">\n  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">\n  <meta property="fb:app_id" content="1401488693436528">\n\n    \n    <meta content="https://avatars3.githubusercontent.com/u/19490737?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="humanitiesprogramming/scraping-corpus" property="og:title" /><meta content="https://github.com/humanitiesprogramming/scraping-corpus" property="og:url" /><meta content="Contribute to scraping-corpus development by creating an account on GitHub." property="og:description" />\n\n  <link rel="assets" href="https://assets-cdn.github.com/">\n  \n  <meta name="pjax-timeout" content="1000">\n  \n  <meta name="request-id" content="E142:1446:33EFACA:4B07C4D:58E00345" data-pjax-transient>\n  \n\n  <meta name="selected-link" value="repo_source" data-pjax-transient>\n\n  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">\n<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">\n    <meta name="google-analytics"'



Wait - why are we scraping from GitHub instead of Project Gutenberg?
Project Gutenberg does not allow automated scraping of their website. So, instead I have collected a corpus of Project Gutenberg texts and loaded them into a GitHub repository for you to practice on.

So far we just have a whole bunch of HTML. We'll need to turn that into something that Beautiful Soup can actually work with.


{% highlight python %}
soup = BeautifulSoup(html, 'lxml')
{% endhighlight %}

This line says, "take the HTML that you've pulled down and get ready to do Beautiful Soup things to it." Think of it this way: you have a certain number of things that you can do in your car:
    
* Drive
* Fill it with gas
* Change the tires
    
But you can only really do those things once you actually get in your car. You couldn't change your tires if you were riding a horse. Horses don't have wheels. In programming speak, we're saying "turn that HTML into a Beautiful Soup **object**." Saying something is an object is a way of saying "I expect this data to have certain characteristics and be able to do certain things." In this case, BeautifulSoup gives us a series of ways to manipulate the HTML. We can do things like:

* Get all the links


{% highlight python %}
soup.find_all('a')[0:10]
{% endhighlight %}




    [<a class="accessibility-aid js-skip-to-content" href="#start-of-content" tabindex="1">Skip to content</a>,
     <a aria-label="Homepage" class="header-logo-invertocat" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark" href="https://github.com/">
     <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewbox="0 0 16 16" width="32"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg>
     </a>,
     <a class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features" href="/features">
               Features
     </a>,
     <a class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/security /business/customers /business" href="/business">
               Business
     </a>,
     <a class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /showcases /explore" href="/explore">
               Explore
     </a>,
     <a class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing" href="/pricing">
               Pricing
     </a>,
     <a class="header-search-scope no-underline" href="/humanitiesprogramming/scraping-corpus">This repository</a>,
     <a class="text-bold site-header-link" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in" href="/login?return_to=%2Fhumanitiesprogramming%2Fscraping-corpus">Sign in</a>,
     <a class="text-bold site-header-link" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up" href="/join?source=header-repo">Sign up</a>,
     <a aria-label="You must be signed in to watch a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-n" href="/login?return_to=%2Fhumanitiesprogramming%2Fscraping-corpus" rel="nofollow">
     <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z" fill-rule="evenodd"></path></svg>
         Watch
       </a>]



We can say, get all me the text


{% highlight python %}
soup.text[0:2000]
{% endhighlight %}




    '\n\n\n\n\n\n\nGitHub - humanitiesprogramming/scraping-corpus\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSkip to content\n\n\n\n\n\n\n\n\n\n\n\n\n          Features\n \n          Business\n \n          Explore\n \n          Pricing\n \n\n\n\n\nThis repository\n\n\n\n\nSign in\nor\nSign up\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n    Watch\n  \n\n    3\n  \n\n\n\n\n    Star\n  \n\n      0\n    \n\n\n\n\n        Fork\n      \n\n      0\n    \n\n\n\n\nhumanitiesprogramming/scraping-corpus\n\n\n\n\n\n\n\nCode\n\n \n\n\n\nIssues\n0\n\n \n\n\n\nPull requests\n0\n\n \n\n\n      Projects\n      0\n\n\n\n    Pulse\n\n\n\n    Graphs\n\n\n\n\n\n\n\n\n\n\n            No description, website, or topics provided.\n          \n\n\n\n\n\n\n\n\n\n\n\n              1\n            \n            commit\n        \n\n\n\n\n\n            1\n          \n          branch\n        \n\n\n\n\n\n            0\n          \n          releases\n        \n\n\n\n\n\n      1\n    \n    contributor\n\n\n\n\n\n\n\n\n\nClone or download\n\n\n\n\n\n          Clone with HTTPS\n          \n\n\n\n\n          Use Git or checkout with SVN using the web URL.\n        \n\n\n\n\n\n\n\n\n\n  Download ZIP\n\n\n\n\n\n\n\n      Find file\n    \n\n\n\nBranch:\nmaster\n\n\n\n\n\nSwitch branches/tags\n\n\n\n\n\n\n\n\nBranches\n\n\nTags\n\n\n\n\n\n\n\n\n\n                master\n              \n\n\nNothing to show\n\n\n\n\nNothing to show\n\n\n\n\n\n        New pull request\n      \n\n\n\n\n\n      Latest commit\n      \n        f31bfdb\n      \nApr 1, 2017\n\n\n\nwalshbr\n\nuploads initial corpus\n\n\nPermalink\n\n\n\n\nFailed to load latest commit information.\n\n\n\n\n\n\n\n0.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n1.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n2.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n3.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n4.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n5.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n6.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n7.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n8.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n9.txt\n\n\n\nuploads initial corpus\n\n\n\nApr 1, 2017\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nContact GitHub\nAPI\nTraining\nShop\nBlog\nAbout\n\n\n\n\n\n© 2017 GitHub, Inc.\nTerms\nPrivacy\nSecurity\nStatus\nHelp\n\n\n'



It might not be very clear, but that's just the text of the webpage as one long string with all the HTML stripped out. Here is a slightly prettier version that strips out all the '\n' characters (those are a just a way for Python to note that there should be a line break at that point in the string):


{% highlight python %}
soup.text.replace('\n', ' ')[0:1000]
{% endhighlight %}




    '       GitHub - humanitiesprogramming/scraping-corpus                                  Skip to content                       Features             Business             Explore             Pricing       This repository     Sign in or Sign up                      Watch         3            Star           0                  Fork               0          humanitiesprogramming/scraping-corpus        Code       Issues 0       Pull requests 0            Projects       0        Pulse        Graphs                       No description, website, or topics provided.                                     1                          commit                           1                      branch                           0                      releases                     1          contributor          Clone or download                Clone with HTTPS                          Use Git or checkout with SVN using the web URL.                     Download ZIP              Find file         Branch: master  '



All that white space is coming because we're grabbing a lot of whitespace from the *entire* page. We can either strip whitespace out, or we can make a bit more nuanced request. Instead of getting all the page text first, we can say, "first get me only the HTML for the links on this page. Then give me the text for just these smaller chunks.


{% highlight python %}
soup.find_all('a').text
{% endhighlight %}


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-22-243f0feb02af> in <module>()
    ----> 1 soup.find_all('a').text
    

    AttributeError: 'ResultSet' object has no attribute 'text'


Wait, what happened there? Python gave us an error. This is because we got confused about what kind of object we were looking at. The error message says, "This thing you've given me doesn't support the method or attribute '.text' Let's work backwards to see what we actually get from soup.find_all('a'):


{% highlight python %}
soup.find_all('a')[0:10]
{% endhighlight %}




    [<a class="accessibility-aid js-skip-to-content" href="#start-of-content" tabindex="1">Skip to content</a>,
     <a aria-label="Homepage" class="header-logo-invertocat" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark" href="https://github.com/">
     <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewbox="0 0 16 16" width="32"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z" fill-rule="evenodd"></path></svg>
     </a>,
     <a class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features" href="/features">
               Features
     </a>,
     <a class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/security /business/customers /business" href="/business">
               Business
     </a>,
     <a class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /showcases /explore" href="/explore">
               Explore
     </a>,
     <a class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing" href="/pricing">
               Pricing
     </a>,
     <a class="header-search-scope no-underline" href="/humanitiesprogramming/scraping-corpus">This repository</a>,
     <a class="text-bold site-header-link" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in" href="/login?return_to=%2Fhumanitiesprogramming%2Fscraping-corpus">Sign in</a>,
     <a class="text-bold site-header-link" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up" href="/join?source=header-repo">Sign up</a>,
     <a aria-label="You must be signed in to watch a repository" class="btn btn-sm btn-with-count tooltipped tooltipped-n" href="/login?return_to=%2Fhumanitiesprogramming%2Fscraping-corpus" rel="nofollow">
     <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewbox="0 0 16 16" width="16"><path d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z" fill-rule="evenodd"></path></svg>
         Watch
       </a>]



That looks as expected. To see what's going, let's look at it another way. The following line will tell us what kind of object we're looking at:


{% highlight python %}
type(soup.find_all('a')).__name__
{% endhighlight %}




    'ResultSet'



Ah! We're getting somewhere. We're looking at a ResultSet. Not a BeautifulSoup object. And ResultSets let us do different things to them. In fact, a results set gives us a list of Tag objects, but those still respond to a lot of the same things as BeautifulSoup objects. Check it:


{% highlight python %}
type(soup.find_all('a')[0]).__name__
{% endhighlight %}




    'Tag'




{% highlight python %}
soup.find_all('a')[0].text
{% endhighlight %}




    'Skip to content'



How many links are there on this page anyway? We can find out by checking out the length of this ResultSet:


{% highlight python %}
len(soup.find_all('a'))
{% endhighlight %}




    71



Here we go. Soup.find_all() returns us something roughly equivalent list. And you can do certain things to lists - you can find out how long they are, you can sort them, you can do things to each item. But you can't pull out the text of each list. That's something that a BeautifulSoup object can do. We were trying to change the tires of our horse. We could, though, go through element in that list and get the text for each individual item. The following lines do just that but also give a little formatting on either side to make it more readable. And we'll strip out whitespace again


{% highlight python %}
for item in soup.find_all('a')[0:10]:
    print('=======')
    print(item.text.replace('\n', ''))

{% endhighlight %}

    =======
    Skip to content
    =======
    
    =======
              Features
    =======
              Business
    =======
              Explore
    =======
              Pricing
    =======
    This repository
    =======
    Sign in
    =======
    Sign up
    =======
        Watch  


Now we're getting somewhere. Beautiful Soup can pull down data from a link, but we'll just have to be careful that we know what kinds of objects we are working with. So let's pull down only the links that we care about by being a bit more specific.


{% highlight python %}
for link in soup.select("td.content a"):
    print(link.text)
{% endhighlight %}

    0.txt
    1.txt
    2.txt
    3.txt
    4.txt
    5.txt
    6.txt
    7.txt
    8.txt
    9.txt


The "td.content a" bit is using css syntax to walk the structure of the HTML document to get to what we want. It says, "find the 'td' tags that have a 'class' content and then give me the 'a' tags inside. Once we have all that, print out the text of those 'a' tags. If you haven't worked with css before, you can find a good tutorial for css selectors [here](https://www.w3schools.com/cssref/css_selectors.asp). Rather than getting the text of those links, this time we will collect those links and store them in a list for us to scrape.


{% highlight python %}
links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href']
    urls.append(url)
print(urls)
{% endhighlight %}

    ['/humanitiesprogramming/scraping-corpus/blob/master/0.txt', '/humanitiesprogramming/scraping-corpus/blob/master/1.txt', '/humanitiesprogramming/scraping-corpus/blob/master/2.txt', '/humanitiesprogramming/scraping-corpus/blob/master/3.txt', '/humanitiesprogramming/scraping-corpus/blob/master/4.txt', '/humanitiesprogramming/scraping-corpus/blob/master/5.txt', '/humanitiesprogramming/scraping-corpus/blob/master/6.txt', '/humanitiesprogramming/scraping-corpus/blob/master/7.txt', '/humanitiesprogramming/scraping-corpus/blob/master/8.txt', '/humanitiesprogramming/scraping-corpus/blob/master/9.txt']


Getting closer to some usable URL's. We just need add the base of the website to it. So here is the same piece of code but reworked slightly. We'll modify the URL just slightly because of the way that GitHub formats its URL's. We want to get something like [this](https://raw.githubusercontent.com/walshbr/ohio-five-workshop/master/cli-tutorial.md) instead of [this](https://github.com/walshbr/ohio-five-workshop/blob/master/cli-tutorial.md), which is what we were getting. The former is stripped of all the GitHub formatting.


{% highlight python %}
links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)
print(urls)
{% endhighlight %}

    ['https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/0.txt', 'https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/1.txt', 'https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/2.txt', 'https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/3.txt', 'https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/4.txt', 'https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/5.txt', 'https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/6.txt', 'https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/7.txt', 'https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/8.txt', 'https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/9.txt']


Bingo! Since we know how to go through a list and run code on each item, we can get closer to scraping them to combine them into a dataset for us to use. Let's scrape each of them. We'll be re-using code from above. See if you can remember what each piece is doing:


{% highlight python %}
corpus_texts = []
for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)
{% endhighlight %}

The variable corpus_texts now is a list containing ten different novels. We've got a nice little collection of data, and we can do some other things with it.
