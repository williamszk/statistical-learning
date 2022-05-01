// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/29730924?start=0#questions

#include <stdio.h>

int findAscenDescenOtherwise(uint32_t num)
{
    // going from left to right...
    if (num < 100)
    {
        int digitLeft = num / 10;
        int digitRight = num % 10;

        if (digitLeft > digitRight)
            return -1;
        else if (digitRight > digitLeft)
            return 1;
    }

    int prev = findAscenDescenOtherwise(num / 10);

    if (prev == 0)
        return 0;

    int digit = num % 10;
    int prevDigit = (num % 100) / 10;

    if (digit > prevDigit)
    {
        if (prev == 1)
            return 1;
        else if (prev == -1)
            return 0;
    }
    else if (prevDigit > digit)
    {
        if (prev == 1)
            return 0;
        else if (prev == -1)
            return -1;
    }
}

void main()
{

    // 1 = very ascending
    // -1 = very descending
    // 0 = otherwise
    // "124" -> 1
    // "12340" -> 0
    // "9643" -> -1

    // assumptions: num >= 10
    // more than 2 digits
    // all digits are different, there are not digits that are equal in the same input

    uint32_t num1 = 124; // should return 1
    printf("num1: %d\n", findAscenDescenOtherwise(num1));  

	uint32_t num2 = 12340; // this should return 0
	printf("num2: %d\n", findAscenDescenOtherwise(num2));

	uint32_t num3 = 9643; // this should return -1
	printf("num2: %d\n", findAscenDescenOtherwise(num3));

}
