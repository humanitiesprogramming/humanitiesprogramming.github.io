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