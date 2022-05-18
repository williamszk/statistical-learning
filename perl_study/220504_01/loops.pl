# how looping works
# https://youtu.be/WEghIXs8F6c?t=1389

use strict;
use warnings;
use diagnostics;

use feature 'say';

use feature "switch";

for (my $i = 0; $i < 10; $i++){
    say $i;
}

say "--------------------";

my $j = 1;

while ($j < 10){
    say $j;
    $j++;
}

say "--------------------";

$j = 0;

while ($j < 10) {
    if ($j % 2 == 0) {
        $j++;
        next; # next is like continue
    }

    if ($j == 7){
        last; # last is like continue
    }

    say $j;
    $j++;
}

say "--------------------";

my $lucky_number = 7;

my $guess; # when we declare but do not assign
# this variable will asume value of undefined

# say $guess; # this gives a warning...

do {
    say "Guess a number between 1 and 10.";
    # how to get input from the user?
    $guess = <STDIN>;
} while $guess != $lucky_number;
# we can omit parenthesis in if statements

say "You guessed $lucky_number";











