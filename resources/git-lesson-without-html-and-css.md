---
layout: page
title: Git Lesson
permalink: /resources/git-lesson-without-html-and-css/
---

# Intro to Git

We've talked at a very basic level about how to work with the computer, but today we're going to start talking about how to put together actual projects - complex works with many moving pieces and many collaborators. Git is one basic tool that helps facilitate large projects.

We are all used to working in Microsoft word, saving as we go. But it's relatively difficult in Word to access older versions of your document. Say, after weeks of work you decide you want to get rid of several days worth of edits. Very difficult to do - they're all embedded in the one document. Git is a piece of software that enables you to get past this limitation. It enables what we call version controlling, a way of controlling and maintaining different versions of your software at one time.

When we use git we tell the computer to take snapshots of our work at different times throughout it's history. We work with files until we decide we want to take a snapshot of them. Then we take a snapshot and commit it to the memory of the database. At any time we can go back and recover virtually any stage of the process. It makes working much less scary. Nothing is lost forever, because we can easily recover files from different points in the past. Because we have full versions of the code at various points in time, we can also do some fairly fancy tricks where we allow different versions of the code to exist alongside each other.

Git also allows people to collaborate easily, which we will cover in a separate lesson.

There is a particular workflow that characterizes this use of version controlling.

Workflow

* Modify a file (in a text editor)
* Add that file to the staging area ($git add file_name)
* Commit it to the repository ($git commit)
* Work some more.

The reason to have a workflow like this is because you don't want to save EVERYTHING. Sometimes you want to just mess around to get something to work. But when you're satisfied that you're ready, you have to get things through to the commit stage before they're actually saved permanently to the history of the repository. Until then, they're in git's short-term memory.

First, an example.

We're going to practice using Git by editing and saving different versions of a text file. Specifically, a beautiful poem, every version of which we want to save for posterity. Because we're #programmers now, to do this we will use a text editor (such as Atom or Sublime Text) for our textual content rather than an application like Microsoft Word. First, however, we need somewhere to house this text file. So let's make a folder precious_poems using the terminal and change into it.

{% highlight bash %}
$ mkdir precious_poems
$ cd precious_poems
{% endhighlight %}

A folder is a folder until you make it git-ready. Then it becomes a repository. We have to tell the computer that we want to use git to trace the version history of this folder. So the first thing to do is "initialize" a git repository. Intuitive command line here:

{% highlight bash %}
$ git init
{% endhighlight %}

You should get some feedback saying you initialized an empty repository. Success! We have a folder with nothing in it. Like gods, the world is a blank canvas for us to play with. And with that blank canvas we will be making... poetry. Just what the world wanted. Anyways, now we have our staging area. Create an empty text file roses.txt:

{% highlight bash %}
$ touch roses.txt
{% endhighlight %}

