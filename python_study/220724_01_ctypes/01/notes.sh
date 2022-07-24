gcc 

# what -fPIC does?
# -o I understand will tell the name of the ouptut file
cc -fPIC -shared -o my_functions.so my_functions.c

# what is the difference between gcc and cc?

# CC is the name given to the UNIX Compiler Command. It is used as the default compiler 
# command for your operating system and also is executable with the same command. 
# GCC, on the other hand, is the GNU Compiler operating system.

# root@17bd5980aa2c:~/statistical-learning/python_study/220724_01_ctypes# cc --version
# cc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
# Copyright (C) 2019 Free Software Foundation, Inc.
# This is free software; see the source for copying conditions.  There is NO
# warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


# so we could use gcc instead of cc
rm my_functions.so
gcc -fPIC -shared -o my_functions.so my_functions.c
# it does the same thing

