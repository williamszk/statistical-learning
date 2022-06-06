// https://www.youtube.com/watch?v=GQp1zzTwrIg&t=5753s&ab_channel=CodeBeauty

#include <iostream>

int main() 
{
    // +, -, /, *, %
    std::cout << 5 + 2 << std::endl;
    std::cout << 5 / 2 << std::endl;
    std::cout << 5.0 / 2.0 << std::endl;
    // We need at least one float to make the division a float 
    std::cout << 5 / 2.0 << std::endl;
    // std::cout << 5.454 % 2.0 << std::endl;
    // The modulo operator does not work with double in C++
    std::cout << 5 % 2 << std::endl;

    // There is a difference between binary operators +, -, *, /
    // And unary operators, ++, --
    std::cout << std::endl; 
    int myNumber01 = 7;
    myNumber01++;
    std::cout << myNumber01 << std::endl;
    
    // Note that below the code will run and then ++ will be applies
    std::cout << myNumber01++ << std::endl;
    // this is called post-increment
    // the alternative way is the pre-increment
    // like in: ++myNumber01;
    
    std::cout << --myNumber01 << std::endl;

    // To clear the screen above
    // The command passed here will go directly to the terminal
    // So this only make sense for Unix-like OS
    // system("clear");

    // Relational operators: <, >, <=, >=, ==, !=
    int myVarA = 5, myVarB = 5;
    std::cout << (myVarA > myVarB) << std::endl;
    std::cout << (myVarA == myVarB) << std::endl;
    // It seems that there is no boolean type in C++
    // They return 0 or 1
    
    std::cout << std::endl;
    // We have also logical operators: &&, ||, !
    std::cout << (myVarA == 5 && myVarB == 5) << std::endl;
    std::cout << !(myVarA == 5 && myVarB == 5) << std::endl;

    // There are also assignment operators
    // =, +=, -=, *=, /=, %=
    int myVarC = 10;
    myVarC %= 3;
    std::cout << "Test with %= assignment operator: " << myVarC << std::endl; 



    std::cout << std:endl;
    return 0;
}

// Next class:
// https://youtu.be/GQp1zzTwrIg?t=8474


