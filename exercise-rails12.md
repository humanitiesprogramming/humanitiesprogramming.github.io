---
layout: exercise
title: Rails App
description: Phase Twelve - Testing with RSpec
permalink: /exercises/rails-twelve/
javascript:
  - /assets/js/catchup.js
---

In the long run, chances are you (or someone else) will need to upgrade or fix
your application. Chances are you also won't remember all the details of your
application in a year when (and trust me, it's **when** not *if*) you need to
fix something. One of the biggest challenges to these fixes is that you can
sometimes fix one part of you application, but break another.

So how do you guard against this? One way is to write ["tests"]({{ "/assets/img/testing_cat.jpg" | prepend: site.baseurl }})
 that allow you to
not only state the intent of your code, but also automates the system
validating that the code does what you intend.

> If you find yourself inheriting an application, writing tests is a good way
> to figure out what is going on in the application. When you change something
> you can update the application, you can also help ensure you don't break
> something else.

## RSpec
For tests, I really like a a framework named [RSpec][rspec] which follows a
"Behavior Driven Development" ([BDD][bdd]) methodology. What this means is that
the tests describe a particular behavior in a test that is expressed in the
code base.

## Setup
First we need to add the `rspec` dependency to the `testing` environment for
our app. Open the `Gemfile` and add the line:

{% highlight ruby %}
gem 'rspec-rails', '~> 3.0.0', group: [:development, :test]
{% endhighlight %}

Now run `bundle` in the terminal (without production).

{% highlight console %}
$ bundle --without production
{% endhighlight %}

> Powertip: `bundle` has an alias for `bundle install`. Hey, it saves 8 characters...

Now we can initialize rspec for our application.

{% highlight console %}
$ bin/rails generate rspec:install
      create  .rspec
      create  spec
      create  spec/spec_helper.rb
      create  spec/rails_helper.rb
{% endhighlight %}

This adds the configuration needed for the application, but we also want to add
a Rails 4 bin stub:

{% highlight console %}
$ bundle binstubs rspec-core
{% endhighlight %}

## First Test

Let's write a test for our Transcription object. Rspec runs tests in the `spec`
directory that are suffixed with `_spec.rb`. Let's write a test for our
Transcription model. Create a new file `spec/models/transcription_spec.rb`. In
it, add the following:

{% highlight ruby %}
require "rails_helper"

describe Transcription do

  it "has a title" do
    transcript = Transcription.new(:title => "United States Constitution")
    expect(transcript.title).to eq("United States Constitution")
  end

  it "has a description" do
      transcript = Transcription.new(:description => "United States Constitution")
      expect(transcript.description).to eq("United States Constitution")
  end

  context "with 2 or more comments" do
    it "orders them in chronological order" do
      transcript = Transcription.create!
      comment1 = transcript.comments.create!(:user_name => "foo", :body => "first comment")
      comment2 = transcript.comments.create!(:user_name => "foo", :body => "second comment")

      expect(transcript.reload.comments).to eq([comment1, comment2])
    end
  end
end
{% endhighlight %}

Now you can run the test with `bin/rspec spec`.

{% highlight console %}
$ bin/rspec spec
...
Finished in 0.03482 seconds (files took 1.19 seconds to load)
3 examples, 0 failures
{% endhighlight %}

Try adding a test that tests to ensure a transcription can be added to the
application.

## Controllers
You can also test controllers. This is useful to make sure the correct
templates are being rendered for a given controller action. Let's create a new
file at `spec/controllers/transcription_spec.rb` and add the following tests.

{% highlight ruby %}
require 'rails_helper'

describe TranscriptionsController do
  describe "GET 'index'" do
    it "returns http success header" do
      get :index
      expect(response).to be_success
      expect(response).to have_http_status(200)
    end

    it "renders the index template" do
      get :index
      expect(response).to render_template("index")
    end

    it "loads all of the transcriptions into @transcriptions" do
        transcript1, transcript2 = Transcription.create!, Transcription.create!
        get :index

        expect(assigns(:transcriptions)).to match_array([transcript1, transcript2])
    end
  end
end
{% endhighlight %}

Now you can run the tests:

{% highlight console %}
$ bin/rspec spec
......
Finished in 0.05028 seconds (files took 1.15 seconds to load)
6 examples, 0 failures
{% endhighlight %}

## Summary

A very common way (once you've gotten use to the syntax of tests) is to
actually write a test *before* you write any code. Think of this as writing an
outline like you would for a paper. You outline what you expect to cover in
your paper, then go and write the actual paper. This same technique goes for
software, but you have the additional benefit of having written a rhubric to
judge if the code actually follows what you're intending.

Testing does get quite complex very quickly, and it may seem like it's not
worth the time. Trust me, it is. Down the road, not only do the tests provide
safeguards against accidently breaking code, you also have additional
documentation on how to actually use the code. Software writers, as well
intentioned as they are, often forget to update documentation, or will "get to
it later." It does take a bit of discipline, and a lot of swearing when it
doesn't work, but it will save you time down the road.

[rspec]: http://rspec.info/
[bdd]: http://en.wikipedia.org/wiki/Behavior-driven_development
