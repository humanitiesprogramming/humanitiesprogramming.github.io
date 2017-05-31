---
layout: exercise
title: First Python Exercises
description: Your first python exercises
permalink: /exercises/python-one/
javascript:
  - /assets/js/hint.js
---

# Printing to the Screen
Store your street address, city, state, and zip code in variables (or
even better, a **dictionary**!), then print them in the usual format:

Name<br/>
Street<br/>
City, State, Zip



{% highlight ruby %}
address = {
  "name": "Thomas Jefferson",
  "street": "931 Thomas Jefferson Parkway",
  "city": "Charlottesville",
  "state": "Virginia",
  "zip": "22902"
}

print(address['name'])
print(address['street'])
print(address['city'] + ", " + address['state'] + " " + address['zip'])
{% endhighlight %}

<hr/>

# Calculations

Write a program that converts seconds to years. Test your program with
`600000000` seconds, `60` seconds, and `40000.33` seconds.

Does this make sense for all the inputs? We can get a bit more exact if
we cast `test1` as a **float**.

`test1 = 600000000.to_f`

{% highlight ruby %}

test1 = 600000000
# there are 60 seconds and minute
in_minutes = test1 / 60
# there are 60 minutes in an hour
in_hours = in_minutes / 60
# there are 24 hours in a day
in_days = in_hours / 24
# there are about 365 days in a year
in_years = in_days / 365

print(in_years)

{% endhighlight %}


<hr class="prepend"/>

# Collections

Create a collection of these authors and the year they kicked the bucket. Print the
collection in the following format:

Charles Dickens died in 1870.

Charles Dickens, 1870<br/>
William Thackeray, 1863<br/>
Anthony Trollope, 1882<br/>
Gerard Manley Hopkins, 1889

{% highlight ruby %}
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print "%s" % author + " died in " + "%s." % date
{% endhighlight %}

<hr/>

# Branching

A time traveler has suddenly appeared in your classroom!

Create a variable representing the traveler's year of origin (e.g., year = 2000) and greet our strange visitor with a different message if he is from the distant past (before 1900), the present era (1900-2020), or from the far future (beyond 2020).

If you want to get really fancy, try writing a line of code that would ask your user "What year is this time traveler from?", then print the appropriate response according to their answer.

{% highlight ruby %}

year = 1899
# if you chose to get fancy, the input request might look like this:
# year = int(input("What year is this time traveler from? "))

if year <= 1900:
    print ("Welcome from the distant past!")
elif year > 1900 and year < 2020:
    print ("Welcome from the present!")
else:
    print ("Welcome from the far future!")

{% endhighlight %}

<hr/>

# Pirate Test (easy)
Write a program that tests whether someone is a pirate or not.  As we all know, no pirate can resist using the exclamation "**Arrr!**" constantly.  If a string contains "**Arrr!**", tell the pirate to go away.  Otherwise, welcome your non-pirate friend with open arms.

## Tests:

* **Arrr! How are ye?**
* **Hellow, friend.**

**Hint**: `string_variable["some text"]` equals "`some text`" if those characters exist in
`string_variable` and otherwise equals `nil`.

{% highlight ruby %}
answers = ["Arrr! How are ye?", "Hello, friend."]

answers.each do |answer|
  if answer['Arrr!']
     puts "Go away, scurvy sea dog"
  else
     puts "Welcome!"
  end
end

{% endhighlight %}

<hr/>

# Longest word (not too hard)
Print out the longest word in "The quick brown fox jumped over the lazy dogs" and its length.

##Hints
* `my_string.length` equals the length of a string.
* `my_long_string.split(" ").each` will break the string up by spaces.

What about "The quick brown fox jumps over the lazy dogs"?  How might we find all the longest words?

{% highlight ruby %}
sentence = "The quick brown fox jumped over the lazy dogs"

longest = ""

sentence.split(" ").each do |word|
   if word.length > longest.length
      longest = word
   end
end

puts "The word '" + longest + "' is " + longest.length.to_s + " characters long."

{% endhighlight %}

<hr/>

