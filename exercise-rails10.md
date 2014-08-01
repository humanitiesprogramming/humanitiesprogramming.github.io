---
layout: exercise
title: Rails App
description: Phase Ten - Adding User Comments
permalink: /exercises/rails-ten/
javascript:
  - /assets/js/catchup.js
---

One of the things you want to be able to do is engage your users with your
application. For this application, allowing people to comment on a
transcription can go a long way in helping you engage your audience. This also
shows off how to associate a model with another (a very common task in web
development).

## Comments

A comment need to be associated with a particular transcription, and a user. In
Rails, these associations are handled at the application layer. If you've done
any database development before, you may have handled this at the database
layer.

## Scaffold

We'll start by getting rails to create a scaffold for the comment, and add a
placeholder to reference the Transcription model (`transcription_id`).

{% highlight console %}
$ bin/rails generate scaffold Comment user_name:string body:text transcription:references
{% endhighlight %}

This generates the new files needed and updates *most* of the files for this to
work properly. The next step is to tell the database about the update

{% highlight console %}
$ rake db:migrate
== 20140730172249 CreateComments: migrating ===================================
-- create_table(:comments)
   -> 0.0052s
== 20140730172249 CreateComments: migrated (0.0053s) ==========================
{% endhighlight %}

## Model Relations

The association between a `Transcription` object and a `Comment` object is that
a `Transcription` **has many** `Comments`. We define this association in the
model. Open `app/models/transcription.rb`. Add the line `has_many :comments` to
the file.

{% highlight ruby %}
class Transcription < ActiveRecord::Base
  mount_uploader :picture, PictureUploader
  has_many :comments
end
{% endhighlight %}

We also want to make sure that the `Comment` model properly **belongs to** to
the `Transcription` object. Open `app/models/comment.rb` and make sure it looks
like this:

{% highlight ruby %}
class Comment < ActiveRecord::Base
  belongs_to :transcription
  validates :user_name, presence: true, length: { minimum: 2 }
end
{% endhighlight %}

## Render Comments

We need a form for adding comments, as well as updating the `Transcription`
controller to know how to save and display a comment. Open
`app/views/transcriptions/show.html.erb`.

{% highlight rhtml %}
<div class="row">
  <div class="col-md-12">
    <h3 class="page-header">Comments</h3>
  </div>
</div>

<% @comments.each do |comment| %>
<div class="row">
  <div class="md-col-10 col-md-offset-1">
    <div class="comment">
      <p><strong><%= comment.user_name %></strong></p>
      <%= simple_format comment.body %>
    </div>
  </div>
</div>
<% end %>

<%= render 'comments/form' %>
{% endhighlight %}

We also need to tell the `Transcription` controller about the comment. Open
`app/controllers/transcriptions_controller.rb` and add find the `show` method.
Update the method to read like this:

{% highlight ruby %}
def show
  @comments = @transcription.comments.all
  @comment = @transcription.comments.build
end
{% endhighlight %}

Now open the comment form (`app/views/comments/_form.html.erb`) and update the
styles:

{% highlight rhtml %}
<div class="row">
  <div class="md-col-12">
    <h2 class="page-header">New Comment</h2>
  </div>
</div>

<div class="row">
  <div class="md-col-4 col-md-offset-1">
    <%= form_for(@comment) do |f| %>
      <% if @comment.errors.any? %>
        <div id="error_explanation">
          <h2><%= pluralize(@comment.errors.count, "error") %> prohibited this comment from being saved:</h2>

          <ul>
          <% @comment.errors.full_messages.each do |message| %>
            <li><%= message %></li>
          <% end %>
          </ul>
        </div>
      <% end %>

      <%= f.hidden_field :transcription_id %>

      <div class="form-group">
        <%= f.label :user_name %><br>
        <%= f.text_field :user_name, class: "form-control", placeholder: "Your Name" %>
      </div>
      <div class="form-group">
        <%= f.label :body %><br>
        <%= f.text_area :body, class: "form-control", placeholder: "Comment", rows: 5 %>
      </div>

    <div class="actions">
      <%= f.submit "Save", class: "btn btn-default" %>
    </div>
  <% end %>
  </div>
</div>
{% endhighlight %}

## Flow
Try out your newly added feature. Notice anything annoying? Yeah, when you post
a comment, the `Comment` controller takes over and takes you to the `index`
view for the transcription. Let's update this action so when you add a new
comment, you go back to the transcription.

Open `app/controllers/comments_controller.rb` and find the `create` method.
Update it to read as follows:

{% highlight ruby %}
# POST /comments
# POST /comments.json
def create
  @comment = Comment.new(comment_params)
  @transcription = @comment.transcription

  respond_to do |format|
    if @comment.save
      format.html { redirect_to transcription_path(@transcription), notice: 'Comment was successfully created.' }
    else
      format.html { render :new }
      format.json { render json: @comment.errors, status: :unprocessable_entity }
    end
  end
end
{% endhighlight %}

## Git

Don't forget to add the new files and commit them in `git`, and also push them
to github!

{% highlight console %}
$ git add .
$ git commit -am "Implements comments on the Transcription"
$ git push origin master
{% endhighlight %}


## Summary

There's a lot of code here, but they're mainly updates to code that Rails
generated for you. Most of the "work" here is actually going to the [Bootstrap
documentation][boostrap] to add the appropriate HTML markup and CSS classes to
produce the desired layout. This exercise did get in to some of the specifics
of creating associated models in Rails that encapsolates different ideas that
are *hopefully* easy to reason about. You can now build out many more features
using these techniques.



[bootstrap]: http://getbootstrap.com/css/

