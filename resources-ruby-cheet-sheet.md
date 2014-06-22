---
layout: exercise
title: Ruby Cheatsheet
description: Cheatsheet for Ruby syntax
permalink: /resources/ruby-cheatsheet/
---

# Ruby Cheatsheet


## Variables
Variable names use underscores between words for complex names

{% highlight ruby %}
number = 5
my_number = 7

@instance # <= Accessible to an instance of an object
local     # <= Accessible only to the current context
CONSTANT  # <= Variable that once set, never changes
$global   # <= Accessible just about anywhere
@@class   # <= 

person1 = person2     # <= both reference same object
person2 = person1.dup # <= shallow copy of person1
person1.freeze        # <= prevents changes to person1
{% endhighlight %}

## Conditional Tests (if)

Place `if`, `elsif`, `else`, and `end` on separate lines. 

{% highlight ruby %}
if number == 5
  puts "Success"
elsif number == 7
  puts "Praxis FTW"
else
  puts "FAIL"
end
{% endhighlight %}

## Operators

{% highlight ruby %}
**   # raise to power
!    # not
%    # modulus
+    # addition
-    # subtraction
|    # pipe
? :  # conditional expression (ternary) 
^    # carrot
>    # greater than
>=   # greater than or equal to
<    # less than
<=   # less than or equal to
&&   # boolean AND
||   # boolean OR
..   # inclusive range (3..10) includes 3 and 10
...  # exclusive range (3...10) excludes 3 and 10 
=    # assignment
not  # logical NOT
and  # logical AND
or   # logical OR
<=>  # comparison
{% endhighlight %}

## Method Calls

Parentheses are optional, but make method calls more readable.

{% highlight ruby %}
puts "Word"
puts("Word")
{% endhighlight %}


## Method Definitions

Methods can return values which can be assigned to a variable.

{% highlight ruby %}
def make_positive(number)
  if number < 0
    -number
  end
  number
end

puts make_positive(-5)
{% endhighlight %}

## Hashes

Hashes hold objects and are referenced by their `key` assignment. 

{% highlight ruby %}
hash = {}
other_hash = {"VA" => "Virginia", "NC" => "North Carolina"}

hash.length
hash.empty?

other_hash.has_key?('VA')
other_hash['VA']
other_hash.values
other_hash.keys

{% endhighlight %}

## Arrays

Arrays hold objects and are referenced by their position, starting with
position `0`.

{% highlight ruby %}
empty_array = Array.new
another_array = [1, 2, "three"]

empty_array[0]   # <= nil
another_array[2] # <= "three"

another_array.last
another_array[0] = "nonsense" # <= sets value at position 0 to
"nonsense"
{% endhighlight %}


## Iterators
Iterators allow you to repeat an action.

{% highlight ruby %}
[1, 2, 3].each do |value|
  puts value
end

(1..3).each { |value| puts value }

["praxis", "program"].collect { |value| puts value.capitalize }

3.times { |i| puts "There's no place like home..." }

{% endhighlight %}
