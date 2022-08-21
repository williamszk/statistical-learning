#!/bin/bash

# solution to:
# https://leetcode.com/problems/two-sum/

nums=(3 7 11 15)

# this gives error
# nums=[3 7 11 15]

for elem in ${nums[@]}; do
# the @ symbol specifies that we want to loop 
# over all the elements of the array
    echo $elem
done

for i in ${!nums[@]}; do
    echo "element $i is ${nums[$i]}"
done

target=9



