---
layout: exercise
title: Python Cheatsheet
description: Cheatsheet for Python syntax
permalink: /resources/python-cheatsheet/
---

# Ruby Cheatsheet


## Variables
Variable names use underscores between words for complex names

{% highlight python %}
number = 5
my_number = 7

{% endhighlight %}

## Spacing
Python enforces consistent tabbing. So, when you're working with loops inside loops or functions inside classes, etc., you must preserve the hierarchy using meaningful whitespace.

if this_thing == True:
     print("this!")


for thing in many_things:
     if this_is == True:
          print('This!')
     else:
          print("This instead")

## Conditional Tests (if)

Place `if`, `elif`, and `else` on separate lines. Each logic line must end in a colon, and the subsequent lines must be indented. You do not need to put an "end" keyword at the end of the sequence. In Python 3 you must indent with five spaces (though most text editors will do this for you).

{% highlight python %}
if number == 5:
  puts "Success"
elif number == 7:
  puts "Praxis FTW"
else:
  puts "FAIL"
{% endhighlight %}

## Operators

Coming soon!

## Method Calls

Parentheses are required (though will change in Python 2 vs 3). Additionally, if you you do not give parentheses at the end of a function it will not run.

{% highlight python %}
print("Word")

run_a_function <-- not run
run_a_function() <-- run!

{% endhighlight %}

## Method Definitions

Methods can return values which can be assigned to a variable. The function must end with a return statement, something that signifies what the function is giving back when called.

{% highlight python %}
def make_positive(number):
  if number < 0:
    -number
  return number
end

puts make_positive(-5)
{% endhighlight %}

## Dictionaries

Dictionaries hold objects and are referenced by their `key` assignment.

{% highlight python %}
dictionary = {}
other_dictionary = {"VA": "Virginia", "NC": "North Carolina"}

len(hash)

other_dictionary.keys()
other_dictionary['VA']
other_dictionary.values()

{% endhighlight %}

## Lists

Lists hold objects and are referenced by their position, starting with
position `0`. You can use a ':' to grab everything before or after particular index positions.

{% highlight python %}
empty_list = []
another_list = [1, 2, "three"]

empty_list[0]   # <= error
another_list[2] # <= "three"

another_list[-1]
another_list[0] = "nonsense" # <= sets value at position 0 to
"nonsense"
another_list[1:] # <= everything from the first element on.
another_list[:2] # <= everything before the 2nd element
{% endhighlight %}


## For Loops

Loops allow you to apply the same thing to each element in a list. You assign a variable name to refer to the item in each index position. The following both do the same thing.

{% highlight python %}
a_list = [1, 2, "three"]

for item in a_list:
     print(item)

for foo in a_list:
     print(foo)

{% endhighlight %}

## List Comprehension

List comprehensions are a way of neatly organizing a particular loop type that happens often. These do the same thing.
{% highlight python %}
numbers = [1,2,3,4,5]
results = []

for item in numbers:     	
     results.append(item + 5)

results_as_a_list_comprehension = [item + 5 for item in numbers]
{% endhighlight %}
