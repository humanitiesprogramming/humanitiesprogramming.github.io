---
layout: exercise
title: Second Python Exercises
description: Your second python exercises
permalink: /exercises/python-two/
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

{% highlight python %}
def multiply(x, y):
  return(x * y)

print(multiply(4, 2))
print(multiply(0, 4))
print(multiply(900, 32))
{% endhighlight %}
<hr/>

## Divide (Easy, with a special case)

Write a method that you can divide two numbers (x,y). If the denominator is
zero, set it to the numerator (so that the method returns one). Test with the
following examples:

* 4, 2
* 0, 4
* 900, 32

{% highlight python %}
def divide(x, y):
  if(y == 0):
    y = x
  else:
    return(x / y)

print(divide(4, 2))
print(divide(0, 4))
print(divide(900, 32))
{% endhighlight %}

<hr/>

# Print Name
Write a method that takes a parameter (name) and greets that user.

{% highlight python %}
def greet(name):
  return("Hello %s, you rock!" % name)

print(greet("phybernightmare"))
{% endhighlight %}

<hr/>

# Smallest Number

Write a method that evaluates two numbers and returns the smallest. If the
numbers are the same, it should return a message stating so.

{% highlight python %}
def smallest_number(x, y):
  smallest = x

  if x == y:
    smallest = "They are the same."
  elif y < x:
    smallest = y
  elif x < y:
    smallest = x

  return(smallest)

print(smallest_number(400,2))

{% endhighlight %}

<hr/>

# String Reverse

Write a method that accepts a string and returns the characters in reverses order.

**Hint**: Look at the Python documentation.

{% highlight python %}
def reverse(string):
  return(string[::-1])

test_string = "Praxis Program"
print(reverse(test_string))

{% endhighlight %}

<hr/>

# Loops

## While Loop

Write a method that uses a `while` loop to count from 1 to 1000 and print the
number of the current iteration to the screen. (That is, the first time
through, the loop should print "1"; "2" the next time through; and so forth.)

{% highlight python %}
def count(limit):
  counter = 0
  while counter <= limit:
    print(counter)
    counter += 1

count(1000)

{% endhighlight %}
<hr/>

## "Until" Loop

As we talked about in class, there is no "until" loop in Python. However, While loops can provide similar results. Write a method that uses an `while` loop to print each number from 0 to 5.

{% highlight python %}
def count(limit):
  counter = 0
  while counter <= limit:
    print(counter)
    counter += 1

count(5)
{% endhighlight %}
<hr/>

## For Loop

Write a method that uses a `for` loop to print each number from 1 to 10.

{% highlight python %}
def count(limit):
  counter = 0
  for i in range(limit + 1)
    print(counter)
    counter += 1

count(10)
{% endhighlight %}

<hr/>

# Classes

Write a simple class that defines a person with attributes of
`first_name`, `last_name` and has a method signature of `to_s` which
prints the object as "Jefferson, Thomas".

{% highlight python %}
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
