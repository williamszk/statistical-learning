// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/ff/29674454#questions

#include <stdio.h>

void _print_internal_aux(int total, char val)
{
    if (total == 1)
    {
        printf("%c", val);
        printf("%c", val - 32);
    }
    else
    {
        printf("%c", val);
        _print_internal_aux(total - 1, val);
        printf("%c", val - 32);
    }
}

void printLowerUpperCase(int total, char val)
{
    _print_internal_aux(total, val);
    printf("\n");
}

int main()
{
    printLowerUpperCase(3, 'c');
    printLowerUpperCase(2, 'b');

    return 0;
}