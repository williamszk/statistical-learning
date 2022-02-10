/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */

/*
 * Exercise 1.9: Write a program that uses a while to sum the numbers from
 * 50 to 100.
 */

#include <iostream>
int main()
{
	int sum = 0, val = 50;
    while (val <= 100) {
        sum += val;
        ++val;
    }
    std::cout << "The sum of all numbers between 50 to 100 is " << sum << std::endl;
}



