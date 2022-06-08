// https://www.udemy.com/course/the-complete-c-programming-bootcamp/learn/lecture/26156672#overview

#include <stdio.h>

int cumulativeSum(int limit)
{
    int result = 0;

    for (int i = 1; i <= limit; i++)
    {
       result += i; 
    }

    return result;
}



int main()
{

    int number = 12;

    if (number < 0)
    {
        printf("number < 0\n");
    }

    if (number == 5)
    {
        printf("number is equal to 5\n");
    }

    int factor = 2;

    printf("Number before multiplication: %d\n", number);

    number *= factor;
    
    printf("Number after multiplication: %d\n", number);

    int sum = cumulativeSum(number);

    printf("Cumulative sum of %d: %d\n", number, sum);

    return 0;
}