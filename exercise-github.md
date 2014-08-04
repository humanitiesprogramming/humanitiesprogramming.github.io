---
layout: exercise
title: Github Pages
description: Create a simple Github User repository
permalink: /exercises/github/
---

In this exercise we will be creating a new `git` repository **remote** at
[Github][github].

## Create a New Respository

1. Navigate your web browser to [http://github.com/new][new-repo].
2. For the **Repository Name**, enter `username.github.io`. Use your
   **actual username**, *or this will not work*!
3. Make the repository **Public**.
4. Check the **Initialize this repository with a README** option.

<img class="img-responsive" src="{{"/assets/img/exercises/new-repo.png" | prepend: site.baseurl}}" alt="new github repository">

## Fire Up Your Terminal

In this step, you will download (`clone`) the files in the repository
you just created.

### Create a project directory

In the terminal, create a new directory (`mkdir`) and navigate to it
(`cd`).

{% highlight console %}
$ mkdir -p ~/projects/
$ cd ~/projects
{% endhighlight %}

### Clone the Repository

Go back to your browser that has the newly create repository. On the
right-hand side, you'll see a section that says "**SSH** clone URL".
Copy the contents, or just replace the following with your valid
information.

{% highlight console %}
$ git clone git@github.com:username/username.github.io.git
$ cd username.github.io
{% endhighlight %}

### Check Your Directory

We can check out the contents of the directory. We should have a
directory with just a single file. We can check this in the terminal by
listing (`ls`) the files in the directory.

{% highlight console %}
$ ls
README.md
{% endhighlight %}

But are those the only files? What happens if you pass the `-a` flag to
`ls`?

### Creating a New File

We will keep this pretty light, for now. We will create an exceptionally
simple web page and push it back to Github.

Create a new file with your name in it in the terminal using the
concatenate command (`cat`) and output redirection (`>`).

{% highlight console %}
$ echo "Hello, my name is Sparticus!" > index.html
{% endhighlight %}

Now we need to check the status of the repository.

{% highlight console %}
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	index.html

nothing added to commit but untracked files present (use "git add" to track)
{% endhighlight %}

Reading the message, we see we need to run `git add` since this is a new
file. If we run `git
status` after adding the file, we'll see its status has changed.

{% highlight console %}
d$ git add index.html
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   index.html
{% endhighlight %}

Git now knows that you want to track the file, but we have to now
actually commit the change to the database, with a message about what we
did at this point.

{% highlight console %}
$ git commit -m "My first commit declaring that I am Sparticus" index.html
[master e48bd94] My first commit declaring that I am Sparticus
 1 file changed, 1 insertion(+)
 create mode 100644 index.html
{% endhighlight %}

Now we can push the master branch of the repository to Github. When we cloned the repository, `git`
automagically set a remote of "origin" for us.

{% highlight console %}
$ git push origin master
Counting objects: 8, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (8/8), 865 bytes | 0 bytes/s, done.
Total 8 (delta 0), reused 0 (delta 0)
To git@github.com:waynegraham/test.git
   1115c8c..c55075c  master -> master
{% endhighlight %}

## A Github Page

Refresh the repository page you had open. You should see the
`index.html` file you just created. Now, here's the crazy part...point
your browser to **http://username.github.io** (where username is your
username). What happens?

## Recap
Congratulations, you just did a full development cycle! You created a
new repository to share your code, cloned it to your development
environment, created new content, and pushed/deployed your code. You
also saw that there are several stages of using `git`...adding new files
and committing them to the git repo. These two steps have to happen
before you're able to `push` the code to the server to share. This can
be a bit confusing at first, but the `git status` command will always
tell you what stage you are at in the process.

[github]: http://github.com
[new-repo]: http://github.com/new
