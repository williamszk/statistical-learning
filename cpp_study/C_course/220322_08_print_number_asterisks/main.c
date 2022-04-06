// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203400#overview

#include <stdio.h>

void main()
{
    int numAst = 0;
    printf("Write the number of asterisks: ");
    scanf("%d", &numAst);

    int counter = 0;
    while (counter < numAst)
    {
        printf("*");
        counter++;
    }
}