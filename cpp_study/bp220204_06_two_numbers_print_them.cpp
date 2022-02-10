/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */

/*
 * Exercise 1.11: Write a program that prompts the user for two integers.
 * Print each number in the range specified by those two integers.
 */

#include <iostream>
int main()
{
    int minNum = 0;
    int maxNum = 0;
    int num1 = 0, num2 = 0;
    std::cout << "Please write two numbers:" << std::endl;
    std::cin >> num1 >> num2;
    if (num1 < num2) {
        minNum = num1;
        maxNum = num2;
    } else {
        minNum = num2;
        maxNum = num1;
    }
    std::cout << "Those are the integers between " << num1 << " and " << num2 << std::endl;
    while (minNum <= maxNum) {
        std::cout << minNum << std::endl;
        ++minNum;
    }
}



