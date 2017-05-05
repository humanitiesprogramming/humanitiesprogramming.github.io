---
layout: exercise
title: Second Ruby Exercises
description: Your second ruby exercises
permalink: /exercises/ruby-two/
javascript:
  - /assets/js/hint.js
---

[Ruby Cheatsheet]({{ "/resources/ruby-cheatsheet/" | prepend: site.baseurl }})


# Basic Methods

## Multiply (Easy)
Write a method that you can multiple two numbers (x,y). Test with the
following examples:

* 4, 2
* 0, 4
* 900, 32
* 29999, 0

{% highlight ruby %}
def multiply(x, y)
  return x * y
end

puts multiply(4,2)
puts multiply(0, 4)
puts multiply(900, 32)
{% endhighlight %}
<hr/>

## Divide (Easy, with a special case)

Write a method that you can divide two numbers (x,y). If the denominator is
zero, set it to the numerator (so that the method returns one). Test with the
following examples:

* 4, 2
* 0, 4
* 900, 32

{% highlight ruby %}
def divide(x, y)
  if(y == 0) 
    y = x
  end
  return x / y
end

puts divide(4,2)
puts divide(0, 4)
puts divide(900, 32)
{% endhighlight %}

<hr/>

# Print Name
Write a method that takes a parameter (name) and greets that user.

{% highlight ruby %}
def greet name
  return "Hello #{name}, you rock!"
end

puts greet "phybernightmare"
{% endhighlight %}

<hr/>

# Smallest Number

Write a method that evaluates two numbers and returns the smallest. If the
numbers are the same, it should return a message stating so.

{% highlight ruby %}
def smallest_number(x, y)
  smallest = x

  if x == y
    smallest = "They are the same"
  elsif y < x
    smallest = y
  end

  smallest

end

puts smallest_number(400,2)

{% endhighlight %}

<hr/>

# String Reverse

Write a method that accepts a string and returns the characters in reverses order.

**Hint**: Look at the Ruby documentation.

{% highlight ruby %}
def reverse(string)
  # use the built in method for reversing strings
  # see http://ruby-doc.org/core/classes/String.html#M001170
  string.reverse
end

test_string = "Praxis Program"
puts reverse(test_string)

{% endhighlight %}

<hr/>

# Loops

## While Loop

Write a method that uses a `while` loop to count from 1 to 1000 and print the
number of the current iteration to the screen. (That is, the first time
through, the loop should print "1"; "2" the next time through; and so forth.)

{% highlight ruby %}
def count(limit)
  counter = 0
  # note that do is optional with the while loop
  while counter <= limit
    puts counter
    counter += 1
  end
end

count(1000)

{% endhighlight %}
<hr/>

## Until Loop

Write a method that uses an `until` loop to print each number from 0 to 5.

{% highlight ruby %}
def count(limit)
  counter = 0
  until counter > limit
    puts counter
    counter += 1
  end
end

count(5)
{% endhighlight %}
<hr/>

## For Loop

Write a method that uses a `for` loop to print each number from 1 to 10.

{% highlight ruby %}
def count(limit)
  counter = 0
  for counter in (1..limit)
    puts counter
  end
end

count(10)
{% endhighlight %}

<hr/>

## Times Loop

Write a method that uses a `times` loop to print each number from 0 to 10.

{% highlight ruby %}
def count(limit)
  limit.times do |counter|
    puts counter
  end
end

count(11)
{% endhighlight %}

<hr/>

# Classes

Write a simple class that defines a person with attributes of
`first_name`, `last_name` and has a method signature of `to_s` which
prints the object as "Jefferson, Thomas".

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
puts tj # note, puts calls to_s if it is availabe
{% endhighlight %}
<hr/>

# Can't Get Enough?
Can't get enough? Work through the [Learn Ruby the Hard
Way](http://ruby.learncodethehardway.org/book/) exercises and/or
implement [the last programming exercises]({{ "/exercises/ruby-one/" | prepend: site.baseurl }}) as Objects.
