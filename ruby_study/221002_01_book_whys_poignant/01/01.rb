
5.times { print "Odelay!" }

['toast', 'cheese', 'wine'].each{|food| print food.capitalize}


# are varibles in ruby like bindings as it is in javascript?

my_var_01 = 1
my_var_02 = my_var_01

puts
puts("my_var_01:",my_var_01)  
puts("my_var_02:",my_var_02)  

# change the content of my_var_01
my_var_01 = 22

puts("After the change:")
puts("my_var_01:",my_var_01)  
puts("my_var_02:",my_var_02)  

# my_var_01:
# 1
# my_var_02:
# 1
# After the change:
# my_var_01:
# 22
# my_var_02:
# 1

# When dealing with atomic data such as numbers the variable behaves like a box
# that is the variable does not behave like a tentacle.

# Let's experiment with doing the same with a compesed type like the list
my_list_01 = [0,1,2]
my_list_02 = my_list_01
print("my_list_01:",my_list_01,"\n")  
print("my_list_02:",my_list_02,"\n")  

my_list_01[0] = 199
puts("After the change:")
print("my_list_01:",my_list_01,"\n")  
print("my_list_02:",my_list_02,"\n")  
# my_list_01:[0, 1, 2]
# my_list_02:[0, 1, 2]
# After the change:
# my_list_01:[199, 1, 2]
# my_list_02:[199, 1, 2]

# Note that both lists changed which means that variables in ruby 
# behave like tentacles when the data type is a container

# about integers
population = 12_000_000

# about floats
3.14
12.09e-04

# in ruby single or double quotes have the same effect
"sealab"
'2921'

# something special about ruby are symbols
:a 
:b
:ponce_de_leon

# symbols are lighweight strings
# symbols are used in situations where you need some kind of string
# to convey meaning but you do not intend to print it

# about constants
Time
Array
Bunny_Lake_Is_Missing

EmpireStateBuilding = "350 5th Avenue, NYC, NY"


# variables that begin with a dollar sign are global variables
$x
$1
$chunky
$Chunky_Bacon

# about instance variables
@x
@y
@chunky_bacon
# those attribute variables of a class

# class variables
# those are variables that are valid for the class and not 
# hust instaces of the of the class 
@@x
@@y
@@i_will_take_your_chunkiest_bacon_and_raise_you_two
# we can think of the double @@ as attribute all

# code block
# we can use curly braces 
# but we can also use do and end
loop do
    print "Much better!"
    print "Ah more space!"
    print "My back was killing me in those crab pincers"
end

# block arguments
# we use the pipe symbol to define block arguments
|x|, |en|
# block arguments are used in the beginning of blocks
{|x,y| x+y }

# blocks and block arguments can act like labda expressions   

# ranges 
# 
(1..2)
('a'..'z')
# rust uses this kind of syntax too


























