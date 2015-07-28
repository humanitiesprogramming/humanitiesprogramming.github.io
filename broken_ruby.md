---
layout: page
title: Ruby Debugging Exercises
description: Ruby Debugging Exercises
permalink: /exercises/broken_ruby/
javascript:
  - /assets/js/hint.js
---

# Pirates

Broken code:

{% highlight ruby %}

put "Hello!
greeting = gets.chomp()
if answer["Arrr!"]
	puts "Go away, pirate."

elsif
	puts "Greetings, hater of pirates!"

{% endhighlight %}

Fixed code:

{% highlight ruby %}

puts "Hello!"
greeting = gets.chomp()
if greeting["Arrr!"]
	puts "Go away, pirate."

elsif
	puts "Greetings, hater of pirates!"
end

{% endhighlight %}

# Collections

Broken code:

{% highlight ruby %}

dickens = ["Charles Dickens," "1870"]
thackeray = {"William Thackeray", "1863"}
trollope = {'Anthony Trollope', '1882'}
hopkins = ["Gerard Manley Hopkins" => "1889"]

def died(array)
	name = array[2]
	year = array[1]
	puts  "#name died in {year}."

puts died(Dickens)
puts died(thackeray)
put died(trollop)
puts died(hopkins)

end

{% endhighlight %}

Fixed code:

{% highlight ruby %}

# Create a collection of these authors and 
# the year they kicked the bucket; 
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889



dickens = ["Charles Dickens," "1870"]
thackeray = ["William Thackeray", "1863"]
trollope = ['Anthony Trollope', '1882']
hopkins = ["Gerard Manley Hopkins", "1889"]

def died(array)
	name = array[0]
	year = array[1]
	puts  "#{name} died in #{year}."

end

puts died(dickens)
puts died(thackeray)
puts died(trollope)
puts died(hopkins)

{% endhighlight %}