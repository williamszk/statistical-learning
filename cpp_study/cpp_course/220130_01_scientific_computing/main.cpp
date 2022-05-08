/* Some notes on the book Scientific computing with c++
 * We can make the compiler warn us when there is a variable
 * not being used.
 * g++ -Wall myFile.cpp
 * The -Wall mean warn all.
 * */

#include <iostream>

int main()
{
    std::cout << "This is a message." << std::endl;
    int thisUnsuedVari = 0;
    return 0;
}

/*
 * This is an example of how the warning message works:
sc220130_01.cpp:13:9: warning: unused variable 'thisUnsuedVari' [-Wunused-variable]
   13 |     int thisUnsuedVari = 0;
      |         ^~~~~~~~~~~~~~

-Wall will create an executable
but -Wall -Werror will not create an executable

*/




