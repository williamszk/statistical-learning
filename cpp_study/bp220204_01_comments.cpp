/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */

/* 
 * Simple main function
 * Read two numbers and write their sum.
 * */

#include <iostream>
int main()
{
	// Prompt users to enter two numbers
	std::cout << "Enter two numbers: " << std::endl;
	int num1 = 0, num2 = 0; // variables to hold the input we read
	std::cin >> num1 >> num2; // read input
	std::cout << "The sum of " << num1 << " and " << num2
		<< " is " << num1 + num2 << std::endl;

}



