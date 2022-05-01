# This is a makefile for 3 source files: main.c, add.c, hello.c
# Save the file with name "Makefile"
# In makefiles make sure that we use tabs instead of spaces for indentation
# in makefiles the indentation has meaning

# ******** Method 1 *********

# final:
# 	gcc main.c add.c hello.c -o final

# ******** Method 2 *********
# the structure of a target in makefiles
# target: dependencies
# 	action:


# initial:
# 	echo "Hello There"

$(CC) = gcc
final:
	$(CC) main.c add.c hello.c -o final
# write: make final, so the command above can be used
# we are using a macro variable $(CC)
# by default "make" will only run the first target



Clean:
	rm *.exe *.o final
# write: make Clean, so we delete all specified files

# ******** Method 3 *********
