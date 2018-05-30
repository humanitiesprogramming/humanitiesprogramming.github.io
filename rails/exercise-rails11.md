---
layout: exercise
title: Rails App
description: Phase Eleven - Deploying Your Application
permalink: /exercises/rails-eleven/
javascript:
  - /assets/js/catchup.js
---

One of the more complicated tasks in the lifecycle of an application is getting
it on a server for people to look at. This can be a rather complex task, but we
will use a service that is specifically designed to make this a relatively
painless task.

The [Heroku][heroku] service is a **platform**
that allows you to run web applications written in most of the popular web
languages.

## Setup

For this, we need to follow the [Heroku Quickstart Guide][quickstart]'s instructions to install the Heroku toolbelt and login from the command line.

## Prepping Scriba

Heroku works with git, which makes deploying a snap. However, there are a few
things we need to do to make this work better.

### Ignore Files

We need to tell git to ignore certain files. Specifically files that are
updated though the server (e.g. the log files and image uploads). For this we
need to edit a special file `.gitignore`. You can do this in an editor, or for
fun, you can do it through the console. Remember what the **echo** command does? What about **>>**?

{% highlight console %}
$ echo "public/uploads" >> .gitignore
$ echo "tmp" >> .gitignore
$ echo "longer" >> .gitignore
$ git commit -am "Ignore files not needed for deployment"
{% endhighlight %}

Open .gitignore in your text editor after all is said and done. Notice anything? Most of these files were probably already included in the .gitignore file that rails generated for you. This won't cause any problems, but you might want to clean out the extra lines.

### Database Configuration

We have been using a database system in our default Rails application called
SQLite. However, Heroku uses a far more robust system called PostgreSQL. If we
deployed our application as is, we'll run in to problems since our application
doesn't know how to "talk" to a PostgreSQL server. We need to tell Rails about
this dependency in our production environment by updating the `Gemfile`.

Find the line that reads `gem 'sqlite3'` and update it to look like this:

{% highlight ruby %}
group :development do
  gem 'sqlite3'
end

group :production do
  gem 'pg'
end
{% endhighlight %}

This tells our application to use one database in development and another in production (when it is running up on Heroku). These sorts of nuances can be very useful when you want to test and run different things while debugging and developing than on your live site.

### 12 Factor

