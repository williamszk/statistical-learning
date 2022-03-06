/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */

/*
 * Rewrite the exercises from § 1.4.1 (p. 13) using for loops.
 * Exercise 1.9: Write a program that uses a while to sum the numbers from
 * 50 to 100.
 */

#include <iostream>
int main()
{
    int sum = 0;
    for (int i = 50; i <= 100; ++i) {
        sum += i;
    }
    std::cout << "The sum of the numbers between 50 to 100 inclusive is " 
        << sum << std::endl;

}



