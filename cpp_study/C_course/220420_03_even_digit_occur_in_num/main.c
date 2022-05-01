// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29735162#questions

#include <stdio.h>

int evenDigitOccurInNum(uint64_t num, int digit)
{
    // going from left to right
    if (num < 10)
    {
        if (num == digit)
            return 0;

        return 1;
    }

    int isPrevEven = evenDigitOccurInNum(num / 10, digit);

    int currDigit = num % 10;
    if (currDigit == digit)
    {
        if (isPrevEven == 0)
            return 1;

        if (isPrevEven == 1)
            return 0;
    }

    return isPrevEven;
}

void main()
{

    int digit;

    uint64_t num1 = 124;
    digit = 2;
    // should return 0
    printf("%d\n", evenDigitOccurInNum(num1, digit));

    uint64_t num2 = 12342;
    digit = 2;
    // should return 1
    printf("%d\n", evenDigitOccurInNum(num2, digit));

    uint64_t num3 = 10200240;
    digit = 0;
    // should return 1
    printf("%d\n", evenDigitOccurInNum(num3, digit));

    uint64_t num4 = 102002400;
    digit = 0;
    // should return 0
    printf("%d\n", evenDigitOccurInNum(num4, digit));

    uint64_t num5 = 1111111100111;
    digit = 1;
    // should return 0
    printf("%d\n", evenDigitOccurInNum(num5, digit));
}