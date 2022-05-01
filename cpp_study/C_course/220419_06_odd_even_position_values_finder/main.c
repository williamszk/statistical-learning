// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25634458#questions/14999744

#include <stdio.h>

int isPositionOddEvenValueFinder(uint32_t num, int isIndexEven)
{
    // if there is no more digits left
    if (num == 0)
        return 1;

    uint32_t digit = num % 10;
    // isIndexEven -> 1 // true, even, not odd
    // isIndexEven -> -1 // false, not even, odd
    if (digit % 2 == 1 && isIndexEven == 1)
        // here the digit is odd, but the index is even (not odd)
        return 0;
    if (digit % 2 == 0 && isIndexEven == -1)
        // here the digit is even, but the index is odd (not even)
        return 0;

    num /= 10;
    isIndexEven *= -1;
    return isPositionOddEvenValueFinder(num, isIndexEven);
}

void main()
{
    uint32_t num1 = 36435; // should return 0
    printf("%d is correct? %d\n", num1, isPositionOddEvenValueFinder(num1, 1));

    uint32_t num2 = 438; // should return 1
    printf("%d is correct? %d\n", num2, isPositionOddEvenValueFinder(num2, 1));

    uint32_t num3 = 6543210; // should return 1
    printf("%d is correct? %d\n", num3, isPositionOddEvenValueFinder(num3, 1));

    uint32_t num4 = 2210; // should return 0
    printf("%d is correct? %d\n", num4, isPositionOddEvenValueFinder(num4, 1));

    uint32_t num5 = 8; // should return 1
    printf("%d is correct? %d\n", num5, isPositionOddEvenValueFinder(num5, 1));

    uint32_t num6 = 12121212; // should return 1
    printf("%d is correct? %d\n", num6, isPositionOddEvenValueFinder(num6, 1));

}