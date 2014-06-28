---
layout: exercise
title: Command Line
description: Command line exercises
permalink: /exercises/command-line/
javascript:
  - /assets/js/hint.js
---

![Drag Folder](http://media.24ways.org/2013/coyier/drag-folder.gif)

# Listing Directories

Change to the desktop. List all the directories on the Desktop

{% highlight console %}
$ cd ~/Desktop
$ ls -d */
{% endhighlight %}

# More Listing

Change to the desktop. List all files and directories, 1 per line.

{% highlight console %}
$ cd ~/Desktop
$ ls
{% endhighlight %}

# Making Directories

Create a directory named demo.

{% highlight console %}
$ mkdir demo
{% endhighlight %}

# Making Deep Directories

Change to the desktop. Create the following directory structure using one command: demo/foo/bar/praxis

{% highlight console %}
$ cd ~/Desktop
$ mkdir -p demo/foo/bar/praxis

{% endhighlight %}

# Creating Files

Change to the demo folder. Create a file named hello.txt in the demo directory.

 {% highlight console %}
$ cd ~/Desktop/demo
$ touch hello.txt
{% endhighlight %}

# Making, Moving, Deleting

Create a new folder called test_projects with three text files in it: test_1, test_2, test_3. Within test_projects, create another folder called files. Move the test files into the new directory. Move into the new directory to make sure it worked. Then delete the test_projects directory.

{% highlight console %}
$ mkdir test_projects
$ cd test_projects
$ touch test_1.txt
$ touch test_2.txt
$ touch test_3.txt
$ mkdir files
$ mv test_1 files
$ mv test_2 files
$ mv test_3 files
$ cd files
$ ls
$ cd ..
$ rmdir -rf test_projects
{% endhighlight %}