Heroku requires applications to adhere to [Twelve-Factor
App](http://12factor.net/) principals. To make this easier for you, there's a
gem that will configure your application in production to adhere to these
principals. All we need to do is add the `rails_12factor` gem to the production
environment in the `Gemfile`. Update the `:production` group as follows.

{% highlight ruby %}
group :production do
  gem 'pg'
  gem 'rails_12factor'
end
{% endhighlight %}

Now you can update the dependencies, but we can run only what we need in
development with the following:

{% highlight console %}
$ bundle install --without production
{% endhighlight %}

Now, **add** and **commit** the updated `Gemfile` and `Gemfile.lock`.

### Web Server

By default, you web application runs through a web server named Webrick. This
is a great server in a development environment, but is really horrible as a
server in production environments. Heroku enourages you to use
[Unicorn][unicorn]. We don't need to do this right now, but if you want to
continue developing this application, this is something you will want to do.

## Deploying Your App

To create a new application on heroku (assuming you installed the [heroku
toolbelt][toolbelt]) with the `heroku create` command.

{% highlight console %}
$ heroku create
Creating shielded-temple-5358... done, stack is cedar
http://shielded-temple-5358.herokuapp.com/ | git@heroku.com:shielded-temple-5358.git
Git remote heroku added
{% endhighlight %}

In my case, my app is named **shielded-temple-5358**. Part of this setup is
that we have a new git remote named *heroku*. To see what remotes you have for your project, remember that you can type **git remote -v**.

Now we can push the **master**
branch to this remote.

{% highlight console %}
$ git push heroku master
Initializing repository, done.
Counting objects: 277, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (257/257), done.
Writing objects: 100% (277/277), 46.21 KiB | 0 bytes/s, done.
Total 277 (delta 119), reused 0 (delta 0)

-----> Ruby app detected
-----> Compiling Ruby/Rails
-----> Using Ruby version: ruby-2.0.0
-----> Installing dependencies using 1.6.3
       Running: bundle install --without development:test --path vendor/bundle --binstubs vendor/bundle/bin -j4 --deployment
       Fetching gem metadata from https://rubygems.org/..........
       Fetching additional metadata from https://rubygems.org/..
       ...
       Bundle completed (23.42s)
       Cleaning up the bundler cache.
-----> Preparing app for Rails asset pipeline
       Running: rake assets:precompile
       I, [2014-08-01T13:26:28.837146 #1055]  INFO -- : Writing /tmp/build_773a12b8-29a6-4f50-b9bf-532c14eba8dc/public/assets/application-c23ffbdd24d84fb51367f46fe4f80265.js
       I, [2014-08-01T13:26:28.902130 #1055]  INFO -- : Writing /tmp/build_773a12b8-29a6-4f50-b9bf-532c14eba8dc/public/assets/application-8d28fbaea5f9f776a348eec2dacde8c6.css
       Asset precompilation completed (7.42s)
       Cleaning assets
       Running: rake assets:clean

###### WARNING:
       You have not declared a Ruby version in your Gemfile.
       To set your Ruby version add this line to your Gemfile:
       ruby '2.0.0'
       # See https://devcenter.heroku.com/articles/ruby-versions for more information.

###### WARNING:
       No Procfile detected, using the default web server (webrick)
       https://devcenter.heroku.com/articles/ruby-default-web-server

-----> Discovering process types
       Procfile declares types -> (none)
       Default types for Ruby  -> console, rake, web, worker

-----> Compressing... done, 21.5MB
-----> Launching... done, v6
       http://shielded-temple-5358.herokuapp.com/ deployed to Heroku

To git@heroku.com:shielded-temple-5358.git
 * [new branch]      master -> master
{% endhighlight %}

You'll know you're done when you see the "**Launching...**" text in the console.

### Database Migration
We also need to migrate the database. We do this by telling heroku to run the
`rake db:migrate` task.

{% highlight console %}
$ heroku run rake db:migrate
Running `rake db:migrate` attached to terminal... up, run.4973
== 20140627192049 CreateTranscriptions: migrating =============================
-- create_table(:transcriptions)
   -> 0.0786s
== 20140627192049 CreateTranscriptions: migrated (0.0788s) ====================

== 20140719205623 DeviseCreateUsers: migrating ================================
-- create_table(:users)
   -> 0.0809s
-- add_index(:users, :email, {:unique=>true})
   -> 0.0398s
-- add_index(:users, :reset_password_token, {:unique=>true})
   -> 0.0283s
== 20140719205623 DeviseCreateUsers: migrated (0.1497s) =======================

== 20140730172249 CreateComments: migrating ===================================
-- create_table(:comments)
   -> 0.0820s
== 20140730172249 CreateComments: migrated (0.0822s) ==========================
{% endhighlight %}

### Check it out
The simplest way to get to your application is from the terminal and typing
`heroku open`. Is it working?

## Plugins
A few things to note, Heroku is a cloud platform with no persistant storage. If
you read the Heroku notes, you'll see the following:

> Each dyno gets its own ephemeral filesystem, with a fresh copy of the most recently deployed code. During the dyno’s lifetime its running processes can use the filesystem as a temporary scratchpad, but no files that are written are visible to processes in any other dyno and any files written will be discarded the moment the dyno is stopped or restarted.

You can do an experiment here; go to your application and upload a new
transcription image. Then, in the console, run `heroku restart` to restart your
application. If you go back to the web page, your image should no longer be
visible.

A common approach to this is to use a service like [Amazon S3][s3] (Simple
Storage Service) or [Rackspace CloudFiles][cloudfiles]. This is relatively
inexpensive (generally less than $0.10/GB) and provides you a method to save
your media uploads.

We wont' get in to this here either, but again, if you want to go further with
this application, here are some useful links for implementing this:

* [How to Make Carrierwave work on Heroku](https://github.com/carrierwaveuploader/carrierwave/wiki/How-to%3A-Make-Carrierwave-work-on-Heroku)
* [Amazon S3 &ndash; The Beginner's Guide](http://www.hongkiat.com/blog/amazon-s3-the-beginners-guide/)

## Summary
You now have an application you can share with your friends and family. And,
without getting into a "back in my day" talk, this is one of the simplest
ways to deploy an application, but it's not the only way. Similar services to
heroku (if you don't have your own IT staff) include:

* [OpenShift](https://www.openshift.com/)
* [TruckerIO](http://developers.trucker.io/Getting-Started)

[heroku]: http://heroku.com
[quickstart]: https://devcenter.heroku.com/articles/quickstart
[unicorn]: https://devcenter.heroku.com/articles/rails-unicorn
[toolbelt]: https://toolbelt.heroku.com/
[s3]: http://aws.amazon.com/s3/
[cloudfiles]: http://www.rackspace.com/cloud/files/
