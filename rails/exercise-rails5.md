---
layout: exercise
title: Rails App
description: Phase Five - Routes &amp; Static Pages
permalink: /exercises/rails-five/
javascript:
  - /assets/js/catchup.js
---

In this module, we will refine the routes, or how the URLs in the
application act, as well as create a static page that contains info
about the **Scriba** application.

If you look at the http://localhost:3000 webpage (with your server
running of course), what do you see? Instead of that file, let's tell
Rails to serve out our `transcriptions#index` view.

Stop your server (remember, any changes to files in the `config`
directory require you to restart `rails`) and open `config/routes.rb`.
Update the root path (`root 'welcome#index'`)

{% highlight ruby %}
Rails.application.routes.draw do
  resources :transcriptions
  ...
  root 'transcriptions#index'
  ...
end
{% endhighlight %}

What happens now if you start your web server back up?

While we're at it, this actually added a new *path* in `rails` for us to
use&mdash;the `root_path`. We can use this in the application layout to
return people to the defined `root` of the project. Open up
`app/views/layouts/application.html.erb` and find the line

{% highlight rhtml %}
<%= link_to "Scriba", transcriptions_path, class: 'navbar-brand' %>
{% endhighlight %}

And update it to:

{% highlight rhtml %}
<%= link_to "Scriba", root_path, class: 'navbar-brand' %>
{% endhighlight %}

If you ever need to check the routes you have defined in your
application, you can check them by running the `bin/rake routes` task.

> Now when you restart the server, what happens when you click on the
> "Scriba" link? How is it different than when you click on
> "Transcriptions"?

## A Static Page

Another common task you will find yourself needing to do is create
content that is **static** (not saved to the database). We'll use a
`rails` generator to create a new controller and view for us but skip
creating a model (and database migration).

{% highlight console %}
$ bin/rails generate controller pages about
      create  app/controllers/pages_controller.rb
       route  get 'pages/about'
      invoke  erb
      create    app/views/pages
      create    app/views/pages/about.html.erb
      invoke  test_unit
      create    test/controllers/pages_controller_test.rb
      invoke  helper
      create    app/helpers/pages_helper.rb
      invoke    test_unit
      create      test/helpers/pages_helper_test.rb
      invoke  assets
      invoke    coffee
      create      app/assets/javascripts/pages.js.coffee
      invoke    scss
      create      app/assets/stylesheets/pages.css.scss
{% endhighlight %}

As you can see from the output, this generated views, tests, and helpers
for us but no models. It also wrote to `config/routes.rb` a line to
tell `rails` how to access the code. Now we can update the file.

Open `app/views/pages/about.html.erb` and add some **lorem ipsum** (in
Atom, simply type the word "**lorem**" and hit the tab key) text in a `<p>`
element.

{% highlight rhtml %}
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
{% endhighlight %}

Now if your server is still running, you can get to the new page at
http://localhost:3000/pages/about.

## Better Routes
When we ran the generator for the controller, one of the things it did for us
was create a new entry in the `config/routes.rb` file. The entry `get
'pages/about'` tells rails what to do when a particular *path* is requested.
Right now it's a bit of an "ugly" URL since to get here you have to have the
word "pages" in them. Let's make this look a bit better by updating the
`config/routes.rb` file so there is a path defined as `/about`.

Under the line `get 'pages/about' in the `config/routes.rb` file, add the line

{% highlight ruby %}
get 'about', to: 'pages#about'
{% endhighlight %}

Restart your server, you should be able to see the same page at
http://localhost:3000/about.

## But we forgot the credits page...

No worries, we don't even have to use the console. We'll do this manually. To
do this, we need to update the `pages` controller (to tell rails what to do),
update the routes (to define what to do), and finally, the actual view with the
information.

Let's work with the controller first. We need to add a simple method that
defines what to do. We don't need to do anything, but we still need to define
this. Simply add this code to `app/controllers/pages_controller`.

{% highlight ruby %}
def credit
end
{% endhighlight %}

Now we can add the route. Open `config/routes.rb` and try create a route for
`pages#credit` (think about it for a second).

Now we need to create a new view file. Create the file
`app/views/pages/credit.html.erb`. In it, create some dummy credits.

{% highlight rhtml %}
<h1>Credits</h1>
<p>This application was created by me, for this thing I did.</p>
<p>Some other people helped too.</p>
{% endhighlight %}

## Git
Now that everything is working, it's time to add and commit everything to git.
Go ahead and add the new files, and commit them all with a "good" message.

## Summary
In this module, we created a static pages for our application that don't
necessarily need to be stored in a database. We used both the rails generator
and did this manually. You also learned a bit more about how routes work and
also how to create custom routes to make the URLs of your application easier to
"guess" by users.
