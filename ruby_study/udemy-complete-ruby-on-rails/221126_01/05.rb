print "What is your first name: "
first_name = gets.chomp
puts
print "What is your last name: "
last_name = gets.chomp
puts

puts "Hi, #{first_name} #{last_name}. How are you doing?"
gets.chomp
full_name = "#{first_name} #{last_name}"
reversed_full_name = full_name.reverse!
puts "This is you name reversed: #{reversed_full_name}."
gets.chomp
num_chars = full_name.length - 1
puts "Your name has #{num_chars} characters in it."
gets.chomp


