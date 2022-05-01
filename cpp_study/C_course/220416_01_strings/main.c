// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203752#overview
#include <stdio.h>

void main()
{
    char chArr[] = {'H', 'e', 'l', 'l', 'o'};

    // this is 1st way of initializing a string
    char myStr[] = {'H', 'e', 'l', 'l', 'o', '\0'};

    // this is the 2nd way of initializing a string
    char myStr2[] = "Hello";
    // which is similar to the previous way
    // so there is also a \0 char behid the scenes

    int arrLen;
    arrLen = sizeof(myStr) / sizeof(myStr[0]);
    printf("arrLen: %d\n", arrLen);

    int i;
    for (i = 0; i < arrLen - 1; i++)
    {
        printf("%c", myStr[i]);
    }
    printf("\n");

    arrLen = sizeof(myStr2) / sizeof(myStr2[0]);

    for (i = 0; i < arrLen - 1; i++)
    {
        printf("%c", myStr2[i]);
    }
    printf("\n");

    char firstName[] = "William";
    char lastName[] = "Suzuki";

    char password[10] = "123456789";
    // remeber to include the \0 char

    


}
