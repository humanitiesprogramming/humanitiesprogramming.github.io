---
layout: page
title: Git Cheatsheet
permalink: /resources/git-cheatsheet/
---

# Git
* Distributed Version Control.
* Distributed in the sense that many copies of your work exist in many places.
* Versioned in the sense that it keeps track of every change you make to every document ever.
* Control in the sense that you can go back to any old version, change the past, affect the future, etc.

## Git Cheatsheet

* $ git init
    * Turns a plain old folder into a git repository that is versioned and ready to track its history (involves making a lot of hidden files and interacting with them).
* $ git status
    * Tells you the current state of your directory
* $ git add .
    * Adds everything in your current directory to the staging site.
* $ git commit -m "message"
    * Takes the current changes you have made and stores them in the longterm memory of the system. Every commit is stored as a series of changes to particular lines and comes with a message describing the changes, the user who made them, and the time.
* $ git branch branchname
    * Makes a new branch named branchname, allowing you to test out new changes and features that you want to add.
* $ git checkout branchname
    * Change from the master branch to branchname. Any changes you make now will be committed to branchname and will not affect master. You can work happily knowing that your work won't override the official copy of things.
* $ git merge branchname
    * Take the differences on branchname and combine them with the current branch. Used for when you have work you have decided is good enough to be part of the public record.
* $ git log
    * Get the history of the repository's commit messages.
* $ git log --graph
    * Get a pretty visual history of the repository. It will try to graph branches and merges for you.
* **repository**: another word for a project. Consists of files and folders.

## Git Exercises
1. Make a git repository
2. Change into it.
3. Make a text file.
4. Make some changes to that file.
5. Commit them.
6. Repeat a few times.
7. Make a branch and switch to it.
8. On this new branch, make a really noticeable change to the file.
9. Change back and forth between your branch and master to see the files change.