/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */

/*
 * This program asks for user input as an integer number
 * Then it outputs the sum of the numbers inputed
 */

#include <iostream>
int main()
{
    int sum = 0, value = 0;
    while (std::cin >> value)
    {
        sum += value;
    }
    std::cout << "Sum is: " << sum << std::endl;
    return 0;
}
