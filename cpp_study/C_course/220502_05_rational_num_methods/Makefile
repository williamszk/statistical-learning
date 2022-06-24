$(CC) = gcc

a: main.o EuclideanAlgo.o Rational.o
	$(CC) -g main.o EuclideanAlgo.o Rational.o -o a

tests: tests.o EuclideanAlgo.o Rational.o
	$(CC) -g tests.o EuclideanAlgo.o Rational.o -o tests

main.o: main.c header.h
	$(CC) -g -c main.c

EuclideanAlgo.o: EuclideanAlgo.c header.h
	$(CC) -g -c EuclideanAlgo.c

Rational.o: Rational.c header.h
	$(CC) -g -c Rational.c

tests.o: tests.c header.h
	$(CC) -g -c tests.c

clear:
	rm *.exe *.o