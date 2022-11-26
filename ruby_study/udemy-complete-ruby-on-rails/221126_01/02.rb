# string concatenation
name = "William"
print "My name is " + name + "." + " Pleased to meet you."
puts

# string interpolation
print "My name is #{name}. Pleased to meet you."
puts

# check the class of an object
print "name".class
puts
print 10.class
puts
print 90.2.class
puts

# In Ruby everything is an object
# so the primitive data types also have methods
# This is not true in Java, for instance

# List the methods of an object
print "Tomy".methods
puts

print 10.methods
puts

print "-------------------------------\n"
# convert integer to string
print ">>>>>>>>>>>>>> " + 10.to_s + "\n"

# method chaining
print 10.to_s.class
puts

letters = "abcdedf"
print letters
puts
print letters.reverse
puts

# check if string is empty
a_str = ""
p a_str.empty? # true
p a_str 

# check if an object is nil
p a_str.nil? # false
p nil.nil? # true

p 0.nil? # false

# substitute strings
sentence = "Welcome to the jungle"
sentence_2 = sentence.sub("the jungle", "utopia")
p sentence
p sentence_2



