// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147892#overview

#include <stdio.h>

struct NumTest
{
    int num1;
    int num2;
    int num3;
};

/**
 * Return 1 if at least one num is divisible by the others.
 * Return 0, otherwise.
 */
int isDivisble(int num1, int num2, int num3)
{
    int i, j;
    int listNums[] = {num1, num2, num3};
    int isDivPrev = 0;

    for (i = 0; i < 3; i++)
    {
        isDivPrev = 0;
        for (j = 0; j < 3; j++)
            if (j != i && listNums[j] % listNums[i] == 0)
                isDivPrev++;
        if (isDivPrev == 2)
            return 1;
    }
    return 0;
}

int main()
{
    int i;
    int result;
    int num1, num2, num3;

    struct NumTest listNumTest[] = {
        {
            .num1 = 5,
            .num2 = 10,
            .num3 = 20,
        },
        {
            .num1 = 3,
            .num2 = 36,
            .num3 = 72,
        },
        {
            .num1 = 2,
            .num2 = 4,
            .num3 = 7,
        },
        {
            .num1 = 5,
            .num2 = 7,
            .num3 = 9,
        }};

    int lenList = sizeof(listNumTest) / sizeof(listNumTest[0]);

    for (i = 0; i < lenList; i++)
    {

        num1 = listNumTest[i].num1;
        num2 = listNumTest[i].num2;
        num3 = listNumTest[i].num3;

        result = isDivisble(num1, num2, num3);

        printf("%d. result: %d\n", i, result);
        
    }

    return 0;
}
