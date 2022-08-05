# !/bin/bash

# https://www.youtube.com/watch?v=p0KKBmfiVl0&ab_channel=LukeSmith 


# you can do most things without using if statements in bash


echo "=================== 1 ==========================="
echo "Hello there"; echo "General Kenobi!"

echo "=================== 2 ==========================="
echo "Hello there" && echo "General Kenobi!"

echo "=================== 3 ==========================="
decho "Hello there" && echo "General Kenobi!"
# compare 3 and 4
# in 4 "General Kenobi" will run regardless the previous command was ok
# but in 3, "General Kenobi" is not ran, the && will not allow it to run
# I think this is similar to javascript

echo "=================== 4 ==========================="
decho "Hello there"; echo "General Kenobi!"

echo "=================== 5 ==========================="
# || what it does?
echo "Hello there" || echo "General Kenobi!"

# if the first command is ok, then it runs only the first one

decho "Hello there" || echo "General Kenobi!"
# if the first command is not ok, then it runs the second command

# || will only run the second command only if the first did not succeed

echo "=================== 6 ==========================="

# & is another operator
sleep 5 ; echo "All done."

# & will not wait for the first command to finish
# & will make the second command execute write after

sleep 5 & echo "All done"


echo "=================== 7 ==========================="

echo "hi" && echo "there" && decho "bob" && echo "how are you doing?" || echo "Something wrong happened"




