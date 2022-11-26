
blue_crystal = 1
leaf_tender = 5

plastic_cup = nil

if plastic_cup
  print "plastic_cup is not nil"
end

my_phrase = ""
if my_phrase
  print "empty string is not false, that is true\n"
end

unless plastic_cup
  print "plastic_cup is negatively charged\n"
end

# use if and unless in a single line
puts "There is something in the plastic_cup" if plastic_cup
puts "Sorry, the plastic_cup is empty" unless plastic_cup

# use if and unless in a same expression
plastic_cup = 10 
glass_cup = nil
puts "We are using plastic_cup 'cause we don't have glass_cup" if plastic_cup unless glass_cup
# do something only if a is true and be is false

print "Hugo Boss" if true
puts

approching_guy = true
if approching_guy == true
  print "That necklace is classic."
  puts
end

if approching_guy == false
  print "Come here, you covening devil!"
  puts
end











