---
layout: page
title: More Humanistic Python Debugging Exercises
description: for HILT 2019
permalink: /exercises/humanistic-python-debugging/
javascript:
  - /assets/js/hint.js
---

# Common Code Errors and How to Find Them  

Many errors in code written by developers at all levels boil down to just a few common types of problems:

1.  Syntax: check brackets, if/elsif/else statements, braces, commas, parentheses, quotation marks, etc. The computer needs syntax to be exactly right in order for it to run your programs: it cannot make any assumptions about what you might mean. So it cannot, for example, infer "Wednesday" from "Wendesday." Make sure you are using [python syntax](https://docs.python.org/2/reference/).
2.  Variables: make sure your variable names are consistent and that they are defined before you use them for the first time. Name them in ways that convey their use so that others (and you!) remember what they are meant to do.
3.  Functions: make sure that you know how your functions work. What kinds of things do they return? A string? A list? A dictionary?


If you get stuck, try the following to help you figure out what is going on:

1.  Print out variable values at different points in the program to make sure they return what you expect.
2.  Make sure the coloring in your text editor looks like you expect it to.
3.  Read the error output in the terminal. It tries to be helpful, but it will often not quite point you towards the problem. It can at least give you a ballpark location in the code and some things to look for.
4.  Get sections of the code working (see step one) so that you can narrow your search for the problem. Python can help with this: try playing in this environment to debug sections.
5.  Read the Python documentation for the methods you are employing.
6.  Comment throughout your code to make sure you understand what every step is doing. This will help you pinpoint problems.
7.  Ask for help!

<hr/>

These exercises will help you practice debugging your code. There are no problems: only solutions waiting to be found.

## Texts

A book you are interested in is 457 pages long, with an average of 250 words per page. If you were to break your book into 100 equal pieces, how many words would there be in each piece? Can you write code that is flexible enough to use for different lengths?

Broken:

{% highlight ruby %}

pages = 457
word_per_page == 250
number-of-pieces = 100

each_chunk = [457 * 250]/10
print "each_chunk"

{% endhighlight %}

Fixed:

{% highlight ruby %}

pages = 457
words_per_page = 250
number_of_pieces = 100

each_chunk = (457 * 250)/100
print(each_chunk)

{% endhighlight %}

<hr/>

## Metadata

Create a collection of texts and metadata about them. Then, print out information about those texts using a method.

Example Data for your Collection:

Jane Eyre, 1847<br>
Cane, 1923<br>
Wide Sargasso Sea, 1966<br>
Citizen: An American Lyric, 2014<br>

Example output you might aim for:

Jane Eyre was published in 1847.

Broken:

{% highlight ruby %}

text = [
	"Jane Eyre": "1847",    
	Cane: "1923",    
	"Wide Sargasso Sea"- 1966,    
	"Citizen: An American Lyrics": "2014"
]

for title. date in texts.items():
	print{title + " was published in " date}

{% endhighlight %}

Fixed:

{% highlight ruby %}

texts = {
	"Jane Eyre": "1847",    
	"Cane": "1923",    
	"Wide Sargasso Sea": "1966",    
	"Citizen: An American Lyrics": "2014"
}

for title, date in texts.items():
	print(title + " was published in " + date)

{% endhighlight %}

<hr/>

## String Cleaning

Create a list containing containing ten words, but make a few of them variant spellings of the same word. Write a program that looks through this list and makes a copy of the original list but with standardized spellings.

Broken:

{% highlight ruby %}

words =  ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']
canonical_spellings = ['color','amuck','adviser','pepper']

mappings = {'colour':'color','amok':'amuck','advisor':'adviser'}

new_list = []
for word in words:
	if word in mappings:
		new_list.append(mappings[word])
	else:
        		new_list.append(word)

print(new_list)

{% endhighlight %}

Fixed:

{% highlight ruby %}

words =  ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']
canonical_spellings = ['color','amuck','adviser','pepper']

mappings = ['colour':'color', amok:'amuck' 'advisor':'adviser']

new_list = []
for words in words:
	if word in mapping
		new_list.append(mappings[word])
	else:
        		new_list.append(word)

print new_list


{% endhighlight %}

<hr/>

## Scraping

We want to scrape a number of pages from my blog. In order to do that, we'll need a list of several URLs to point our Python program to. We know the name of each page we are interested in, and we know the top-level domain. Make a new list consisting of all the URLs we want by combining the two.
domain = 'http://walshbr.com/'
pages = ['about','blog','pedagogy','projects','cv']

Broken:

{% highlight ruby %}

domain = 'https://walshbr.gov/'
pages = [about,'blog','pedagogy';'projects' 'cv']

urls = {}

for thing in pages:
	url = domains + pages
	urls.add(url)

url

{% endhighlight %}

Fixed:

{% highlight ruby %}

domain = 'http://walshbr.com/'
pages = ['about','blog','pedagogy','projects','cv']

urls = []

for page in pages:
	url = domain + page
	urls.append(url)

urls

{% endhighlight %}

<hr/>
