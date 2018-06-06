---
layout: page
title: Live Coding 2018
permalink: /resources/live-coding-2018/
---
```
curl https://humanitiesprogramming.github.io/eyre.txt
curl https://humanitiesprogramming.github.io/eyre.txt > eyre.txt

what happened?

type git status

open the file

we have a file!

full code at /resources/coding-2018.py

=====
filename="../eyre.txt"

with open(filename, 'r') as our_file:
    text = our_file.read()
    
print(text[0:100])
=====

import nltk

filename="../eyre.txt"

with open(filename, 'r') as our_file:
    text = our_file.read()

print(text[0:100])

words = nltk.word_tokenize(text)
print(words[0:10])
=====

import nltk

filename="../eyre.txt"

with open(filename, 'r') as our_file:
    text = our_file.read()

print(text[0:30])

words = nltk.word_tokenize(text)
print(words[0:10])
if "The" != "the":
    print("Case matters!")

clean_words = []
for word in words:
    clean_words.append(word.lower())
print(clean_words[0:30])
=====
#refactoring!

import nltk

def open_file_and_get_text(filename):
    with open(filename, 'r') as our_file:
        text = our_file.read()
    return text
    
print(text[0:30])

words = nltk.word_tokenize(text)
print(words[0:10])
if "The" != "the":
    print("Case matters!")

clean_words = []
for word in words:
    clean_words.append(word.lower())
print(clean_words[0:30])

filename="../eyre.txt"

=====
import nltk


def open_file_and_get_text(filename):
    with open(filename, 'r') as our_file:
        text = our_file.read()
    return text


def clean_tokens(raw_tokens):
    clean_words = []
    for word in words:
        clean_words.append(word.lower())
    return clean_words


# the actual stuff
filename="../eyre.txt"
text = open_file_and_get_text(filename)
print(text[0:30])

words = nltk.word_tokenize(text)
print(words[0:10])
if "The" != "the":
    print("Case matters!")

clean_words = clean_tokens(words)
print(clean_words[0:30])
=====
import nltk


def open_file_and_get_text(filename):
    with open(filename, 'r') as our_file:
        text = our_file.read()
    return text


def clean_tokens(raw_tokens):
    clean_words = []
    for word in words:
        clean_words.append(word.lower())
    return clean_words


# the actual stuff
filename="../eyre.txt"
text = open_file_and_get_text(filename)
print(text[0:30])

words = nltk.word_tokenize(text)
print(words[0:10])
if "The" != "the":
    print("Case matters!")

clean_words = clean_tokens(words)
print(clean_words[0:30])
word_counts = nltk.FreqDist(clean_words)
print(word_counts.most_common(10))
```