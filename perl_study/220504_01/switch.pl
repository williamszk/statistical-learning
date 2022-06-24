# how switch statements work 
# https://youtu.be/WEghIXs8F6c?t=1389

use strict;
use warnings;
use diagnostics;

use feature 'say';

use feature "switch";


my $my_age = 18;

given($my_age){
    when($_ > 16) {
        # we use $_ to reference $age_old
        # instead of writting $age_old entirely
        say "Drive";
        # continue
        # the key word continue is like fallthrough
        # it will check the next condition
        continue;
    } 
    when ($_ > 17) {
        say "Go vote";
    } 
    default {
        say "Nothing special";
    }
}

