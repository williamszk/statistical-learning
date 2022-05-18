use strict;
use warnings;
use diagnostics;

use feature 'say';

use feature "switch";

# this will use a specific version of perl
# use v5.16;

print "Hello World!\n";

# data types
# scalars
# arrays
# hashes

# sigul? $

my $name = 'William';

my ($age, $street) = (40, '123, Oxford St');

# single quotes are simpler than double quotes in perl
# in double quotes we can include string interpolation

my $my_info = "$name lives on \"$street\"\n";
# we can include \" and \n for special characters

print $my_info;
# is perl an interpreted language?

# we use the keyword "my" to declare a variable

# what happens if we use a variable that is not declared?
# $a_variable = 2;
# Global symbol "$a_variable" requires explicit package name 
# (did you forget to declare "my $a_variable"?) at perltut01.pl line 38.
# It gives an error...

# we can change the internal value of the variable without redeclaring it
$my_info = "Hello there\n";
print $my_info;

$my_info = qq{$name lives on "$street"\n};
# qq{} will start a double quotes

print $my_info;

# define long strings over multiple lines
my $bunch_of_info = <<"END";
This is a bunch 
of information
in multiple
lines.
END

say $bunch_of_info;

# the largest integer
my $big_int = 18446744073709551615;
# it is a 64 bit integer

# we can use printf also
# %c: character
# %s: string
# %d: decimal
# %u: unsigned integer
# %f: floating number (decimal notation)
# %e: floating number (scientific notation)


printf("%u\n", $big_int);
printf("%u\n", $big_int+1);
# although we summed +1 the number didn't go up
# nor we had overflow
# when we sum to the maximum value of an integer
# the integer stays at the maximum

my $big_float = .1000000000000001;
# the max values if 16 digits after the point

printf("%f\n", $big_float);
# we need to include .16 after the %f to indicate that we want to see all 16 digits
printf("%.16f\n", $big_float);

# the answer is correct because we are in the range of the possible values of float
printf("%.16f\n", $big_float + .1000000000000001);

# the answer is incorrect because we are out the 16 of precision range of float
printf("%.20f\n", $big_float + .000000000000000023456);


my $first = 1;
my $second = 2;
say qq{first: $first, second: $second};
# how to switch the values?
($first, $second) = ($second, $first);
say qq{first: $first, second: $second};

# math functions of perl
say "5 + 4 = ", 5 + 4;
say "5 - 4 = ", 5 - 4;
say "5 * 4 = ", 5 * 4;
say "5 / 4 = ", 5 / 4;
say "5 % 4 = ", 5 % 4;
say "5 ** 4 = ", 5 ** 4;

# some common math perl functions
# interestingly we don't need to use () to pass arguments to the function
say "exp 1 = ", exp 1;
say "hex 10 = ", hex 10;
say "oct 10 = ", oct 10;
say "int(6.45) = ", int(6.45);
say "log 2 = ", log 2;
say "random between 1 - 10: ", int(rand 11);
say "sqrt 9 = ", sqrt 9;
# ruby has this behavior of using arguments without parenthesis
# how can we pass functions are arguments if the function doesn't 
# know when it is been called?

# shortcut assignment operators
# +=
# -=
# *=
# /=
# ++

my $my_num_01 = 5;
$my_num_01 += 3;
say $my_num_01;

$my_num_01++;
say $my_num_01;

# what is the difference between
# a++
# ++a
# it is the order of execution

my $my_num_02 = 6;
say "6++ = ", $my_num_02++; # 6
say "++7 = ", ++$my_num_02; # 8
say "8-- = ", $my_num_02--; # 8
say "--7 = ", --$my_num_02; # 6

# operation precedence in programming
say "3 + 2 * 5 = ", 3 + 2 * 5;
say "(3 + 2) * 5 = ", (3 + 2) * 5;


# conditionals

# falsy values
# undef, 0, 0.0, "", "0", 

# conditional logic
# ==, !=, <, >, <=, >=, 

# boolean operations
# ! (not), &&, ||, 

my $age = 80;

my $is_not_intoxicated = 0;
# aren't there boolean values?

my $age_last_exam = 16;

if ($age < 16){
    say "You can't drive";
} elsif (!$is_not_intoxicated){
    # notice that it is elsif, not elif
    say "You can't drive";
} else {
    say "You can drive";
}

if (($age >= 1) && ($age < 16)){
    say "You can't drive";
}

if ($age >= 1 && $age < 16){
    say "You can't drive";
}
# we don't need the internal parenthesis

# is there switch in perl?

if ($age >= 1 && $age < 16) {
    say "You can't drive";
} elsif(!$is_not_intoxicated) {
    say "You can't drive";
} elsif ($age >= 80 && ($age > 100 || $age - $age_last_exam > 5)){
    # people above 100 years cannot drive
    # if you have more than 80 you need to have the 
    # the last exam in less than 5 years to be able to drive
    say "You can't drive";
} else {
    say "You can drive";
}


# comparison operators with strings

# eq, ne, lt, le, gt, ge, 

if ('a' eq 'b') {
    say "a equals b";
} else {
    say "a doesn't equal to b";
}

if ('banana' eq 'banana') {
    print "Banana!\n";
}

# what is the differece using "" or using ''
# or using q{} and qq{}

# and what is the difference between say, print and printf

unless (0){
    say "Ran inside unless!";
}
# the code from unless will run if its condition
# is false, the oposite of if

# ternary operator
say $age > 18 ? 'Can vote' : "Can't vote";

# how looping works
# https://youtu.be/WEghIXs8F6c?t=1389

