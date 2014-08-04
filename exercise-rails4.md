---
layout: exercise
title: Rails App
description: Phase Four
permalink: /exercises/rails-four/
javascript:
  - /assets/js/catchup.js
---

Now that the application looks pretty good (you did resize your browser
to look at how it snaps at different sizes, right?), we can turn our
attention back to the functionality of the application. We have a field
for the picture, but right now it only is a text field. From a user's
perspective, this is pretty confusing. For our application, we want to
give users the ability to upload an image file to our application.

File uploads can get pretty complex quickly, so it's a good idea to look
at what solutions exist. Two very popular methods for working with file
uploads in Rails are [CarrierWave][carrierwave] and
[Paperclip][paperclip]. Each of these solutions does things slightly
differently, and for completely arbitrary reasons, we'll use CarrierWave
in this application.

## Libraries

The first thing we need to do is install the `carrierwave` gem. Open
your `Gemfile` in the text editor and add the this line:

{% highlight ruby %}
gem 'carrierwave'
{% endhighlight %}

Now that we've declared the dependency, we can install it with
`bundler`.

{% highlight console %}
$ bundle install
{% endhighlight %}

When CarrierWave is installed, it includes new generators for `rails` to
help us set up everything we need for the application. For our
application, we're going to add a new `uploader` named Picture.

{% highlight console %}
$ bin/rails generate uploader Picture
      create  app/uploaders/picture_uploader.rb
{% endhighlight %}

> **Note** If you ever want to see the generators that `rails` currently
> has access to, run the `bin/rails generate` command.

## Picture Uploader

We need to tell our `Transcription` model that it should treat the field
we created (`pictures`) through CarrierWave now. We need to edit
`app/models/transcription.rb` and make it read as so:

{% highlight ruby %}
class Transcription < ActiveRecord::Base
  mount_uploader :picture, PictureUploader
end
{% endhighlight %}

Now we need to change the form for the transcription. We have to change
the form to allow multiple types of content (e.g. text from the form, as
well as a file) as well as change the `picture` field to a **file** form
type.

Open the form **partial** (`app/views/transcriptions/_form.html.erb`).
We need the `form_for` line to read like this:

{% highlight rhtml %}
<%= form_for(@transcription, :html => {:multipart => true}) do |f| %>
{% endhighlight %}

Now we need to change the field type of `picture` from `text_field` to
`file_field`.

{% highlight rhtml %}
<div class="field">
  <%= f.label :picture %><br>
  <%= f.file_field :picture %>
</div>
{% endhighlight %}

When you start your server and add a new transcription, you should now
see a form that looks like this:

![File Upload]({{"/assets/img/exercises/rails-four/file-upload.png" | prepend: site.baseurl }}){: .img-responsive}

Try uploading a file now! Does it work? Click around, is it doing what
you expect?

## Git

Ok, so the file uploads are *functioning* (which is different than
*working*), so now is a good time to add and commit all of the new
files we've created.

{% highlight console %}
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   Gemfile
	modified:   Gemfile.lock
	modified:   app/models/transcription.rb
	modified:   app/views/transcriptions/_form.html.erb

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	app/uploaders/
$ git add app/uploaders
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   app/uploaders/picture_uploader.rb

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   Gemfile
	modified:   Gemfile.lock
	modified:   app/models/transcription.rb
	modified:   app/views/transcriptions/_form.html.erb
$ git commit -am "Added CarrierWave gem to handle file uploads"
[master 4b2bd53] Added CarrierWave gem to handle file uploads
 1 file changed, 51 insertions(+)
 create mode 100644 app/uploaders/picture_uploader.rb
{% endhighlight %}

## Show the Picture

Right now whenever we look at a view of the information (in the
`transcription#index` and `transcription#show` views), it simply
displays a string of the path to the image we've uploaded. Let's change
that to actually show the image.

Let's take care of the `transcription#show` view first. Open
`app/views/transcriptions/show.html.erb` and the line for the `picture`.
We need to update it to read like this:

{% highlight rhtml %}
<%= image_tag(@transcription.picture_url, :width => 600) if @transcription.picture.present? %>
{% endhighlight %}

Now if you refresh your browser, does the image show up? Do we have
access to any additional sizes of images (e.g. thumbnails)?

## Generating Derivatives

To create thumbnails of the images (and provide smaller assets for
different views), we need to create different image files. CarrierWave
doesn't do this directly, but provides access to two systems that do,
`RMagick` and `MiniMagick`. For CarrierWave, `MiniMagick` is
recommended, so we'll use that. This does require a system library named
[imagemagick][imagemagick] which is a Linux-based interface for working with image
files. First, let's install `imagemagick` with `homebrew`.

{% highlight console %}
$ brew install imagemagick
{% endhighlight %}

