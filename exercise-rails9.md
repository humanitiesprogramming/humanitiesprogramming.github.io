---
layout: exercise
title: Rails App
description: Phase Nine - User Experience
permalink: /exercises/rails-nine/
javascript:
  - /assets/js/catchup.js
---

Now that we have fancy tricks to make awesome CSS, let's take a look at the
interface and update it a bit. While we can make our own, let's use as much of
the Twitter Bootstrap styles as we can.

## Transcriptions Page

Right now the transcriptions are in a table with a cell for every property of
the object. One way to make this easier to navigate would be to make each image
the primary visual for the page in a grid. We can do this with some helpers
Rails provides, as well as some styles that Bootstrap provides. Open
`app/views/transcriptions/index.html.erb`. We want to update the file to first
use Bootstrap's layout options, specifically the idea of **rows** and
**columns**.

{% highlight rhtml %}
<div class="row">
  <h1>Transcriptions</h1>

  <p>
    <%= link_to 'New Transcription', new_transcription_path, :class => "btn btn-large btn-primary" %>
  </p>
</div>

<% @transcriptions.in_groups_of(3) do |group| %>
<div class="row">
  <% group.compact.each do |transcription| %>
    <div class="col-xs-6 col-md-4">
      <div class="thumbnail">
        <%= link_to(image_tag(transcription.picture_url(:thumb)), transcription_path(transcription)) if transcription.picture.present? %>
        <div class="caption">
          <h3><%= transcription.title %></h3>
          <p><%= truncate(transcription.description, length: 250) %></p>
          <p>
            <%= link_to 'Edit', edit_transcription_path(transcription), :class => "btn btn-mini btn-primary" %>
            <%= link_to 'Destroy', transcription, method: :delete, data: { confirm: 'Are you sure?' }, :class => "btn btn-mini btn-danger" %>
          </p>
        </div>
      </div>
    </div>
  <% end %>
</div>
<% end %>
{% endhighlight %}

Before you start your server back up, what do you expect to happen? How should
this be different? How many different helper methods are getting used here?

## Show View

The `transcription#show` view needs some work too. We can make this look a lot
better, separating the metadata (title and description) from the actual content
(image and transcription). We can also update the notice (for when a new item
has been created, or a current item has been updated). Open
`app/views/transcription/show.html.erb` and replace with the following:

{% highlight rhtml %}
<% unless notice.nil? %>
<div class="row">
  <div class="col-md-12">
    <p id="notice" class="alert alert-info" role="alert">
      <button type="button" class="close" data-dismiss="alert">
        <span aria-hidden="true">&times;</span><span class="sr-only">Close</span>
      </button>
      <%= notice %>
    </p>
  </div>
</div>
<% end %>

<div class="row">
  <div class="col-md-12">
    <h1><%= @transcription.title %></h1>
    <h2>Description:</h2>
    <p>
      <%= @transcription.description %>
    </p>
  </div>
</div>

<div class="row">
  <div class="col-md-6">
    <h3>Picture</h3>
    <p>
      <%= image_tag(@transcription.picture_url, class: "img-responsive") if @transcription.picture.present? %>
    </p>
  </div>

  <div class="col-md-6">
    <h3>Transcription</h3>
    <%= simple_format @transcription.transcription %>
  </div>
</div>

<div class="row">
  <%= link_to 'Edit', edit_transcription_path(@transcription), class: "btn btn-primary" %>
  <%= link_to 'Back', transcriptions_path, class: "btn btn-success" %>
</div>
{% endhighlight %}

Ok, hands off the keyboard. What is going on here? What is `simple_format`?
What is the `unless notice.nil?` doing at the top? Why is there all that
additional markup around the notice?

## Forms

Let's take a look at the `form` partial for transcriptions. Open
`app/views/transcriptions/_form.html.erb` and make it read as follows:

