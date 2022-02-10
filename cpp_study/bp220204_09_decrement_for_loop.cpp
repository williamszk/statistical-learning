/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */

/*
 * Rewrite the exercises from § 1.4.1 (p. 13) using for loops.
 * Exercise 1.10: In addition to the ++ operator that adds 1 to its operand,
 * there is a decrement operator (--) that subtracts 1. Use the decrement
 * operator to write a while that prints the numbers from ten down to zero.
 */

#include <iostream>
int main()
{
    for (int i = 10; i >= 0; --i) {
        std::cout << i << std::endl;
    }

}



