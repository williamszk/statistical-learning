# https://www.udemy.com/course/the-complete-ruby-on-rails-developer-course/learn/lecture/8356460#overview

puts "Hello World"

p "Hello World"
# p is a little different than puts


greetings = "Hello"

puts greetings

print "Hello World!\n"

def say_hello(thing_to_say)
    puts thing_to_say
end

say_hello("I'm lerning ruby on rails")

# strings
"Ruby on Rails"
'Ruby on Rails'
# we can use single or double quotes
# with single quotes we can't do stirng interpolation

# string concatenation
first_name = "Bob"
last_name = "Martin"
puts first_name + last_name

puts "The author of clean code is #{first_name} #{last_name}"
# we can't use string interpolation with single quotes

full_name = "#{first_name} #{last_name}"
puts full_name

# irb

# to check the type/class
full_name.class
# String
"Dennis".class
# String

# they are pascal case, so it seems that they are classes
10.class
# Integer

10.09.class
# Float

# something that is different is that even the integer is an object
# because we can call methods from just 10
# which is something that is not possible with Python or Java

10.to_s # "10"
10.to_s.class # String
# method chainning

full_name.length
# 10

full_name.reverse
full_name
# if we include the ! sign it is going to be an inplace change

full_name.reverse!

# this is changed permanently
full_name


"apple".capitalize
# we don't need to use () to call a function...
# if it is not ambiguous
# what if we want to pass a function as argument or return
# of another function?

full_name.empty?
# the ? sign indicates that the return is boolean

full_name.empty?.class
# This is FalseClass

"".empty?

"".empty?.class
# TrueClass

"".nil?
# false
# it is a empty string, but it is not nil


0.empty? # this will give error

nil.empty? # this will give error

[].empty?
# true

nil.nil?
# true

sentense = "Welcome to the jungle"
sentense.sub("the jungle", "utopia")
# this is not replacing
# gsub is global replaces all coccurances

first_name
first_name.methods
# this will list all methods that we can run with a string

first_name = "Bob"
# this is passing by reference
new_first_name = first_name
new_first_name 
# so new_first_name and first_name point to the same spot in memory
# variables in ruby are labels not boxes

first_name = "Ken"
puts first_name # "Ken"
puts new_first_name # "Bob"
# first_name change the object that is pointing to

# single quotes is a string literal like `` in javascript and Go
















