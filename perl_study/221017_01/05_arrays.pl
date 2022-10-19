# https://www.youtube.com/watch?v=-MbHXGiWzkA&list=PL_RGaFnxSHWpqRBcStwV0NwMA3nXMh5GC&index=7&ab_channel=Simplified

@players = ("Roger", "Andy");

print "Players Set One: @players\n";

# append to array
push (@players, "Rafa");
print "Players Set Two: @players\n";

# add element at beginning 
unshift(@players, "Novak");
print "Players Set Three: @players\n";

# remove element from end
pop(@players);
print "Players Set Four: @players\n";

# remove element from beginning
shift(@players);
print "Players Set Five: @players\n";