# Calculating Grades (ok, let me think about this one)

Write a program that will average 3 numeric exam grades and return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

<table>
<tr>
<th>Average</th>
<th>Grade</th>
</tr>
<tr>
<th>90+</th>
<th>A</th>
</tr>
<tr>
<th>80-89</th>
<th>B</th>
</tr>
<tr>
<th>70-79</th>
<th>C</th>
</tr>
<tr>
<th>60-69</th>
<th>D</th>
</tr>
<tr>
<th>0-59</th>
<th>F</th>
</tr>
</table>

Exams: 89, 90, 90<br/>
Average: 90<br/>
Grade: A<br/>
Student is passing.

Exams: 50, 51, 0<br/>
Average: 33<br/>
Grade: F<br/>
Student is failing.


{% highlight ruby %}
# option 1 to calculate the grade average
e1 = 89
e2 = 90
e3 = 90

avg = (e1 + e2 + e3) / 3

# option 2 to calculate the grade average
grades = [50, 51, 0]
sum = 0
grades.each do |g|
  sum = sum + g
end

avg = sum / grades.length

if avg >= 90
  grade = "A"
elsif avg >= 80 && avg < 90
  grade = "B"
elsif avg > 69 && avg < 80
  grade = "C"
elsif avg >= 69 && avg <= 69
  grade = "D"
else
  grade = "F"
end

grades.each do |g|
  puts "Exam: " + g.to_s
end

puts "Average: " + avg.to_s

puts "Grade: " + grade

if grade == "F"
  puts "Student is failing"
else
  puts "Sudent is passing"
end


{% endhighlight %}

<hr/>

# Population Growth (Might need to ask somebody)

The population of Fibonaccia has been shown to grow at an exponential rate with a really odd phenomenon: each year the total population is the sum of the population for the previous two years. With a starting population of 10, the population for the first five years would be:

10, 20, 30, 50, 80

Write a program that will calculate the population of Fibonaccia after 10 years, 20 years, 100 years.

**Hint**: `population = [0,10]`

{% highlight ruby %}
years = 1000
population = [0,10]

years.times do |p|
  population.push(population[-1] + population[-2])
end

puts population
{% endhighlight %}

<hr/>

# Population Growth (Are you serious?)

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not exceed 4 million.

{% highlight ruby %}
# There are many ways to solve this problem; here are three:

MAX = 4000000

fib_seq = [1, 2]
sum = 2
while fib_seq[-1] <= MAX
  next_fib = fib_seq[-1] + fib_seq[-2]
  fib_seq.push(next_fib)
  sum += next_fib if next_fib.even?
end

puts "Sum of even members of Fibonacci sequence less than 4,000,000: #{sum}."


# Another way

cutoff = 1000000 # when to end
f_2 = 1
f_1 = 2
fib = 3 # star of the fibonacci sequend
sum = 2 # sum of even numbered fib numbers

while fib <= cutoff
  oldfib = fib # save current fib value
  fib = fib + f_1
  f_2 = f_1
  f_1 = oldfib

  if fib % 2 == 0
    sum += fib
  end
end

puts 'sum of even numbered fibonacci numbers is ' + sum.to_s

# Using more advanced syntax

x, y, sum = 1, 1, 0
while sum < 1000000
  sum += (x + y)
  x, y = x + 2 * y, 2 * x + 3 * y
end

puts "Sum is #{sum}."

# Yet another method, perhaps less obvious, but far more interesting...
#
# If you look at the numbers printed out from 1, you may notice
# something interesting
#
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610
#
# specifically, look at every third number in the index
#
# 2, 8, 34, 144, 610
#
# This is based on the general rule in the Fibannci sequence that every
# nth term is a multiple of F(n). Mathematically, this is
#
# F(nk) is a multiple of F(k) for all values of n and k from 1 up.
#
# Try it out:
# * every 4th term (3) is a multiple of 3
# * every 5th term (5) is a multiple of 5
# * every 6th term (8) is a multiple of 8
#
# Use this fact to build a solution

{% endhighlight %}
