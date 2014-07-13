---
layout: exercise
title: Rails App - Creating a New App
description: Phase One
permalink: /exercises/rails-one/
---

# Creating a New Application

We're going to create a new Rails application named *scriba*. First we
need to createa a `projects` directory. Don't forget about the [Rails
Beginner Cheatsheet](http://www.pragtob.info/rails-beginner-cheatsheet/)
in case you get stuck.

## Install Rails

The first thing we need to do is ensure that the `rails` gem is
installed on the system. Open your terminal and install the gem:

{% highlight console %}
$ gem install rails
{% endhighlight %}

There are a lot of dependencies, so this could take a few minutes.

## Create Projects

Now we can start setting up the project. Create a `projects` directory
that will contain all of your web application projects.

{% highlight console %}
$ mkdir -p ~/projects
{% endhighlight %}

Verify that the `projects` directory was created by running the **list**
command. You should see the new directory in the output. Once you verify
that the directory is there, you can **change the directory** to
`projects`.

{% highlight console %}
$ ls
$ cd project
{% endhighlight %}

## Create New Rails Application

Now we're ready to create a new Rails application. We do this by running
the `rails` command, giving it a name for the project.

{% highlight console %}
$ rails new scriba
{% endhighlight %}

There will be a lot of output as Rails generates the files needed for
your application. Once finished, **change directories** in to the new
`scriba` directory.

{% highlight console %}
$ ls
$ cd scriba
{% endhighlight %}

Now that we're here, **list** what's in the directories. You should see
directories like `app` and `config`. This is where all of the files
Rails needs to work are located. Before we start working on anything,
let's make sure that the application is working. We can start the
included web server with this command:

{% highlight console %}
$ bin/rails server
{% endhighlight %}

Open your web browser to [http://localhost:3000](http://localhost:3000).
You should see something along these lines.

![Welcome Abort]({{ "/assets/img/exercises/rails-one/rails-default.png" | prepend: site.baseurl }})

When you are ready to **stop** the server, hit the `ctrl` and `c` keys
at the same time.

## Git

Now that we have something that is working, it is a good time to get
everything we have in `git`. We first need to initialize the repository,
then add the generated files, the commit them with a message about what
we did so far.

{% highlight console %}
$ git status
...
$ git add .
$ git commit -m "Generated initial rails application"
{% endhighlight %}

## Summary

Congratulations! You just created your first Rails application. It
doesn't do much (yet), but is a fully functioning Rails application. In
the next module we'll talk a bit about what the pieces of a Rails
application are, and how to start making the application do what we need
it to.

