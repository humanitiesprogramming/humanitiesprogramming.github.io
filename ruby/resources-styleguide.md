---
layout: page
title: Ruby Style Guide
description: Styleguide for writing Ruby applications
permalink: /resources/style-guide/
---

These styles are adapted from the excellent work Bozhidar Batsov posted
on his [Ruby Style Guide](https://github.com/bbatsov/ruby-style-guide)
project.

<blockquote>
Nearly everybody is convinced that every style but their own is
ugly and unreadable. Leave out the "but their own" and they're
probably right...
<br/><span class="by">Jeffy Coffin</span>
</blockquote>

## Formatting

* Use UTF-8 as the source file encoding
* Use two-space indent (NO TABS)
* Use Unix style line endings

    Use `$git config --global core.autoclrf true` to ensure Window's
style doesn't creep in

* Use spaces around operators, and curly braces ('`{`', '`}`') after commas and semicolons

{% highlight ruby %}
sum = 1 + 2
a, b = 1, 2
1 > 2 ? true : false; puts "hi"
[1, 2, 3].each { |e| puts e }
{% endhighlight %}

* No spaces after '`(`', or between braces ('`[`', '`]`').

{% highlight ruby %}
some(arg).other
[1, 2, 3].length
{% endhighlight %}

* Indent `when` as deep as `case`.
{% highlight ruby %}
case
when song.name == 'Tik Tok'
  puts "Not again!"
when song.duration > 120
  puts "That's really long"
when Time.now.hour > 21
  puts "It's time to start coding"
else
  song.play
end

epoch = case year
        when 1607..1777 then "Colonial Period"
        when 1778..1812 then "Early Republic"
{% endhighlight %}

* Use an empty line before the return value of a method (unless it only
  has one line), and an empty line betwee `def` declarations.

{% highlight ruby %}
def some_method
  do_something
  do_something_else

  result
end

def do_something
  result
end
{% endhighlight %}

* Use [RDoc](http://rdoc.sourceforge.net/) and its conventions for documentation ([SDoc](http://rubygems.org/gems/sdoc) may be used to generate more searchable documentation).
* Use empty lines to break up a method in to logical paragraphs.
* Keep lines to fewer than 80 characters.

## Syntax
* Use `def` with parentheses when there are arguments. Omit parentheses
  when the method does not accept any arguments

{% highlight ruby %}
def some_method
  # payload
end

def method_with_arguments(arg1, arg2)
  # payload
end
{% endhighlight %}

* Never use `for`, unleass you know exactly why. **Iterators** should be
  used instead

{% highlight ruby %}
arr = [1, 2, 3]

# bad
for elem in arr do
  puts elem
end

# good
array.each { |elem| puts elem }

{% endhighlight %}

* Never use `then` for multi-line `if/unless`

{% highlight ruby %}
# bad
if some_condition then
  # payload
end

# good
if some_condition
  # payload
end
{% endhighlight %}

* Favor ther ternary operator over `if/then/else/end` constructs. It's
  more common and concise.

{% highlight ruby %}
# bad
result = if some_condition then something else something_else end

# good
result = some_condition ? something : something_else
{% endhighlight %}

* Use one expression per branch in a ternary operator. This also means that ternary operators must not be nested. Prefer `if/els`e constructs in these cases.

{% highlight ruby %}
# bad
some_condition ? (nested_condition ? nested_something : nested_something_else) : something_else

# good
if some_condition
  nested_condition ? nested_something : nested_something_else
else
  something_else
end
{% endhighlight %}

* Use `&&` and `||` for boolean expressions. Use `and` and `or` for flow
  control. 

{% highlight ruby %}
# boolean expression
if some_condition && some_other_condition
  do_something
end

# control flow
document.saved? or document.save!
{% endhighlight %}

* Avoid multi-line ternary operations, use `if/unless` instead
* Favor modifier `if/unless` usage when you have a single-line body.
 
{% highlight ruby %}
# bad
if some_condition
  do_something
end

# good
do_something if some_condition

# another good option
some_condition and do_something
{% endhighlight %}

* Favor `unless` over `if` for negative conditions (or control flow
  `or`)

{% highlight ruby %}
# bad
do_something if !some_condition

# good
do_something unless some_condition

# another good option
some_condition or do_something

{% endhighlight %}

* Suppress superfluous parentheses when calling methods, but keep them
  when calling "functions", i.e. when you use the return value in the
  same line.

{% highlight ruby %}
x = Math.sin(y)
array.delete e
{% endhighlight %}

* Prefer {...} over do...end for single-line blocks.  Avoid using {...} for
  multi-line blocks.  Always use do...end for "control flow" and "method
  definitions" (e.g. in Rakefiles and certain DSLs.)  Avoid do...end when
  chaining.

* Avoid `return` where not required.

{% highlight ruby %}
# bad
def some_method(some_arr)
  return some_arr.size
end

# good
def some_method(some_arr)
  some_arr.size
end
{% endhighlight %}

* Avoid line continuation (\\) where not required. In practice, avoid using
  line continuations at all.

{% highlight ruby %}
# bad
result = 1 - \
         2

# good (but still ugly as hell)
result = 1 \
         - 2
{% endhighlight %}

* Using the return value of = is ok.

{% highlight ruby %}
if v = array.grep(/foo/) ...
{% endhighlight %}

* Use ||= freely.

{% highlight ruby %}
# set name to Bozhidar, only if it's nil or false
name ||= "Bozhidar"
{% endhighlight %}

* Avoid using Perl-style special variables (like $0-9, $`, ...).
* The annotation keyword is followed by a colon and a space, then a note
  describing the problem.

* If multiple lines are required to describe the problem, subsequent
  lines should be indented two spaces after the `#`.

{% highlight ruby %}
def bar
  # FIXME: This has crashed occasionally since v3.2.1. It may
  #   be related to the BarBazUtil upgrade.
  baz(:quux)
end
{% endhighlight %}

* In cases where the problem is so obvious that any documentation would
  be redundant, annotations may be left at the end of the offending line
  with no note. This usage should be the exception and not the rule.

{% highlight ruby %}
def bar
  sleep 100 # OPTIMIZE
end
{% endhighlight %}

* Use `TODO` to note missing features or functionality that should be
  added at a later date.

* Use `FIXME` to note broken code that needs to be fixed.

* Use `OPTIMIZE` to note slow or inefficient code that may cause
  performance problems.

* Use `HACK` to note code smells where questionable coding practices
  were used and should be refactored away.

* Use `REVIEW` to note anything that should be looked at to confirm it
  is working as intended. For example: `REVIEW: Are we sure this is how the
  client does X currently?`

* Use other custom annotation keywords if it feels appropriate, but be
  sure to document them in your project's `README` or similar.

## Classes

* Always supply a proper `to_s` method.
* Use the `attr` family of functions to define trivial accessors or
  mutators.
* Consider adding factory methods to provide additional sensible ways
  to create instances of a particular class.
* Prefer duck-typing over inheritance.
* Avoid the usage of class (@@) variables due to their "nasty" behavior
  in inheritance.
* Assign proper visibility levels to methods (`private`, `protected`)
in accordance with their intended usage. Don't go off leaving
everything `public` (which is the default). After all we're coding
in *Ruby* now, not in *Python*.

## Exceptions

* Don't suppress exceptions.
* Don't use exceptions for flow of control.
* Avoid rescuing the `Exception` class.

## Strings

* Prefer string interpolation instead of string concatenation:

{% highlight ruby %}
# bad
email_with_name = user.name + ' <' + user.email + '>'

# good
email_with_name = "#{user.name} <#{user.email}>"
{% endhighlight %}

* Prefer single-quoted strings when you don't need string interpolation or
  special symbols such as `"\t"`, `"\n"`, etc.
* Avoid using `String#+` when you need to construct large data chunks.
  Instead, use `String#<<`. Concatenation mutates the string instance in-place
  and is always faster than `String#+`, which creates a bunch of new string objects.

{% highlight ruby %}
# good and also fast
html = ''
html << '<h1>Page title</h1>'

paragraphs.each do |paragraph|
  html << "<p>#{paragraph}</p>"
end
{% endhighlight %}

## Percent Literals

* Use `%w` freely.

{% highlight ruby %}
STATES = %w(draft open closed)
{% endhighlight %}

* Use `%()` for single-line strings which require both interpolation and embedded double-quotes. For multi-line strings, prefer heredocs.

{% highlight ruby %}
# bad (no interpolation needed)
%(<div class="text">Some text</div>)
# should be '<div class="text">Some text</div>'

# bad (no double-quotes)
%(This is #{quality} style)
# should be "This is #{quality} style"

# bad (multiple lines)
%(<div>\n<span class="big">#{exclamation}</span>\n</div>)
# should be a heredoc.

# good (requires interpolation, has quotes, single line)
%(<tr><td class="name">#{name}</td>)
{% endhighlight %}

* Use `%r` only for regular expressions matching *more than* one '/' character.

{% highlight ruby %}
# bad
%r(\s+)

# still bad
%r(^/(.*)$)
# should be /^\/(.*)$/

# good
%r(^/blog/2011/(.*)$)
{% endhighlight %}

* Avoid `%q`, `%Q`, `%x`, `%s`, and `%W`.

* Prefer `()` as delimiters for all `%` literals.

## Misc

* Write `ruby -w` safe code.
* Avoid hashes as optional parameters. Does the method do too much?
* Avoid methods longer than 10 LOC (lines of code). Ideally, most methods will be shorter than
  5 LOC. Empty lines do not contribute to the relevant LOC.
* Avoid parameter lists longer than three or four parameters.
* Use `def self.method` to define singleton methods. This makes the methods
  more resistant to refactoring changes.

{% highlight ruby %}
class TestClass
  # bad
  def TestClass.some_method
    # body omitted
  end

  # good
  def self.some_other_method
    # body omitted
  end

  # Also possible and convenient when you
  # have to define many singleton methods.
  class << self
    def first_method
      # body omitted
    end

    def second_method_etc
      # body omitted
    end
  end
end
{% endhighlight %}

* If you really have to, add "global" methods to Kernel and make them private.
* Use class instance variables instead of global variables.

{% highlight ruby %}
#bad
$foo_bar = 1

#good
class Foo
  class << self
    attr_accessor :bar
  end
end

Foo.bar = 1
{% endhighlight %}

* Avoid `alias` when `alias_method` will do.
* Use `OptionParser` for parsing complex command line options and
  `ruby -s` for trivial command line options.
* Write for Ruby 1.9. Don't use legacy Ruby 1.8 constructs.
    * Use the new JavaScript literal hash syntax.
    * Use the new lambda syntax.
    * Methods like `inject` now accept method names as arguments.

{% highlight ruby %}
  [1, 2, 3].inject(:+)
{% endhighlight %}

* Avoid needless metaprogramming.

## Design

* Use common sense.
* Code in a functional way, avoiding mutation when that makes sense.
* Do not mutate arguments unless that is the purpose of the method.
* Do not mess around in core classes when writing libraries. (Do not monkey
  patch them.)
* [Do not program   defensively.](http://www.erlang.se/doc/programming_rules.shtml#HDR11)
* Keep the code simple (although this is subjective). Each method should have a single,
  well-defined responsibility.
* Avoid more than three levels of block nesting.
* Don't overdesign. Overly complex solutions tend to be brittle and hard to
  maintain.
* Don't underdesign. A solution to a problem should be as simple as
  possible, but no simpler than that. Poor initial design can lead to a lot
  of problems in the future.
* Be consistent. In an ideal world, be consistent with these guidelines.
