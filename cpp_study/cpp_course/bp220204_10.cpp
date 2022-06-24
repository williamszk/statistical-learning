/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */

/*
 * Rewrite the exercises from § 1.4.1 (p. 13) using for loops.
 * Exercise 1.11: Write a program that prompts the user for two integers.
 * Print each number in the range specified by those two integers.
 */

#include <iostream>
int main()
{
    int num1 = 0, num2 = 0;
    std::cout << "Write two integer numbers:" << std::endl;
    std::cin >> num1 >> num2;

    for (int i = num1; i <= num2; ++i) {
        std::cout << i << std::endl;
    }

}



