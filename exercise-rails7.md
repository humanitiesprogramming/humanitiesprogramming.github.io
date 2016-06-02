---
layout: exercise
title: Rails App
description: Phase Seven - Adding Users
permalink: /exercises/rails-seven/
javascript:
  - /assets/js/catchup.js
---

Users are important for your application as they'll be contributing the data.
We need to make sure this is as simple for users to contribute as possible, but
keep track of individual users.

## Devise
For this exercise, we'll be using the `devise` gem to manage user
authentication for us. First we need to add the gem dependency to the `Gemfile`

{% highlight ruby %}
gem 'devise', '~> 3.4.0'
{% endhighlight %}

And then install the new dependencies.

{% highlight console %}
$ bundle install
{% endhighlight %}

## Set Up Devise

Devise has it's own generators that it adds to Rails. We need to run the
install generator for devise. Run the following in the terminal:

{% highlight console %}
$ rails g devise:install
    create  config/initializers/devise.rb
    create  config/locales/devise.en.yml
{% endhighlight %}

You'll notice a bunch of messages also in the console after you've run the
installer.  This provides further information about how to configure your
application to work
with Devise.

First, we need the default URL options for the development environment. Open
`config/environments/development.rb` and add this line before the `end`
keyword:

{% highlight ruby %}
config.action_mailer.default_url_options = { :host => 'localhost:3000' }
{% endhighlight %}

{% gist waynegraham/07e799c3aca31f4739ae %}

Now we need to edit the application view to hold an alert for us. Edit
`app/views/layouts/application.html.erb` and add the following just before
the line that reads `<%= yield %>`.

{% highlight rhtml %}
<% flash.each do |name, msg| %>
  <% if msg.is_a?(String) %>
    <div class="alert alert-<%= name.to_s == 'notice' ? 'success' : 'danger' %>">
      <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
      <%= content_tag :div, msg, :id => "flash_#{name}" %>
    </div>
  <% end %>
<% end %>
{% endhighlight %}

Now we can clean up some of the code. Since we put this on the global
application layout, we can remove the `notice` elements in the `show` views.
Open `app/views/transcriptions/show.html.erb` and remove the line that reads
`<p id="notice"><%= notice %></p>`.

## User Model

We need to tell the database about the **User** model to store information
about the application's users.

{% highlight console %}
$ rails g devise user
      invoke  active_record
      create    db/migrate/20140719205623_devise_create_users.rb
      create    app/models/user.rb
      invoke    test_unit
      create      test/models/user_test.rb
      create      test/fixtures/users.yml
      insert    app/models/user.rb
       route  devise_for :users
$ rake db:migrate
== 20140719205623 DeviseCreateUsers: migrating ================================
-- create_table(:users)
   -> 0.0055s
-- add_index(:users, :email, {:unique=>true})
   -> 0.0010s
-- add_index(:users, :reset_password_token, {:unique=>true})
   -> 0.0004s
== 20140719205623 DeviseCreateUsers: migrated (0.0070s) =======================
{% endhighlight %}

This sets up the basic table structure for devise to store user account
information.  If you look at the migration that was created, you'll notice that
you can configure Devise to do all kinds of things. For our purposes today, the
defaults are fine, but just make a mental note that this is configurable.


## Create a User

Start your Rails server (`bin/rails server`) and navigate to
[http://localhost:3000/users/sign_up](http://localhost:3000/users/sign_up) and create
a new user for your application.

What happens?

## Log In Link

We don't want our users to have to guess what the URL for signing in/up is, so
let's add a link. 

In `app/views/layouts/application.html.erb`, under the line

{% highlight rhtml %}
<li class="active">
  <%= link_to "Transcriptions", transcriptions_path %>
</li>
{% endhighlight %}

add:

{% highlight rhtml %}
<li>
  <p class="navbar-text pull-right">
    <% if user_signed_in? %>
      Logged in as <strong><%= current_user.email %></strong>.
      <%= link_to 'Edit profile', edit_user_registration_path, :class => 'navbar-link' %> |
      <%= link_to "Logout", destroy_user_session_path, method: :delete, :class => 'navbar-link'  %>
    <% else %>
      <%= link_to "Sign up", new_user_registration_path, :class => 'navbar-link'  %> |
      <%= link_to "Login", new_user_session_path, :class => 'navbar-link'  %>
    <% end %>
  </p>
</li>
{% endhighlight %}

This will add the links for "Sign up | Login" when the user isn't logged in.

![Login]({{ "/assets/img/exercises/rails7/navigation.png" | prepend: site.baseurl  }}){: .img-responsive}

What's different when the user is logged in?

# One last thing...

We want to force people who are using the app to log in, but only if they attempt
to add, or modify, an existing transcription. Open
`app/controllers/transcription_controller.rb` and add this line (after
`before_action :set_transcription, only: [:show, :edit, :update, :destroy]`).

{% highlight ruby %}
before_action :authenticate_user!, only: [:edit, :update, :destroy]
{% endhighlight %}

This will force a user to authenticate if they edit, update, or destroy
(delete) a transcription from the application.

Why might this be a good idea?

# Git

Now that there's a new feature, it's a good time to commit the new code to git.
Since this is a full feature, it's a good idea to make sure you have a good
commit message.

## Adding Gravatars

A nice addition to showing user names is to use an avatar. For our application,
we can use the service that [Gravatar](http://gravatar.com/) provides. This
service matches user email addresses with an avatar picture of their choosing,
with several default images for those who have not yet configured an image.

If you don't already have a [Gravatar](http://gravatar.com/) account, head over
and set one up.

We can use the `gravtastic` gem to make this quite easy. In your `Gemfile` add
the following dependency (under `devise`).

{% highlight ruby %}
gem 'gravtastic', '~> 3.2.6'
{% endhighlight %}

Then in the terminal, install the dependency (`bundle install`).

### Gravtastic Mixin

We need to let the `User` model know to include the mixin for creating Gravatar
URLs. Open `app/models/user.rb` and add the following after the first line:

{% highlight ruby %}
include Gravtastic
gravtastic
{% endhighlight %}

### The Image

We need to update the application layout to include the image for users who
have logged in. Open `app/views/layouts/application.html.erb` and find the
section that starts with `<% if user_signed_in? %>` and add this line:

{% highlight rhtml %}
<%= image_tag current_user.gravatar_url %>
{% endhighlight %}

If you reload your page (and are logged in), you should now see the gravatar
associated with the email for that user.

Feel free to play around with the placement of the image, but do you notice
anything you might like to change about the image? How can you adjust the CSS here to make things look more aesthetically pleasing and usable?

## What time is it?

That's right, it's time to add and commit the changes to git. It's also a
good time to push to the Github remote (just in case your computer fails). We
can also close the open issue (should be #1). Be sure to add "closes #1" to
your commit message.

## Summary

In this module we added users and a complete backend for managing users for the
application. This allows you to manage authentication, but remember
authorization is something different. We also added images from the gravatar
service, which help give your site a more personal feel.
