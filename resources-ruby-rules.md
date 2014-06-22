---
layout: page
title: Ruby Rules
description: Sandi Metz's Ruby Rules
permalink: /resources/ruby-rules/
---

[Sandi Metz](http://www.sandimetz.com/) articulated these rules for new
developers on an excellent episode of [Ruby Rogues](http://rubyrogues.com/087-rr-book-clubpractical-object-oriented-design-in-ruby-with-sandi-metz/). 

1. Classes can be no longer than one hundred lines of code.
2. Methods can be no longer than five lines of code.
3. Pass no more than four parameters into a method. Hash options are parameters.
4. In Rails, controllers can instantiate only one object. Therefore, views can only know about one instance variable and views should only send messages to that object (`@object.collaborator` value is not allowed).

