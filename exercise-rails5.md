---
layout: exercise
title: Rails App
description: Phase Five
permalink: /exercises/rails-five/
javascript:
  - /assets/js/catchup.js
---

In this module, we will refine the routes, or how the URLs in the
application act as well as creating a static page that contains info
about the **Scriba** application.

If you look at the [http://localhost:3000][t] webpage (with your server
running of course), what do you see? Instead of that file, let's tell
Rails to serve out our `transcriptions#index` view.

Stop your server (remember any changes to files in the `config`
directory require you to restart `rails`) and open `config/routes.rb`.
Update the root path (`root 'welcome#index`)

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
`rails` generator to create a new controller and view for us, but skip
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
for us, but no models. It also wrote to `config/routes.rb` a line to
tell `rails` how to access the code. Now we can update the file.

Open `app/views/pages/about.html.erb` and add some **lorem ipsum** (in
atom, simply type the word "lorem" and hit the tab key to add some dummy
text in a `<p>` element.

{% highlight rhtml %}
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
{% endhighlight %}

TODO: finish

## But we forgot the credits page...

No worries, we don't even have to jump in to the editor. 

- add method to controller
- create view

## Git

## Summary

[t]: http://localhost:3000/
