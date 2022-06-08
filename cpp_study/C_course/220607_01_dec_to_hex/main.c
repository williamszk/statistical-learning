// https://www.udemy.com/course/the-complete-c-programming-bootcamp/learn/lecture/26172990#overview

#include <stdio.h>

int main()
{

    int input;

    printf("Welcome to the Decimal To Hexadecimal Converter!\n");
    printf("===^^===\n");
    printf("Enter a number:\n");

    scanf("%d", &input);

    printf("Decimal representation: %d\n", input);
    printf("Converted to hexadecimal: 0x%X\n", input);

    printf("===^^===\n");
    
    return 0;
}


