// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29735162#questions

#include <stdio.h>

int countOccurrDigitInNum(uint64_t num, int digit, int countOccur)
{
    if (num < 10)
    {
        if (num == digit)
        {
            countOccur++;
        }
        return countOccur;
    }

    uint64_t currDigit = num % 10;

    if (currDigit == digit)
    {
        countOccur++;
    }

    num /= 10;

    return countOccurrDigitInNum(num, digit, countOccur);
}


void main()
{
    int digit;

    uint64_t num1 = 124;
    digit = 2;
    // should return 1
    printf("%d\n", countOccurrDigitInNum(num1, digit, 0));

    uint64_t num2 = 12342;
    digit = 2;
    // should return 2
    printf("%d\n", countOccurrDigitInNum(num2, digit, 0));

    uint64_t num3 = 10200240;
    digit = 0;
    // should return 4
    printf("%d\n", countOccurrDigitInNum(num3, digit, 0));

    uint64_t num4 = 102002400;
    digit = 0;
    // should return 5
    printf("%d\n", countOccurrDigitInNum(num4, digit, 0));

    uint64_t num5 = 1111111100111;
    digit = 1;
    // should return 11
    printf("%d\n", countOccurrDigitInNum(num5, digit, 0));

}