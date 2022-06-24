# https://youtu.be/WEghIXs8F6c?t=2672

use strict;
use warnings;
use diagnostics;

use feature 'say';

use feature "switch";
# hashes are like dictionaries or js objects

# $ -> atomic data type
# @ -> arrays
# % -> are for hashes

my %employees = (
    "Sue" => 35,
    "Paul" => 43,
    "Sam" => 39
);

# when accessing the values of employees
# we need to use $ instead of %
printf("Sue is %d\n", $employees{Sue});
# and we can use just the key without the quotes

# add a new key to a hash
$employees{Frank} = 44;
# we use $ instead of %

# loop though the key and values of the hashes
while (my ($k, $v) = each %employees){
    print "$k $v\n";
}

# create an array using the values of the hash
my @ages = @employees{"Sue", "Sam"};
# we are using @ instead of % here...

say @ages;


# transform hash into array
my @hash_array = %employees;
say @hash_array;
say $hash_array[0];
# although we use @ to declare and use the array
# when we need to access its items we need to use $
say $hash_array[1];
# when we transform a hash into an array its keys and values
# are all aligned one after the other
# which it seems strange

# how to delete an item from the hash?
delete $employees{'Frank'};
while (my ($k, $v) = each %employees){
    print "$k $v\n";
}

# check if a key is present in the hash
say (exists $employees{'Sam'} ? "Sam is here" : "Sam is not here");

# we can loop throgh just the keys
for my $key (keys %employees) {
    if ($employees{$key} == 35) {
        say "Hi Sue";
    }
}

# the keys function will just take the keys out of the hash
say keys %employees;
# is there a function to just take the values?
say values %employees;
# I think it is values...











