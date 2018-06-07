---
layout: page
title: Live Coding 2018
permalink: /resources/live-coding-2018/
---
Prep work
```
$ curl https://humanitiesprogramming.github.io/resourceseyre.txt
$ curl https://humanitiesprogramming.github.io/resourceseyre.txt > eyre.txt

what happened?

type git status

open the file

we have a file!
```

First steps - reading in a file
```
# take a filename and set it equal to filename
filename="eyre.txt"

# open a file, read it, set it equal to text
with open(filename, 'r') as our_file:
    text = our_file.read()

# print the first 100 characters
print(text[0:100])
```

Using NLTK for the first time - tokenizing
```

import nltk

# take a filename and set it equal to filename
filename="eyre.txt"

# open a file, read it, set it equal to text
with open(filename, 'r') as our_file:
    text = our_file.read()

# print the first 100 characters
print(text[0:100])

# use nltk to tokenize the text and print out the first words
words = nltk.word_tokenize(text)
print(words[0:10])
```

Using a loop to lowercase all the words.
```
import nltk

# take a filename and set it equal to filename
filename="eyre.txt"

# open a file, read it, set it equal to text
with open(filename, 'r') as our_file:
    text = our_file.read()

# print out the first characters of the text
print(text[0:30])

# tokenize the text and print out the first several words
words = nltk.word_tokenize(text)
print(words[0:10])
# prove that case matters
if "The" != "the":
    print("Case matters!")

# initialize an empty list, clean_words
clean_words = []
# build up the clean_words list by lowercasing all of the words we had
for word in words:
    clean_words.append(word.lower())
# print the first several
print(clean_words[0:30])
```

Refactoring things to make them more organized

```
#refactoring!

import nltk

def open_file_and_get_text(filename):
    # open a file, read it, set it equal to text
    with open(filename, 'r') as our_file:
        text = our_file.read()
    return text

# take a filename and set it equal to filename    
filename="eyre.txt"
text = open_and_get_text(filename)
print(text[0:30])

# tokenize the text and print out the first several words
words = nltk.word_tokenize(text)
print(words[0:10])
# prove that case matters
if "The" != "the":
    print("Case matters!")

# initialize an empty list, clean_words
clean_words = []
# build up the clean_words list by lowercasing all of the words we had
for word in words:
    clean_words.append(word.lower())
print(clean_words[0:30])

```

Refactoring for a second time.
```
import nltk


def open_file_and_get_text(filename):
    # open a file, read it, set it equal to text
    with open(filename, 'r') as our_file:
        text = our_file.read()
    return text


def clean_tokens(raw_tokens):
    # initialize an empty list, clean_words
    clean_words = []
    # build up the clean_words list by lowercasing all of the words we had
    for word in words:
        clean_words.append(word.lower())
    return clean_words


# the actual stuff
# take a filename and set it equal to filename
filename="eyre.txt"
text = open_file_and_get_text(filename)
print(text[0:30])

# tokenize the text and print out the first several words
words = nltk.word_tokenize(text)
print(words[0:10])
# prove that case matters
if "The" != "the":
    print("Case matters!")

# clean the text and print out the first few words
clean_words = clean_tokens(words)
print(clean_words[0:30])
```

Adding a final vizualization
```
import nltk


def open_file_and_get_text(filename):
    # open a file, read it, set it equal to text
    with open(filename, 'r') as our_file:
        text = our_file.read()
    return text


def clean_tokens(raw_tokens):
    clean_words = []
    for word in words:
        clean_words.append(word.lower())
    return clean_words


# the actual stuff
# take a filename and set it equal to filename
filename="eyre.txt"
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
print(word_counts['she'])
nltk.Text(clean_words).dispersion_plot(['he', 'she', 'tony'])
```
Refactoring as a class!
```
# there is a package called nltk. load it for this file.
import nltk

class TonyClass:
    def __init__(self, filename):
        self.filename = filename
        self.text = self.open_file_and_get_text(self.filename)
        self.tokens = nltk.word_tokenize(self.text)
        self.clean_tokens = self.clean_tokens(self.tokens)
        self.word_counts = nltk.FreqDist(self.clean_tokens)

    def make_the_plot(self, clean_tokens):
        nltk.Text(clean_words).dispersion_plot(['he', 'she', 'jane', 'tony'])

    def open_file_and_get_text(self, filename):
        # given a filename, open it.
        with open(filename, 'r') as our_file:
            # takes the the file and reads the text. Stores it.
            text = our_file.read()
        return text

    def clean_tokens(self, words):
        # given some tokens, lowercase them all.
        # create an empty list called clean_words
        clean_words = []

        # loop over every word item in the words list
        for word in words:
            # make each word lowercase and append it to the new list.
            clean_words.append(word.lower())
        return clean_words

# To actually run this, go into your python interpreter from within the same folder as this script. Import our own script
# $ python3
# >>> import eyre
# >>> our_text = TonyClass(ourfile)
# then we can access all of the stuff we've wrapped up in this package like so:
# >>> our_text.clean_tokens
# >>> our_text.tokens
```
