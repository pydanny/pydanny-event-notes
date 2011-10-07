==========================================
The Prejudgement of Programming Languages
==========================================

* by Gary Bernhardt
* runs `Destroy all software`

Alternative Title: 10 years of failures and bad mistakes

2001-
=====

* Used to be ignorant of software

2001
====

* C is the best thing!
* Java Sucks cause it has garbage collection
* Programming is supposed to be hard, right?

2003
====

* Learned Lisp
* Started his own crazy language
* But Python did the same thing, so went with that instead
* Python <3

2006
=====

* Exhausted by his company, Python
* BitBacker


2009
====

* Started doing Ruby/Python 50/50
* Every day of the year switched languages halfway through

Quotes of the time:

* "I can integrate Python lib in 10 minutes, Ruby lib in an hour..."
* "Ruby syntax tricks can be hard, but other languages might want to take note"
* "Wrote a Python specer that would have been trivial to do in Python"

Not sure Ruby is serious cause the docs have some crazy stuff

Q2 2010
=======================

Writing tests in python:

.. sourcecode:: python

    class TestCount(UnitTest):
    
        def test_counter(self):
            
            c = Counter()
            c.count(1)
            self.assertEquals(1, c)

Writing tests in ruby:

.. sourcecode:: ruby

    require 'counter'
    describe Counter do
        if "increments" do
        c = Counter.new
        expect { c.increment }.to change { c.count }.by(1)
    end
    
    
* claim: "RSpec is confusing" 

    * But not really true
    * Feigned ignorance
    
* Python is based off of SUnit: 1994

Awesome tweet he made: "**Python programmer rejects without considering its value, Ruby accept without considering it's value**"

Instance Variables in Ruby
=============================

* Ugly things in Ruby

.. sourcecode:: ruby

    class Horse
    
        def what
            @mustard
        end
    end
    puts Horse.new.what # => 5

* Really? Let's take another look...

.. sourcecode:: ruby

    class Horse
    
        def what
            @mustard ||= compute_it
        end
    end
    puts Horse.new.expensive
    
* This is how you do memoization in Ruby.
* Really trivial to do something really important

