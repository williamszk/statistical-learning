/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */


#include <iostream>

int main()
{
	unsigned int u1 = 42, u2 = 10;
	std::cout << u1 - u2 << std::endl; // 32
	std::cout << u2 - u1 << std::endl; // 4294967264 it wraps around

	return 0;
}