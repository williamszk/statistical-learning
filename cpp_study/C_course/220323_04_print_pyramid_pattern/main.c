// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24180508#overview

#include <stdio.h>

void main()
{
    int num;
    int j;
    int numPrint = 1;

    printf("Write a number: ");
    scanf("%d", &num);

    for (int numLines = 1; numLines <= num; numLines++)
    {
        for (int i = 1; i <= num - numLines; i++)
        {
            printf(" ");
        }

        for (j = 1; j <= numLines; j++)
        {
            printf("%d ", numPrint);
            numPrint++;
        }

        printf("\n");
    }
}