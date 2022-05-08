$(CC) = gcc

a: main.o LargeInteger.o
	$(CC) -g main.o LargeInteger.o -o a

testIncrementLargeInt: testIncrementLargeInt.o LargeInteger.o
	$(CC) -g testIncrementLargeInt.o LargeInteger.o -o test

testIncrementLargeInt.o: tests/testIncrementLargeInt.c header.h
	$(CC) -g -c tests/testIncrementLargeInt.c


testDecrementLargeInt: testDecrementLargeInt.o LargeInteger.o
	$(CC) -g testDecrementLargeInt.o LargeInteger.o -o test

testDecrementLargeInt.o: tests/testDecrementLargeInt.c header.h
	$(CC) -g -c tests/testDecrementLargeInt.c


testAddLargeInt: testAddLargeInt.o LargeInteger.o
	$(CC) -g testAddLargeInt.o LargeInteger.o -o test

testAddLargeInt.o: tests/testAddLargeInt.c header.h
	$(CC) -g -c tests/testAddLargeInt.c


testSubLargeInt: testSubLargeInt.o LargeInteger.o
	$(CC) -g testSubLargeInt.o LargeInteger.o -o test

testSubLargeInt.o: tests/testSubLargeInt.c header.h
	$(CC) -g -c tests/testSubLargeInt.c


testLogicalLargeInt: testLogicalLargeInt.o LargeInteger.o
	$(CC) -g testLogicalLargeInt.o LargeInteger.o -o test

testLogicalLargeInt.o: tests/testLogicalLargeInt.c header.h
	$(CC) -g -c tests/testLogicalLargeInt.c


testShiftLargeInt: testShiftLargeInt.o LargeInteger.o
	$(CC) -g testShiftLargeInt.o LargeInteger.o -o test

testShiftLargeInt.o: tests/testShiftLargeInt.c header.h
	$(CC) -g -c tests/testShiftLargeInt.c


testGreaterSmallerLargeInt: testGreaterSmallerLargeInt.o LargeInteger.o
	$(CC) -g testGreaterSmallerLargeInt.o LargeInteger.o -o test

testGreaterSmallerLargeInt.o: tests/testGreaterSmallerLargeInt.c header.h
	$(CC) -g -c tests/testGreaterSmallerLargeInt.c


testMultLargeInt: testMultLargeInt.o LargeInteger.o
	$(CC) -g testMultLargeInt.o LargeInteger.o -o test

testMultLargeInt.o: tests/testMultLargeInt.c header.h
	$(CC) -g -c tests/testMultLargeInt.c


testDivLargeInt: testDivLargeInt.o LargeInteger.o
	$(CC) -g testDivLargeInt.o LargeInteger.o -o test

testDivLargeInt.o: tests/testDivLargeInt.c header.h
	$(CC) -g -c tests/testDivLargeInt.c


main.o: main.c header.h
	$(CC) -g -c main.c


LargeInteger.o: LargeInteger.c
	$(CC) -g -c LargeInteger.c -I .


clean:
	rm *.exe *.o

# https://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/