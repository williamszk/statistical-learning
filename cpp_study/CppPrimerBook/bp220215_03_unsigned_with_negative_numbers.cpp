/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */


#include <iostream>

int main()
{
	// assign negative values to unsigned integer
	unsigned int u = 10;

	int i = -42;

	std::cout << i + i << std::endl; // -84
	std::cout << u + i << std::endl; // this will show incorrect values, 4294967264

	return 0;
}