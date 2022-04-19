// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203764#overview

#include <stdio.h>

void countCharInput()
{
    printf("Write something:\n");
    char myStr[100];
    gets(myStr);

    int counter = 0;
    int i = 0;
    while (myStr[i] != '\0')
    {
        counter++;
        i++;
    }
    printf("You wrote %d characters.\n", counter);
}

void main()
{
    // get input string from user
    // count the number of characters from the input
    // tell the quantity of chars

    countCharInput();
}