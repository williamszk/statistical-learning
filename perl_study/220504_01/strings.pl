use strict;
use warnings;
use diagnostics;

use feature 'say';

use feature "switch";

my $long_string = "My random long string";

say "Length of string ", length $long_string;


# how to find the index of a certain word in the string?
printf("Long is at %d\n", index $long_string, "long");
# -1 returns when the pattern does not exist  

# how to find the index of the last occurance of some word
# or letter

printf("Last g is at %d \n", rindex $long_string, "g");

# how to concatenate strings
$long_string = $long_string . ' isn\'t that long';

say $long_string;

# getting substrings
say "Index 7 through 10 is: ", substr $long_string, 7, 4;
# the last argument of substr function is the number of 
# chars that we'll select

# using chop to extract the last character of a string
# it will delete and return the last character
my $animal = "animals";
printf("Last character is %s\n", chop $animal);

printf("Uppercase: %s\n", uc $long_string);
# note that we use the function "uc"
printf("Lowercase: %s\n", lc $long_string);

# we can make the upper case and lower case first
printf("1st Uppercase: %s\n", ucfirst "apple");

# using replacement of chars
# the command is similar to vim
# note that we need to use the tilde =~
$long_string =~ s/ /, /g;
# we substitue " " by ", "
# g means that it is global
say $long_string;

# we can duplicate or multiply the string
my $two_times = "What I said... " x 2;
# note that we include x the letter
say $two_times;

# using range for letter and numbers
my @abcs = ('a' .. 'z');
say @abcs;

my @numbers = (1 .. 5);
say @numbers;

# we can use the function join to concatenate all chars in
# an array
print join(", ", @abcs), "\n";
# we can use , to separate arguments from the
# the function print

# we can increment letters
my $letter = "c";
say "Next letter: ", ++$letter;

# is this following ascii? 
# or it supports unicode?
my $letter_z;
say "Next letter from z is: ", ++$letter_z;
# this gives the character 1

