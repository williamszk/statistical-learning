// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25434662#overview

#include <stdio.h>

void qtdLessThanNumUserInput()
{
    int num;
    printf("Write the num: ");
    scanf("%d", &num);

    uint32_t countLessThanNum = 0;
    int numInput;
    while (1)
    {
        printf("Input number: ");
        scanf("%d", &numInput);

        if (numInput == -1)
            break;

        if (numInput < num)
            countLessThanNum++;
    }

    printf("From the inputed values, %d were less than %d.\n", countLessThanNum, num);
}

uint32_t recurLessThan(uint32_t num)
{
    int numInput;
    printf("Input number: ");
    scanf("%d", &numInput);

    if (numInput == -1)
        return 0;

    if (numInput < num)
        return recurLessThan(num) + 1;

    return recurLessThan(num);
}

void qtdLessThanNumUserInputRecursive()
{
    uint32_t num;
    printf("Write the num: ");
    scanf("%d", &num);

    printf("From the inputed values, %d were less than %d.\n", recurLessThan(num), num);
}

void main()
{
    printf("This is the iterative function:\n");
    qtdLessThanNumUserInput();

    printf("\n\nThis is the recursive function:\n");
    qtdLessThanNumUserInputRecursive();
}