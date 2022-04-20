// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25634464#questions/14999744

#include <stdio.h>

int isPositionOddEvenValueFinder(int num)
{
    if (num < 10)
    { // it means one digit
        // this should be pair
        if (num % 2 == 1)
            return 0;

        return 1;
    }

    uint32_t evenDigit = num % 10;
    uint32_t oddDigit = (num % 100) / 10;

    if (evenDigit % 2 == 1)
        return 0;

    if (oddDigit % 2 == 0)
        return 0;

    if (num < 100)
    { // this is the case of 2 digits
        // _ _, the left should be odd and the right should be even
        // if this is the case num < 100, then we are the last iteration
        return 1;
    }

    num /= 100;

    return isPositionOddEvenValueFinder(num);
}

void main()
{
    uint32_t num1 = 36435; // should return 0
    printf("%d is correct? %d\n", num1, isPositionOddEvenValueFinder(num1));

    uint32_t num2 = 438; // should return 1
    printf("%d is correct? %d\n", num2, isPositionOddEvenValueFinder(num2));

    uint32_t num3 = 6543210; // should return 1
    printf("%d is correct? %d\n", num3, isPositionOddEvenValueFinder(num3));

    uint32_t num4 = 2210; // should return 0
    printf("%d is correct? %d\n", num4, isPositionOddEvenValueFinder(num4));

    uint32_t num5 = 8; // should return 1
    printf("%d is correct? %d\n", num5, isPositionOddEvenValueFinder(num5));

    uint32_t num6 = 12121212; // should return 1
    printf("%d is correct? %d\n", num6, isPositionOddEvenValueFinder(num6));

    uint32_t num7 = 834; // should return 1
    printf("%d is correct? %d\n", num7, isPositionOddEvenValueFinder(num7));
}