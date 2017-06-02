---
layout: page
title: Python Debugging Exercises
description: Python Debugging Exercises
permalink: /exercises/python-debugging/
javascript:
  - /assets/js/hint.js
---

# Common Code Errors and How to Find Them  

Many errors in code written by developers at all levels boil down to just a few common types of problems:

1.  Syntax: check brackets, if/elsif/else statements, braces, commas, parentheses, quotation marks, etc. The computer needs syntax to be exactly right in order for it to run your programs: it cannot make any assumptions about what you might mean. So it cannot, for example, infer "Wednesday" from "Wendesday." Make sure you are using [python syntax](https://docs.python.org/2/reference/).
2.  Variables: make sure your variable names are consistent and that they are defined before you use them for the first time. Name them in ways that convey their use so that others (and you!) remember what they are meant to do.
3.  Functions: make sure that you know how your functions work. What kinds of things do they return? A string? A list? A dictionary?


If you get stuck, try the following to help you figure out what is going on:

1.  Print out variable values at different points in the program to make sure they return what you expect.
2.  Make sure the coloring in your text editor looks like you expect it to.
3.  Read the error output in the terminal. It tries to be helpful, but it will often not quite point you towards the problem. It can at least give you a ballpark location in the code and some things to look for.
4.  Get sections of the code working (see step one) so that you can narrow your search for the problem. Python can help with this: try playing in this environment to debug sections.
5.  Read the Python documentation for the methods you are employing.
6.  Comment throughout your code to make sure you understand what every step is doing. This will help you pinpoint problems.
7.  Ask for help!

<hr/>

These exercises will help you practice debugging your code. There are no problems: only solutions waiting to be found.

# Pirates

Broken:

{% highlight ruby %}

greeting = input("Hello, possible pirate! What's the password?)
if greeting in ["Arrr!"):
	print("Go away, pirate.")
elif
print("Greetings, hater of pirates!")

{% endhighlight %}

Fixed:

{% highlight ruby %}

greeting = input("Hello, possible pirate! What's the password? ")
if greeting in ["Arrr!"]:
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")

{% endhighlight %}

<hr/>

# Collections

Broken:

{% highlight ruby %}

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authrs = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"

for author date in authors.items{}:
    print "%s" % authors + " died in " + "%d." % Date
}

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



authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print("%s" % author + " died in " + "%s." % date)

{% endhighlight %}

<hr/>

# Branching

Broken:

{% highlight ruby %}

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year == int.input("Greetings! What is your year of origin? '))

if year <= 1900
    print ('Woah, that's the past!')
elif year > 1900 && year < 2020:
    print ("That's totally the present!")
elif:
    print ("Far out, that's the future!!")


{% endhighlight %}

Fixed:

{% highlight ruby %}

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")

{% endhighlight %}

<hr/>

# Classes

Broken:

{% highlight ruby %}


# Write a simple class that defines a person
# with attributes of first_name, last_name
# and has a method signature of "speak" which
# prints the object as "Jefferson, Thomas".

classy Person:
  def __initalize__(self, first_name, last_name):
    self.first = first_name
    self.last = lname
  def speak(self):
  print("My name is + " self.fname + " " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.self.speak

{% endhighlight %}

Fixed:

{% highlight ruby %}

class Person:
  def __init__(self, first_name, last_name):
    self.first = first_name
    self.last = last_name
  def speak(self):
    print("My name is " + self.first + " " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()

{% endhighlight %}

<hr/>

# Grading

Broken:

{% highlight ruby %}

# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = input("Input exam grade two: "))

exam_3 = str(input("Input exam grade three: "))

grades = [exam_one exam_two exam_three]
sum = 0
for grade in grade:
  sum = sum + grade

avg = sum / len(grdes)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C'
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter-grade is "F":
    print "Student is failing."
else:
    print "Student is passing."

{% endhighlight %}

Fixed:

{% highlight ruby %}

# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.


exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade is "F":
    print("Student is failing.")
else:
    print("Student is passing.")

{% endhighlight %}
