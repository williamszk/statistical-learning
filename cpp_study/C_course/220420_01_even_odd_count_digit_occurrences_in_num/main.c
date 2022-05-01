// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29735158?start=15#questions

#include <stdio.h>

// return 1, if the count of digit in num is even
// return 0, if the count of the digit is odd
uint32_t digitEvenOccurInNum(uint32_t num, int digit, int isEven)
{
    if (num < 10)
    { // this is the case where there is only 1 digit left
        if (num == digit)
        {
            if (isEven == 1)
                return 0;
            if (isEven == -1)
                return 1;
        }

        // here is the case where the last digit is not equal do the user's digit
        if (isEven == 1)
            return 1;
        if (isEven == -1)
            return 0;
    }

    uint32_t currDigit = num % 10;

    if (currDigit == digit)
    {
        isEven *= -1;
    }

    num /= 10;

    return digitEvenOccurInNum(num, digit, isEven);
}

void main()
{
    int digit;

    uint32_t num1 = 124;
    digit = 2;
    // should return 0
    printf("%d\n", digitEvenOccurInNum(num1, digit, 1));

    uint32_t num2 = 12342;
    digit = 2;
    // should return 1
    printf("%d\n", digitEvenOccurInNum(num2, digit, 1));

    uint32_t num3 = 10200240;
    digit = 0;
    // should return 1
    printf("%d\n", digitEvenOccurInNum(num3, digit, 1));

    uint32_t num4 = 102002400;
    digit = 0;
    // should return 0
    printf("%d\n", digitEvenOccurInNum(num4, digit, 1));

}

// Next challenge: 
// Write a recursive function that counts the number of occurrences of a digit
// in a num.
// Return the count of time that the number appeared.