// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24180586?start=15#overview

#include <stdio.h>

void main()
{
    // If receive 7452
    // evenDigitSum = 4 + 2 = 6
    // oddDigitSum = 7 + 5 = 12
    // print(evenDigitSum - oddDigitSum) = -6

    int num;
    printf("Write a number: ");
    scanf("%d", &num);

    int digit = 0; 
    int evenDigitSum = 0;
    int oddDigitSum = 0;

    while (num != 0)
    {
        digit = num % 10;

        if (digit % 2 == 0)
            evenDigitSum += digit;
        else
            oddDigitSum += digit;
        num /=10;
    }

    printf("Result: %d\n", evenDigitSum - oddDigitSum);

}