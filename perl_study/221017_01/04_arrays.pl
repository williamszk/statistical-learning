#!/usr/bin/perl

# https://www.youtube.com/watch?v=Jivx99MwK3s&list=PL_RGaFnxSHWpqRBcStwV0NwMA3nXMh5GC&index=5&ab_channel=Simplified

# arrays need to have @ in the name
@ranks = (1,2,3);
@names = ('Novak', 'Roger', 'Andy');

print "All ranks: @ranks\n";
print "All names: @names\n";

print "Top Player: @names[0]\n";

# https://www.youtube.com/watch?v=7OJN46FcnCY&list=PL_RGaFnxSHWpqRBcStwV0NwMA3nXMh5GC&index=7&ab_channel=Simplified

# this is sequential filling
@ranks = (1..10);
@alphabets = (a..z);
@alphabets = ('a'..'z'); # this way also works

print "All ranks: @ranks\n";
print "All Alphabets: @alphabets\n";

# this will get the length of the array
$size = @alphabets;

print "Size of Alphabets array: $size\n";

@alphabets_upper = (A..Z);
print "Alphabets upper: @alphabets_upper\n";
