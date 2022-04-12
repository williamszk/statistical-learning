// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25821678?start=15#overview

// is palindrome

#include <stdio.h>

int isPalindrome(int *arr, int n)
{
    // we need to pass an array to the argument
    int lenCheck = n / 2;
    for (int i = 0; i < lenCheck; i++)
    {
        if (arr[i] != arr[n - i - 1])
            return 0;
    }
    return 1;
}

void printIsPalindrome(int result)
{
    if (result == 1)
        printf("is palindrome.\n");
    else if (result == 0)
        printf("is not palindrome.\n");
}

void main()
{
    int arrLen;

    int test1[] = {1, 3, 2, 3, 1}; // is palindrome
    arrLen = sizeof(test1) / sizeof(test1[0]);
    printf("test1 ");
    printIsPalindrome(isPalindrome(test1, arrLen));

    int test2[] = {1, 2, 3, 3, 2, 1}; // is palindrome
    arrLen = sizeof(test2) / sizeof(test2[0]);
    printf("test2 ");
    printIsPalindrome(isPalindrome(test2, arrLen));

    int test3[] = {1, 4, 6, 2}; // not palindrome
    arrLen = sizeof(test3) / sizeof(test3[0]);
    printf("test3 ");
    printIsPalindrome(isPalindrome(test3, arrLen));

    int test4[] = {1,1,1,1,1,5,1,1,1}; // not palindrome
    arrLen = sizeof(test4) / sizeof(test4[0]);
    printf("test4 ");
    printIsPalindrome(isPalindrome(test4, arrLen));
}