{% highlight rhtml %}
<div class="row">
  <div class="col-md-12">
    <%= form_for(@transcription, :html => {:multipart => true}, :role => 'form') do |f| %>
      <% if @transcription.errors.any? %>
        <div id="error_explanation">
          <h2><%= pluralize(@transcription.errors.count, "error") %> prohibited this transcription from being saved:</h2>

          <ul>
          <% @transcription.errors.full_messages.each do |message| %>
            <li class="alert alert-warning"><%= message %></li>
          <% end %>
          </ul>
        </div>
      <% end %>

      <div class="form-group">
        <%= f.label :title %><br>
        <%= f.text_field :title, class: "form-control", placeholder: "Document Title" %>
      </div>
      <div class="form-group">
        <%= f.label :description %><br>
        <%= f.text_area :description, class: "form-control", placeholder: "Document Description" %>
      </div>
      <div class="form-group">
        <%= f.label :picture %><br>
        <%= f.file_field :picture %>
        <p class="help-block">Image for document.</p>
      </div>
      <div class="actions">
        <%= f.submit "Save", class: "btn btn-default" %>
      </div>
    <% end %>
  </div>
</div>
{% endhighlight %}

This code adds HTML 5 placeholders to the form fields. Anything else
interesting going on here? Go back to your browser and add a new transcription,
then edit it. Does this feel right?

You may notice that in the `transcription#edit` view, you never actually see
the image, you can only ever upload a new image. We need a new view for this.
For now, let's make a new partial that will allow users to edit the title,
description, but see the image that was uploaded to create a transcription.

Create a new file `app/views/transcriptions/_edit_form.html.erb` and add the
following:

{% highlight rhtml %}
<%= form_for(@transcription, :html => {:multipart => true}, :role => 'form') do |f| %>
  <div class="row">
    <% if @transcription.errors.any? %>
      <div id="error_explanation">
        <h2><%= pluralize(@transcription.errors.count, "error") %> prohibited this transcription from being saved:</h2>

        <ul>
        <% @transcription.errors.full_messages.each do |message| %>
          <li class="alert alert-warning"><%= message %></li>
        <% end %>
        </ul>
      </div>
    <% end %>
  </div>

  <div class="row">
    <div class="form-group">
      <%= f.label :title %><br>
      <%= f.text_field :title, class: "form-control", placeholder: "Document Title", required: true %>
    </div>
    <div class="form-group">
      <%= f.label :description %><br>
      <%= f.text_area :description, class: "form-control", placeholder: "Document Description" %>
    </div>
  </div>

  <div class="row">
    <div class="col-md-6">
      <div class="form-group">
        <% if @transcription.picture.present? %>
          <%= image_tag(@transcription.picture_url, class: "img-responsive") %>
        <% else %>
          <%= f.label :picture %><br>
          <%= f.file_field :picture %>
        <% end %>
      </div>
    </div>
    <div class="col-md-6">
      <div class="form-group">
        <%= f.label :transcription %><br>
        <%= f.text_area :transcription, class: "form-control", placeholder: "Transcription", rows: 30 %>
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-md-6">
      <div class="actions">
        <%= f.submit "Save", class: "btn btn-default" %>
      </div>
    </div>
  </div>
<% end %>
{% endhighlight %}

If you look at the view code for `transcriptions#new` and
`transcriptions#edit`, you'll notice they both include the partial `form`.

{% highlight rhtml %}
<%= render 'form' %>
{% endhighlight %}

We need to update `app/views/transcription/edit.html.erb` to render the
`edit_form` partial:

{% highlight rhtml %}
<%= render 'edit_form' %>
{% endhighlight %}

It's time to explore your application a bit. Are there other things you could
do to make the application easier to navigate?


> Have you forgotten anything at this point? Starts with **G**, rhymes with
> **hit**...

## Summary
In this exercise, we implemented some basic styles that the Twitter Bootstrap
framework provides. In many projects, the design process takes as much (if not
more) time to get to a point where the front-end is thought through to ensure
users can perform the intended actions of an application with little (or no)
help from you, the developer. If you're interested in this component of the
software lifecycle, I would encourage you to consider taking the
[Introduction to Web Development and Design Principals][design] course.

[design]: http://www.dhtraining.org/hilt/course/introduction-to-web-development-design-and-principles/

