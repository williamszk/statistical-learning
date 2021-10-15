
# https://www.youtube.com/watch?v=EsDyGfh8bnM&ab_channel=ArvinAsh

# first simulate a vector of true and false
# which is a stream of information

# then we can simulate binary logical gates

# transistor
# is a switch

# how to build logic gates?

# there are 4 bits, 8 bits, 16 bits, 32bits and 64 bits processors

# let's start with a 1 bit processor
# (maybe we can't do much with 1 bit processor)
# (maybe 4 is the lower bound)
# the design of the CPU will determine the size of
# which the data comes in
# in our case we can only work with 1 bit at a time

# definition of "word"
# a word is an object made of 1s and 0s

# Intel 4004
# 4 bit
# 2250 transistors
# made in 1970

# now a days a processor uses 64bit word length
# and have billions of transistors


# the first task is to build an 'AND GATE'
# using transistor like functions

# then build logic gates for the other binary logical operations
# : OR, XOR, search all the possible gates
# https://youtu.be/EsDyGfh8bnM?t=480


# AND GATE

function and_logic_gate(input_1, input_2)
    # output is like a electrict current
    # it starts as 1
    # we need only 2 transistors to build
    # an AND logic gate
    output = 1

    if input_1 == 1
        if input_2 == 1
            output = 1
        else
            output = 0
        end
    else
        output = 0
    end
    return output
end


# some tests with and_logic_gate
#
and_logic_gate(1,1) == 1
and_logic_gate(1,0) == 0
and_logic_gate(0,1) == 0
and_logic_gate(0,0) == 0
