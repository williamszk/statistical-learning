// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30516444#overview

#include <stdio.h>

void main()
{
    char myChar;

    printf("Write a character here:\n");
    scanf("%c", &myChar);

    if (myChar >= 48 && myChar <= 57) printf("The character is a digit.\n");
    else if (myChar >= 65 && myChar <= 90) printf("The character is a upper case letter.");
    else if (myChar >= 97 && myChar <= 122) printf("The character is an lower case letter.");
    else printf("The character is other.");

}