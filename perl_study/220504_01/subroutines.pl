# https://youtu.be/WEghIXs8F6c?t=2912


use strict;
use warnings;
use diagnostics;

use feature 'say';

use feature "switch";

# subroutines are like functions

sub get_random {
    return int(rand 11);
}

say "Random number ", get_random();

sub get_random_max {
    my ($max_num) = @_; # the arguments will be stored at this @_
    $max_num ||= 11; # this is a default value in case $max_num was not defined
    return int(rand $max_num);
}

say "A random number ", get_random_max(20);

sub experiment_sub {
    say "Arguments passed: ", @_;
}

experiment_sub "This is an argument";
experiment_sub(10);
experiment_sub 99.99;

experiment_sub 99.99, "Bob";

sub experiment_sub_2 {
    say "Arguments 0: ", $_[0];
    say "Arguments 1: ", $_[1];
    # why in here we use $ instead of @?
    # $ will return an Scalar
    # @ will return an array
    # 
}

experiment_sub_2 10, "bob";

# what if we define a subroutine that expects one argument
sub experiment_sub_3 {
    say "2. Argument: ", $_; # this doesn't work... strange
}

# experiment_sub_3 20;

# I think that we need to pass @_ first 
# I think that _ is the default way to capture values passed as arguments
# _ can be just a scalar
# or _ can be an array

# the problem with this syntax is that we can include any number
# of arguments in a subroutine that shouldn't receive it
# this could be caught in compile time, or by the IDE
# not in Perl or maybe in other interpreted languages

sub sum {
    # unpacking
    my ($num1, $num2) = @_;

    # we can define default values if the arguments are not passed
    $num1 ||= 0;
    $num2 ||= 0;

    return $num1 + $num2;
}

say "sum 2, 1 = ", sum 2,1;

say "sum = ", sum;

say "sum 1 = ", sum 1;

# what happens if we pass more argument than necessary?

say "sum 1 2 3= ", sum 1, 2, 3;
# I think that they just ignore the other arguments


# how to pass n number of values
sub sum_many {
    my $sum = 0;

    foreach my $val (@_){
        $sum += $val;
    }

    return $sum;
}

say "Sum: ", sum_many(1,2,1,1,1,1);

my $execute_total;
# we can increment global variables
sub increment {
    # state $execute_total = 0;
    # using the line above gave me an error...
    $execute_total ++;
    say "Executed $execute_total times";
}

increment();
increment();

# we can return multiple values
sub double_array {
    # this function doubles the values of the array passed as an argument
    my @num_array = @_;
    $_ += 2 for @num_array; # this is like a list comprehension, but it is in place
    # this will return an array of values
    return @num_array;
}

my @array_01 = (1,2,3,4,5);

say "using double_array = ", double_array @array_01;

print join(", ", double_array(@array_01)), "\n";

# return multiple arguments
sub get_mult {
    my ($rand_num) = @_;

    $rand_num ||= 1;

    return $rand_num*2, $rand_num*3;
}

my ($num_2, $num_3) = get_mult(3);

say "num_2 = $num_2, num_3 = $num_3";

# recursions 
# an example with factorial
sub factorial {
    my ($num) = @_;
    return 0 if $num <= 0;
    return 1 if $num == 1;
    return $num * factorial($num - 1);
}

say "Factorial 4 = ", factorial 4;
say "Factorial 3 = ", factorial 3;


# next : file io
# https://youtu.be/WEghIXs8F6c?t=3363



