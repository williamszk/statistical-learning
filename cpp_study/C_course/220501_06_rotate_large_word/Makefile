# We can change the compiler here
$(CC) = gcc

program: main.o Word128.o
	$(CC) -g main.o Word128.o -o a

main.o: main.c header.h
	$(CC) -g -c main.c

Word128.o: Word128.c header.h
	$(CC) -g -c Word128.c

clear:
	rm *.exe *.o
