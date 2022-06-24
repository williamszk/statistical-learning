# https://youtu.be/WEghIXs8F6c?t=2131
# here we stoped at this part of the video
# we'll study with arrays in Perl

use strict;
use warnings;
use diagnostics;

use feature 'say';




my @primes = (2, 3, 5, 11, 13);

say @primes;

# include different types of information inside the array
my @personal_info = ("William", "My personal address", 40, 29);

say @personal_info;

# how to access information through index
say "Accessing arrays using index: ",$personal_info[0];

# assign value to an index in the array
$personal_info[4] = "Perl tutorial";

# what if we include a new item into the array 
# but outside of its current range
$personal_info[18] = 10;
# we can include it...

# are there booleans in perl?
# in C we don't have

# say $personal_info[17];
# we can't access this uninitialized index of the array

# we can use a foreach loop to cycle through the elements
# of the array
say "------- starting loop --------------------";
@personal_info = ("William", "My personal address", 40, 29);

for my $info (@personal_info) {
    say $info;
}

say "------- ending loop --------------------";

say "------- starting traditional loop --------------------";

# we could also use the traditional loop to print and cycle through
# the elements of the array

for (my $i = 0; $i < scalar @personal_info; $i++) {
    say $personal_info[$i];
}

say "------- ending traditional loop --------------------";

# strangely there is also a foreach
# I though that the first for was kind of a foreach
# and it actually is kind of the same thing...
# what is the difference between using foreach and for?

foreach my $num (@primes) {
    say $num;
}

say "------- end --------------------";
# this is another way to print all elements of the array
say "A simpler way to print element from the array";
for (@personal_info) {
    say $_;
}

say "------- end --------------------";
say "How to slice elements from an array";
@personal_info = ("William", "My personal address", 40, 29, "Suzuki");

my @my_name = @personal_info[0, 4];
say @my_name;
# use join to concatenate the firtname and lastname with a space
say join(" ", @my_name);
say "------- end --------------------";
# get the number of items inside of the array
# it is like length
my $num_items = scalar @personal_info;
say $num_items;

say "------- end --------------------";
# we can unpack values from the array
my ($first_name, $address, $age, $age_young, $last_name) = @personal_info;
say "$first_name $last_name";

say "------- end --------------------";
say "Popped value of the array: ", pop @personal_info;
say "Pushed value: ", push @personal_info, 17;
say "First item: ", shift @personal_info;
say "Unshifted Item: ", unshift @personal_info, 2;
say join(", ", @personal_info);
# it seems that unshift will append items to the start
# of the array

print join(", ", @primes), "\n";

splice @primes, 0, 3; 
# 3 is the number of items to be removed
say "Remove index 1 to 2: ";
print join(", ", @primes), "\n";

print join " ", ('list', 'of', 'words', "\n");

my $customers = "Sue Sally Paul";
my @cust_array = split / /, $customers;
# the / / means that we want to split the string in the spaces

print join(" ", @cust_array), "\n";

# reverse the array
my @cust_reversed = reverse @cust_array;
print join(" ", @cust_reversed), "\n";

# sort the array
my @cust_sorted = sort @cust_array;
print join(" ", @cust_reversed), "\n";

# reverse sort
my @cust_reverse_sort = reverse sort @cust_array;
print join(" ", @cust_reverse_sort), "\n";

# grep for filtering the array

my @num_array = (1,2,3,4,5,6,7,8,9);
# add a value for odd numbers

my @odds_array = grep {$_ % 2} @num_array;
print join(" ", @odds_array), "\n";

# map in array
# multiply every number in the array by 2
my @double_array = map {$_ * 2} @num_array;
print join(" ", @double_array), "\n";










