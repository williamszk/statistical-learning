// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20745246#overview

#include <stdio.h>
#include <string.h>

int isPalindrome(char *str)
{
    char strHolder[1000];

    int j = 0;
    for (int i = strlen(str) - 1; i >= 0; i--)
    {
        strHolder[j] = str[i]; // copy string in reverse
        j++;
    }

    int equalStr = strcmp(str, strHolder);

    if (equalStr == 0)
        return 1;
    return 0;
}

void main()
{
    // "noon" 1
    // "tech" 0
    // "wow" 1

    char str1[] = "noon";
    printf("%s is palindrome: %d\n", str1, isPalindrome(str1));

    char str2[] = "tech";
    printf("%s is palindrome: %d\n", str2, isPalindrome(str2));

    char str3[] = "wow";
    printf("%s is palindrome: %d\n", str3, isPalindrome(str3));
}