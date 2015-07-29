---
layout: exercise
title: Rails App - A Little Design
description: Phase Three
permalink: /exercises/rails-three/
javascript:
  - /assets/js/catchup.js
---

In the last module we built up fields to handle the transcription fields
we wanted using the scaffolding that Rails provides. This gets us down
the road quite a ways in creating a new application, but it doesn't
necessarily look very nice. Since we have to look at this, now is a good
time to get a bit further into implementing an updated view from the
**View** layer using Ruby's built-in ERB templating language.

Don't tell the instructors in the **Introduction to Web Development and
Design Principals**, but we're going to use a shortcut in our design and
layout with the [Twitter Bootstrap](http://getbootstrap.com/) CSS
framework not only to make things look a lot better, but also to give us a
version of the application that works as well on mobile devices as it
does in the browser on a computer.

## Include the CSS

We need to tell the main application layout to include the Twitter
Bootstrap styles from their [CDN](http://en.wikipedia.org/wiki/Content_delivery_network).
Open `app/views/layouts/application.html.erb` and add the following under
the `stylesheet_link_tag` line:

{% highlight rhtml %}
<%= stylesheet_link_tag "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" %>
<%= stylesheet_link_tag "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css" %>
{% endhighlight %}

Now find the main `yield` section and surround it with a
`div.container`.

{% highlight rhtml %}
<div class="container">
  <%= yield %>
</div>
{% endhighlight %}

If you're like me, you're impatient and want to see what changed. Start
up your server (`bin/rails server`) and see if you see anything different at
[http://localhost:3000/transcriptions/][t].

## JavaScript

Twitter Bootstrap makes use of JavaScript to help with a few
interactions. Let's add that library in. Again, in the
`app/views/layouts/application.html.erb` file, just before the end tag for the`<body>`
element, add these new `footer` and `script` elements.

{% highlight rhtml %}
<footer>
  <div class="container">
    HILT <%= Time.now.year %>
  </div>
</footer>
<%= javascript_include_tag "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" %>
{% endhighlight %}

If you start your web server up again, you should see the new footer on
the page, and it should also be loading the `bootstrap` library of
effects.

> **Question**: What does `Time.now.year` do? Why might this be better than manually typing out "2014"?

## Navigation

We want to add a cool navigation header on the page. We want to include
a menu option for mobile users that displays all the pages, as well as
the name of the app and a link to the transcriptions. Add the following below the `body`
element and before the `div.container`.

{% highlight rhtml %}
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <%= link_to "Scriba", transcriptions_path, class: 'navbar-brand' %>
    </div>
    <div class="collapse navbar-collapse">
      <ul class="nav navbar-nav">
        <li class="active">
          <%= link_to "Transcriptions", transcriptions_path %>
        </li>
      </ul>
    </div>
  </div>
</nav>
{% endhighlight %}

{% gist waynegraham/50d282f4ea72f56e2c7b %}

Fire up your browser now and look at [http://localhost:3000/transcriptions][t].
Does it look correct?

![Bootstrap Header]({{ "/assets/img/exercises/rails-three/bootstrap-header.png" | prepend: site.baseurl }}){: .img-responsive}


Let's fix that now. We need to update the stylesheets for Rails. We
won't get too much in to **SASS/SCSS** in this course, but it's a
superset of CSS that has some really cool features added. However, for
our purposes, we'll keep it "simple" and just write to the SCSS file
with CSS. Open `app/assets/stylesheets/transcriptions.scss` and add
the following rules:

{% highlight css %}
body { padding-top: 100px; }
footer { margin-top: 100px; }
table, td, th { vertical-align: middle; border: none; }
th { border-bottom: 1px solid #DDD; }
{% endhighlight %}

If you refresh your the page of transcrions ([http://localhost:3000/transcriptions][t]),
you should see something that looks much better.

![Bootstrap Header]({{ "/assets/img/exercises/rails-three/bootstrap-header-update.png" | prepend: site.baseurl }}){: .img-responsive}


## Git

Now that the main components are working and we have the content
working, it's a good time to add and commit the changes to `git`.

{% highlight console %}
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   app/assets/stylesheets/transcriptions.scss
      modified:   app/views/layouts/application.html.erb$ git commit
$ git add app
$ git commit -m "Added Twitter Bootstrap for the views"
[master f14d44a] Added Twitter Bootstrap for the views
 2 files changed, 36 insertions(+)
{% endhighlight %}

## Scaffold Styles

So your app doesn't use browser defaults, Rails adds a few styles when you run
the `scaffold` generator. However, we have some better styles for much of what
we want to do from Twitter Bootstrap. Let's just go ahead and remove the
generated file. We'll use the `git` command to do this.

{% highlight console %}
$ git rm app/assets/stylesheets/scaffolds.scss
rm 'app/assets/stylesheets/scaffolds.scss'
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

  deleted:    app/assets/stylesheets/scaffolds.scss
$ git commit -m "Removed generated scaffold styles"
{% endhighlight %}

> If you start the server up again, and look at the [transcriptions][t], does this look any different?

[t]: http://localhost:3000/transcriptions
