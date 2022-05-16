
$(CC) = gcc

a: main.o large_integer.o
	$(CC) -g main.o large_integer.o -o a


test_comparison_u128: test_comparison_u128.o large_integer.o
	$(CC) -g test_comparison_u128.o large_integer.o -o test

test_comparison_u128.o: tests/test_comparison_u128.c 
	$(CC) -g -c tests/test_comparison_u128.c -I .

test_add_subtract_u128: test_add_subtract_u128.o large_integer.o
	$(CC) -g test_add_subtract_u128.o large_integer.o -o test

test_add_subtract_u128.o: tests/test_add_subtract_u128.c 
	$(CC) -g -c tests/test_add_subtract_u128.c -I .

test_bool_operators_u128: test_bool_operators_u128.o large_integer.o
	$(CC) -g test_bool_operators_u128.o large_integer.o -o test

test_bool_operators_u128.o: tests/test_bool_operators_u128.c 
	$(CC) -g -c tests/test_bool_operators_u128.c -I .

test_increment_decrement_u128: test_increment_decrement_u128.o large_integer.o
	$(CC) -g test_increment_decrement_u128.o large_integer.o -o test

test_increment_decrement_u128.o: tests/test_increment_decrement_u128.c 
	$(CC) -g -c tests/test_increment_decrement_u128.c -I .

main.o: main.c 
	$(CC) -g -c main.c -I .

large_integer.o: large_integer.c
	$(CC) -g -c large_integer.c -I .
# -I . means that we include all header file that are present in the present diretory

clean:
	rm *.exe *.o

