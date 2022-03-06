#include <stdio.h>
#include <stdlib.h>

int getAmtOfDigitsSmallerThanADigit(int num, int digit)
{
    int amtOfDigitsSmaller = 0;
    int numHolder = num;

    while (numHolder > 0)
    {
    int theRest = numHolder % 10;
    if (theRest < digit)
    {
        ++amtOfDigitsSmaller;
    }

    numHolder /= 10;
    }
    
    return amtOfDigitsSmaller;
}

int main()
{
    int amtOfDigitsSmaller;

    amtOfDigitsSmaller = getAmtOfDigitsSmallerThanADigit(12345, 3);
    printf("This should be 2: %d\n", amtOfDigitsSmaller);

    amtOfDigitsSmaller = getAmtOfDigitsSmallerThanADigit(123456789, 5);
    printf("This should be 4: %d\n", amtOfDigitsSmaller);

    return 0;
}