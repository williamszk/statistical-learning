// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30516412#overview
#include <stdio.h>

int main()
{
    char myChar1 = 'a';

    printf("Character: %c \n", myChar1);
    printf("Decimal ASCII Code: %d \n", myChar1);
    printf("Hexadecimal ASCII Code: 0x%X \n", myChar1);

    printf("---------------------------\n");
    char myChar2 = 'O';

    printf("Character: %c \n", myChar2);
    printf("Decimal ASCII Code: %d \n", myChar2);
    printf("Hexadecimal ASCII Code: 0x%X \n", myChar2);


    return 0;
}
// In C, char uses 1 byte of memory
// the smallest memory unit that we can store in RAM is a byte (8 bits)
// so each slot of RAM have size of 8 bits (1 byte)