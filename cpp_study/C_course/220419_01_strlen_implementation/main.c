// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168690?start=15#overview

#include <stdio.h>

// we can declare the function on the top of the file
// and then define it later
uint32_t strlen2(char *str);

void main()
{
    char myStr[] = "Hello";
    printf("%s has length of %d\n", myStr, strlen2(myStr));

    char myStr2[] = "Thisisanotherstring";
    printf("%s has length of %d\n", myStr2, strlen2(myStr2));
}

uint32_t strlen2(char *str)
{
    uint32_t j = 0;
    while (str[j] != '\0')
    {
        j++;
    }
    return j;
}