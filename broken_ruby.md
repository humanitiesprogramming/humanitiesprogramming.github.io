---
layout: page
title: Ruby Debugging Exercises
description: Ruby Debugging Exercises
permalink: /exercises/broken_ruby/
javascript:
  - /assets/js/hint.js
---

# Common Code Errors and How to Find Them  

Many errors in code written by developers at all levels boil down to just a few common types of problems:

1.  Syntax: check brackets, if/elsif/else statements, braces, commas, parentheses, quotation marks, etc. The computer needs syntax to be exactly right in order for it to run your programs: it cannot make any assumptions about what you might mean. So it cannot, for example, infer "Wednesday" from "Wendesday." Make sure you are using [ruby syntax](http://ruby-doc.org/docs/ruby-doc-bundle/Manual/man-1.4/syntax.html).
2.  Variables: make sure your variable names are consistent and that they are defined before you use them for the first time. Name them in ways that convey their use so that others (and you!) remember what they are meant to do. 
3.  Functions: make sure that you know how your functions work. What kinds of things do they return? A string? An array? A hash?


If you get stuck, try the following to help you figure out what is going on:

1.  Print out variable values at different points in the program to make sure they return what you expect.
2.  Read the error output in the terminal. It tries to be helpful, but it will often not quite point you towards the problem. It can at least give you a ballpark location in the code and some things to look for.
3.  Get sections of the code working (see step one) so that you can narrow your search for the problem. irb can help with this: try playing in this environment to debug sections.
4.  Read the ruby documentation for the methods you are employing.
5.  Comment throughout your code to make sure you understand what every step is doing. This will help you pinpoint problems.
6.  Ask for help!

<hr/>

These exercises will help you practice debugging your code. There are no problems: only solutions waiting to be found. 

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

<hr/>

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

<hr/>

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

<hr/>

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
# Student if fails


put "Input exam grade one:"
exam_one = gets.chomp().toi

puts 'Input exam grade two:'
exam_two = gets.chomp(.to_s

puts "Input exam grade three:"
exam_3 = gets.chomp().to_i

def list_grade(exam_one exam_two exam_three)
	puts "Exams: #exam_one}, #{exam_two}, {exam_three}"
end

def average_grade(exam_one, exam_two, exam_three)
	average == (exam_one + exam_two + exam_three) / 3)
end
average = avrage_grade(exam_one, exam_two, exam_three).to_i

def letter_grade(average-grade)
	if average_grade < 59
		puts "Grade: F"
	elseif average_grade >= 60 && average_grade <= 69
		puts "Grade: D"
	elsif average_grade > 70 & average_grade <= 79
		puts 'Grade: C"
	elseif average_grade >= 80 && average_grade <= 89
		puts "Grade: B"
	elsif average_grade == 90
		puts "Grade: A'
	
end

def pass_fail(average)
	if average < 59
		puts "Student is failing.
	else puts "Student is passing."
	end
end

list_grade(exam_one, exam_two, exam_three)
puts "Average": #{average}"		
lettergrade(average)			
pass_fail(average)

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
# Student if fails


puts "Input exam grade one:"
exam_one = gets.chomp().to_i

puts "Input exam grade two:"
exam_two = gets.chomp().to_i

puts "Input exam grade three:"
exam_three = gets.chomp().to_i

def list_grade(exam_one, exam_two, exam_three)
	puts "Exams: #{exam_one}, #{exam_two}, #{exam_three}"
end

def average_grade(exam_one, exam_two, exam_three)
	average = ((exam_one + exam_two + exam_three) / 3)
end

average = average_grade(exam_one, exam_two, exam_three).to_i

def letter_grade(average_grade)
	if average_grade < 59
		puts "Grade: F"
	elsif average_grade >= 60 && average_grade <= 69
		puts "Grade: D"
	elsif average_grade > 70 && average_grade <= 79
		puts 'Grade: C'
	elsif average_grade >= 80 && average_grade <= 89
		puts "Grade: B"
	else average_grade == 90
		puts "Grade: A"
	end
end

def pass_fail(average)
	if average < 59
		puts "Student is failing"
	else 
		puts "Student is passing."
	end
end

list_grade(exam_one, exam_two, exam_three)
puts "Average: #{average}"		
letter_grade(average)			
pass_fail(average)

{% endhighlight %}

<hr/>

# [Room 101](https://en.wikipedia.org/wiki/Ministries_of_Nineteen_Eighty-Four#Room_101)

Broken:

{% highlight ruby %}

module Ex2

  # This function will break up words for us.
  def Ex25.brak_words(stuff
    words = stuff.split(' ')
    return word
  end

  # Sorts the words.
  def Ex25.sortwords(words)
    return words.sort
  end

  # Prints the first word after popping it off.
  df Ex25.print_first_word(words)
    word = words.pop(1)
    puts wor
  end

  # Prints the last word after popping it off.
  def Ex25:print_last_word(words)
    word = words.pop
    put word
  end

  # Takes in a full sentence and returns the sorted words.
  def Ex25.sort_sentence(sentence)
    words = Ex25.break_words(sentence)
    return Ex25.sort_words(words)
  ed

  # Prints the first and last words of the sentence.
  def Ex25.print_first_and_last(sentence
    words = Ex25.break_words(sentenc)
    Ex25.print_first_wrd(word)
    Ex25.print_last_word(words)
  end

  # Sorts the words then prints the first and last one.
  def Ex25.print_first_and_last_sorted(sentence)
    words = Ex25.sort_sentence(sentence)
    Ex25.print_fist_word(words)
    Ex25.print_last_word(words)
  end



puts "Let's practice everything."
puts 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = <<END
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
ENDED

puts "--------------"
puts poem
puts "--------------"


five = 10 - 2  3 - 6
puts "This should be five: #{five"

def secret_formula(started)
  jelly_bens = started * 500
  jars = jelly_beans / 1000
  crate = jars / 100
  return jelly_beans, jars, crates
end


start_point = 10000
beans, jars crates = secret_formula(start_point)

puts "With a starting point of: #{start_point}"
puts "We'd have #{beans beans, #{jars} jars, and #{crates} crates."

start_point = start_point / 10

sentence = "All good things come to those who wait."
words = Ex25.break_words(sentence)
sorted_words = Ex25.sort_words(words)
Ex25.print_first_word(wrds)
Ex25.print_last_word words)
Ex25.print_first_word(sort_words)
Ex25.print_last_word(sorted_words)
sorted_words = Ex25.sort_sentenc(sentence)
Ex25.print_first_and_last(sentence)
Ex25:print_first_and_last_sorted(sentence)

{% endhighlight %}

Fixed:

{% highlight ruby %}

# Note - we haven't actually learned several of the methods 
# and syntactical tricks in this exercise. Google them!

module Ex2

  # This function will break up words for us.
  def Ex25.brak_words(stuff
    words = stuff.split(' ')
    return word
  end

  # Sorts the words.
  def Ex25.sortwords(words)
    return words.sort
  end

  # Prints the first word after popping it off.
  df Ex25.print_first_word(words)
    word = words.pop(1)
    puts wor
  end

  # Prints the last word after popping it off.
  def Ex25:print_last_word(words)
    word = words.pop
    put word
  end

  # Takes in a full sentence and returns the sorted words.
  def Ex25.sort_sentence(sentence)
    words = Ex25.break_words(sentence)
    return Ex25.sort_words(words)
  ed

  # Prints the first and last words of the sentence.
  def Ex25.print_first_and_last(sentence
    words = Ex25.break_words(sentenc)
    Ex25.print_first_wrd(word)
    Ex25.print_last_word(words)
  end

  # Sorts the words then prints the first and last one.
  def Ex25.print_first_and_last_sorted(sentence)
    words = Ex25.sort_sentence(sentence)
    Ex25.print_fist_word(words)
    Ex25.print_last_word(words)
  end



puts "Let's practice everything."
puts 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = <<END
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
ENDED

puts "--------------"
puts poem
puts "--------------"


five = 10 - 2  3 - 6
puts "This should be five: #{five"

def secret_formula(started)
  jelly_bens = started * 500
  jars = jelly_beans / 1000
  crate = jars / 100
  return jelly_beans, jars, crates
end


start_point = 10000
beans, jars crates = secret_formula(start_point)

puts "With a starting point of: #{start_point}"
puts "We'd have #{beans beans, #{jars} jars, and #{crates} crates."

start_point = start_point / 10

sentence = "All good things come to those who wait."
words = Ex25.break_words(sentence)
sorted_words = Ex25.sort_words(words)
Ex25.print_first_word(wrds)
Ex25.print_last_word words)
Ex25.print_first_word(sort_words)
Ex25.print_last_word(sorted_words)
sorted_words = Ex25.sort_sentenc(sentence)
Ex25.print_first_and_last(sentence)
Ex25:print_first_and_last_sorted(sentence)

{% endhighlight %}