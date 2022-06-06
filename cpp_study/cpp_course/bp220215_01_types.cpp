/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */


#include <iostream>

int main()
{

	bool myBool = 42; // it becomes true
	std::cout << myBool << std::endl;
	int i = myBool; // i has value of 1
	std::cout << i << std::endl;
	i = 3.14; // i has value of 3
	std::cout << i << std::endl;
	double pi = i;
	std::cout << pi << std::endl;

	unsigned char c = -1;
	std::cout << c << std::endl;
	signed char c2 = 256;
	std::cout << c2 << std::endl;
	/*
	bp220215_01.cpp:16:22: warning: overflow in conversion from 'int' to 'signed char' changes value from '256' to '0' [-Woverflow]
	16 |     signed char c2 = 256;
		|                      ^~~
	*/
	return 0;
}