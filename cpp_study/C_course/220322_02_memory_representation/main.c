// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30516414#overview

#include <stdio.h>

void main()
{
    char myChar1 = 'a';
    char myChar2 = 97; // we can use a number to store a character...
    char myChar3 = 0x61; // we can also use hexadecimal notation to store a character

    printf("myChar1 \t %c \t %d \t 0x%X \n", myChar1, myChar1, myChar1);
    printf("myChar2 \t %c \t %d \t 0x%X \n", myChar2, myChar2, myChar2);
    printf("myChar3 \t %c \t %d \t 0x%X \n", myChar3, myChar3, myChar3);

    // although we started the chars in different ways when we print them they are all stored in the same way
    // in RAM all of the variables are stored in binary
    // myChar1          a       97      0x61 
    // myChar2          a       97      0x61 
    // myChar3          a       97      0x61 

}
