---
layout: page
title: Ruby Debugging Exercises
description: Ruby Debugging Exercises
permalink: /exercises/broken_ruby/
javascript:
  - /assets/js/hint.js
---

# Pirates

Broken:

{% highlight ruby %}

put "Hello!
greeting = gets.chomp()
if answer["Arrr!"]
	puts "Go away, pirate."

elsif
	puts "Greetings, hater of pirates!"

{% endhighlight %}

Fixed:

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

Broken:

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

Fixed:

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


# Branching

Broken:

{% highlight ruby %}

# A time traveller has suddenly appeared in your classroom!

# Create a variable representing the traveller's 
# year of origin (e.g., year = 2000) 
# and greet our strange visitor with a different message 
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

puts "Greetings! What is your year of origin?'
origin == gets.chomp().to_i
if origin < 1900
	puts 'That's the past!'
elseif origin > 1900 && origin < 2020
	puts "That's the present!"
elsif
	puts "That's the future!"

{% endhighlight %}

Fixed:

{% highlight ruby %}

# A time traveller has suddenly appeared in your classroom!

# Create a variable representing the traveller's 
# year of origin (e.g., year = 2000) 
# and greet our strange visitor with a different message 
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

puts "Greetings! What is your year of origin?"
origin = gets.chomp().to_i

if origin < 1900
	puts "That's the past!"

elsif origin > 1900 && origin < 2020
	puts "That's the present!"

elsif
	puts "That's the future!"
end

{% endhighlight %}

# Classes

Broken:

{% highlight ruby %}


# Write a simple class that defines a person 
# with attributes of first_name, last_name 
# and has a method signature of to_s which 
# prints the object as "Jefferson, Thomas".


classy Person

	def initial(fname lname)
		@first_name = firstname
		@last_name == lname
	

	def to_s
		@last_name +," " + @first_name
	
end

tj = Person.new("Thomas", "Jefferson")
puts person.fname
put tj

{% endhighlight %}

Fixed:

{% highlight ruby %}

class Person

	def initialize(fname, lname)
		@first_name = fname
		@last_name = lname
	end
	
	def to_s
		@last_name + ", " + @first_name
	end	

end

tj = Person.new("Thomas", "Jefferson")
print tj.to_s

{% endhighlight %}