Now copy and paste [this](https://humanitiesprogramming.github.io/assets/git-text-files/roses.txt) text into that file.

Truly, an amazing poem. Who could have crafted this work of untold genius?? Right. Let's paste it in, save it, and take a look at this new command:

{% highlight bash %}
$ git status
{% endhighlight %}

We've modified something but not staged it.

Pretty intuitive - git status tells us what is going on in our git project. And it tells us what to do next - add the files so that they will be tracked and staged. Let's do that and hit status again.

{% highlight bash %}
$ git add roses.txt
$ git status
{% endhighlight %}

Now we have things staged but not committed just yet.

{% highlight bash %}
$ git commit -m "Initial idea for poem."
{% endhighlight %}

The git commit command, perhaps obviously, commits our changes to the snapshot history of the repository. It stores it in the history of the repo. The -m let's us give it a message. We need to give detailed messages so that we can tell what changes we made at which points in the history of the repository. Simply having different chunks of code is useful, but not as useful as giving human readable notes about the changes you've made. Imagine someone looking at a list of all the changes you made over a two-year period - you want them to be able to quickly find the particular change that they are interested in.

Success! Now we have finished the process of committing, and the working area goes back to the beginning. We also get a dot on the git tree.

*Note: in the actual workshop we draw on the board to track the progress of the directory. You can follow along at home!*

Let's keep going. As it currently stands, our initial idea for a poem is just that: an initial idea. But now we've decided that we need to make a few edits to really capture the epic *feel* of what we were going for. This poem needs multiple stanzas. And allusions to other poets! So copy and paste from [this link](https://humanitiesprogramming.github.io/assets/git-text-files/roses2.txt) into the same file, overwriting all the old stuff.

Where are we in the workflow? We've modified. What happens next? We stage. How do we do that?

{% highlight bash %}
$ git add .
{% endhighlight %}

The . tells the terminal to apply the command to everything in the directory. So it's a shorthand for saying "add everything." Now we commit.

{% highlight bash %}
$ git commit -m "Added some style."
{% endhighlight %}

Now we modify the tree on the board with another dot.

Now our next edit. Totally new vision for this poem, punctuation-wise. Also getting rid of a few things. Copy the text from [here](https://humanitiesprogramming.github.io/assets/git-text-files/roses3.txt
).

Before we move on, let's learn a new command. Some of the changes here are more subtle, so let's say that we want to know what they are.

{% highlight bash %}
$ git diff
{% endhighlight %}

This command tells us what we have modified. It works going through the two files and comparing them line by line to see what is added and what is removed. Hence the positive and negative signs on the left margin. So looking down that column we can see what has changed. Git actually stores the history of the project like this, as a series of additions and subtractions.

Let's go through the process again - edit, add, and commit. Can you do this without me telling you the commands again?

At this point we have three commits, three distinct moments in the history of the project. Things are getting complicated. Say that we want to know what has changed up to this point.

{% highlight bash %}
$ git log
{% endhighlight %}

The git log command tells us the history of our commits to this point. Three commits with our beautiful messages. We can also reproduce the lovely tree that we've been building (important in a moment).

{% highlight bash %}
$ git log --graph
{% endhighlight %}

One thing to note here is that the log tells us what we've done in reverse order.

One last thing at this point. We want the poem to be longer, but don't feel like writing anything new for now. So copy the text [here](https://humanitiesprogramming.github.io/assets/git-text-files/roses4.txt
).

You tell me what to do. Yep - same pattern. Edit, add, commit

Remember - the -m option allows us to leave a message when we commit. So we'll do so again.

{% highlight bash %}
$ git commit -m "Added lorem ipsum to the poem."
{% endhighlight %}

An aside: Lorem ipsum is standard junk text used by typesetters throughout the centuries as they prepare their work.

*Note: at this point we sometimes stop depending on the budgeted time. But feel free to keep going!*

Branches

Because Git takes snapshots of all our code at different times, it is very easy to allow different versions of the same code to co-exist. Say we think we might want to try something different, but we're not certain that we want to go with the new option. Or, say we are working on a project with many collaborators. Git makes it easy for you to break up the project and have people working on very small tasks. You work on the individual thing until it's ready for primetime. This is where things get (even more) confusing. To go with our tree metaphor, our next command is:

{% highlight bash %}
$ git branch indent
{% endhighlight %}

This command takes the central tree and split it (gives it a branch) that we tell the computer to name 'indent'. We now have two different versions of the code that we can switch between - the source (master) branch and the 'indent' branch. The branch name usually identifies what we want the new feature to be, how we understand the branch to be distinct. In this case, we're going to try out some new formatting. Important to note here is that this new branch exists at the same time as the main tree (called master). I find it helpful to think of this like time travel. We're creating a parallel universe in which our text will be indented, but in the real, master universe things will remain the same. Let's move into that parallel universe. To switch the version of code you're looking at, the branch you're on, try this out:

{% highlight bash %}
$ git checkout indent
{% endhighlight %}

Now we are no longer in the main world. We are in the land of indentations.

Copy and paste this material onto that [same file](https://humanitiesprogramming.github.io/assets/git-text-files/roses4B.txt
) again.

Now we move through our standard workflow: edit, add, commit. But what happens to the tree. How would we represent that here graphically?

If we switch back and forth between master and indent, we can see how the different options look easily.

{% highlight bash %}
$ git checkout master
$ git checkout indent
{% endhighlight %}

Maybe we want to sit with that feature for a while. In the meantime, we've been toiling away on a fourth and final section to our poem that we are sure we want to keep. Move back on the master branch (we want to keep the indent branch clean and dealing only with the one feature - indentation.)

{% highlight bash %}
$ git checkout master
{% endhighlight %}

And add [this content](https://humanitiesprogramming.github.io/assets/git-text-files/roses5.txt
) to your roses.txt file.

Standard workflow: edit, add, commit with a message. Once we've committed, we'll update the tree drawing.

So now let's say we've made a choice. We know what we want to indent things. We want that we want that to be the new normal, not a parallel option. We want the new world to contain both a fourth section and indentation . We want to combine the changes from the secondary world with the primary one that we have been recording. First, get back to the master branch.

{% highlight bash %}
$ git checkout master
$ git merge indent
{% endhighlight %}

We're telling the computer we want to take the 'indent' branch and combine it with master, reuniting the two options and pulling the new information from the secondary branch. The result is one single branch with all our features combined. This is pretty common practice - you spend time on a feature, get it working, and when it's up to speed you bring it back into the main timeline. How would we represent this on our graph? The log --graph function will give us a hint.

{% highlight bash %}
$ git log --graph
{% endhighlight %}

Now, you can imagine if you were working on a project that required multiple files that interacted with one another - like a website, for example - all of this could get much more hectic. As it currently stands, we now have all versions of our awesome poem on record in case we want to see an earlier draft.

Can anyone guess why our indentation style didn't copy affect the bio page? Because it was a change in the style that was only made to the index.html page. How could we get around that? CSS! If the CSS were contained in a separate file we wouldn't have to worry about it.

Some final tips - branching gets very confusing when the same line of the same file is modified in different branches. When you try to merge them back together you get merge conflicts, which cause endless headaches. Be careful with your work, though, and you should be able to minimize these problems. And the good news is that, with git, you always have everything saved a million times over. So you won't lose anything.

So we've covered the basics - we have a workflow, this procedure gives us a history, and we can use version controlling to map out different states of the codebase as we work.