Now we need to add the `mini_magick` gem to the `Gemfile`.

{% highlight ruby %}
gem 'mini_magick', '~> 3.7.0'
{% endhighlight %}

And then install the gem.

{% highlight console %}
$ bundle
{% endhighlight %}

Now we need to take a closer look at the uploader CarrierWave generated.
Open the `app/uploaders/picture_uploader.rb` file.

There are a lot of lines commented out, and now we can uncomment some
that make sense for our app. We want to enable the `MiniMagick` mixin,
process the files that are updated and create thumbnails, as well as
limit the type of images that can be uploaded (e.g. no TIFFs). These are
slight changes to the file, so read these carefully.

{% highlight ruby %}
  ...
  include CarrierWave::MiniMagick
  ...

  # Process files as they are uploaded:
  process :resize_to_fit => [800, 800]

  ...

# Create different versions of your uploaded files:
  version :thumb do
    process :resize_to_fill => [200, 200]
  end

  # Add a white list of extensions which are allowed to be uploaded.
  # For images you might use something like this:
  def extension_white_list
    %w(jpg jpeg gif png)
  end
  ...
{% endhighlight %}

{% gist waynegraham/b75a355dbaeadd59303a %}

Now create a new transcription and add a new file. If you open the
`public/uploads/` directory, you should see two files in the latest
created file.

{% highlight console %}
$ ls -la public/uploads/transcription/picture/2/
{% endhighlight %}

Awesome, now we have access to the additional features from CarriewWave
to provide a thumbnail. We can use this in the `transcriptions.index`
view to show a thumbnail next to the title.

Open the `app/views/transcriptions/index.html.erb`. We can then update
the view table to use the thumbnail. We'll use the same `picture_url`
method, but pass the `:thumb` symbol to retrieve the thumbnail version.

{% highlight rhtml %}
<% @transcriptions.each do |transcription| %>
  <tr>
    <td><%= transcription.title %></td>
    <td><%= transcription.description %></td>
    <td><%= image_tag transcription.picture_url(:thumb) if transcription.picture.present? %></td>
    <td><%= link_to 'Show', transcription %></td>
    <td><%= link_to 'Edit', edit_transcription_path(transcription) %></td>
    <td><%= link_to 'Destroy', transcription, method: :delete, data: { confirm: 'Are you sure?' } %></td>
  </tr>
<% end %>
{% endhighlight %}

Start your server back up (if it's not running) and see what happens.
Are you seeing thumbnails for new items? What do you notice when you
upload an image?

> **Note**: In development you may, from time-to-time, need to reset
> your database and clear out test data. The easiest way to do this is
> with the `bin/rake db:reset` command. **NEVER DO THIS IN PRODUCTION!!!**

## Git

You may notice that there's a directory `public/uploads` that contains
your test data. We want to ignore these files (you don't want to have
different files on the "real" server). For this, we'll do some `git`
magick where we will include the parent directory (`public/uploads`) and
ignore the child directories. This way we can upload as much test stuff
as we want, without accidently pushing our test data to the production
machine.

The first thing we want to do is clear out the files that are in there,
and reset the database.

{% highlight console %}
$ rm -rf public/uploads
$ mkdir public/uploads
$ bin/rake db:reset
$ touch public/uploads/.gitkeep
$ git add public/uploads
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   public/uploads/.gitkeep
{% endhighlight %}

Next we need to add these directories to the `.gitignore` file. Open the
`.gitignore` file in your editor and add `public/uploads/` (the trailing
slash is important). Here's a fancy-smansy way to do it in the console:

{% highlight console %}
$ echo "public/uploads/" >> .gitignore
{% endhighlight %}


Now we can add and commit the rest of the changed files for this
feature.

{% highlight console %}
$ git commit -am "Add thumbnails for image uploads. Add local uploads to the ignore file."
[master 802fe88] Add thumbnails for image uploads. Add local uploads to the ignore file.
 7 files changed, 18 insertions(+), 11 deletions(-)
 create mode 100644 public/uploads/.gitkeep
{% endhighlight %}

## Summary
In this module we added the abiilty for "users" to upload their own
images for transcriptions and then have the system resize them for us.
There is a fair amount of processing going on in the background to save
the various images. We also updated the view to use these new images,
and tried our hands at some `git`-fu. The application is starting to
really come together now as a coherent application with expected user
interactions.

In the next module we'll take a step back and work on sharing this code
on Github and looking at workflow for managing these kinds of projects.

### Questions

* How many images get written each time a user uploads an image?


[carrierwave]: https://github.com/carrierwaveuploader/carrierwave
[paperclip]: https://github.com/thoughtbot/paperclip
[imagemagick]: http://www.imagemagick.org/

