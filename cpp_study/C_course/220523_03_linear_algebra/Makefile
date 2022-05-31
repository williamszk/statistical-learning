
$(CC) = gcc

simpleLinearRegression: simpleLinearRegression.o
	$(CC) -g simpleLinearRegression.o -o experiment.out
	
simpleLinearRegression.o: experiments/simpleLinearRegression.c
	$(CC) -g -c experiments/simpleLinearRegression.c -I .

testDoubleLinAlg: testDoubleLinAlg.o doubleLinAlg.o
	$(CC) -g testDoubleLinAlg.o doubleLinAlg.o -o test.out
	
testDoubleLinAlg.o: tests/testDoubleLinAlg.c 
	$(CC) -g -c tests/testDoubleLinAlg.c -I .



doubleLinAlg.o: doubleLinAlg.c
	$(CC) -g -c doubleLinAlg.c -I .


clean:
	rm *.out *.o
