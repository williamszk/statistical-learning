#!/usr/bin/perl

# scalars can hold integers, floats, strings, octets and hex
$rank = 1;
$name = "Novak";
$tot_money = 55555555.55;
$my_oct = 0167; # with a 0 in front it represents a octet number
$my_hex = 0xbabe;
$my_bin = 0b0101;

print "Name: $name\n";
print "Rank: $rank\n";
print "Total Prize Money: $tot_money\n";

print "My Octal Number: $my_oct\n";
print "My Hexadecimal Number: $my_hex\n";
print "My Binary Number: $my_bin\n";
