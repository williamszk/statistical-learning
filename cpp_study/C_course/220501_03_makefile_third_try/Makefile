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

# $(CC) = gcc
# final:
# 	$(CC) main.c add.c hello.c -o final
# write: make final, so the command above can be used
# we are using a macro variable $(CC)
# by default "make" will only run the first target

# Clean:
# 	rm *.exe *.o final
# write: make Clean, so we delete all specified files

# ******** Method 3 *********
$(CC) = gcc

final: main.o add.o hello.o
	$(CC) main.o add.o hello.o -o final

main: main.c header.h
	$(CC) -c main.c

hello: hello.c header.h
	$(CC) -c hello.c

add: add.c header.h
	$(CC) -c add.c

clear:
	rm *.exe *.o final

# the makefile is smart enough no know when we changed the file
# and which files we changed
# so if we run "make" without chaging anything
# makefile will tell: make: 'final' is up to date.
# 
# But if we change the main.c file and use "make"
# makefile will know that it just needs to recompile main.c
# cc    -c -o main.o main.c
# cc main.o add.o hello.o -o final