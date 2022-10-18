print "Hello World\n";

# escape sequence

# scalars use $
$my_var = "5 is different from \"five\"\n";
print $my_var;

print "Do you hear the bell?\a\n";
# what \a does?
# the \a should produce a sound...

# using singles quotes the escape sequence does not work
$my_var_2 = '5 is different from \"five\"\n';
print $my_var_2;
print "\n";

# what \u does?
print "The odd \uone out\n";
# The odd One out

print "MY \lNEW GUITAR!\n";
# MY nEW GUITAR!

print "the next \Ucase\n";
# the next CASE

print "THE LAST \LCASE\n";
# THE LAST case

print "\Q!@#^&*_+";
# \!\@\#\^\&\*_\+
# it seems that it quit everything