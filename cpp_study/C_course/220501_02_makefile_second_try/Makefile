# My First Makefile

all: printy

printy: main helloWorld
	gcc -o main main.c -c -W -Wall -ansi -pedantic

main: main.c helloWorld.h
	gcc -o main main.c -c -W -Wall -ansi -pedantic

helloWorld: helloWorld.c helloWorld.h
	gcc -o helloWorld helloWorld.c -c -W -Wall -ansi -pedantic

clean:
	rm -rf *.exe *~ printy