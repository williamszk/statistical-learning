// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147712#overview

#include <stdio.h>

int main()
{
    int x;
    int x2, x4, x6, x8;

    printf("Enter X: ");
    scanf("%d", &x);

    x2 = x * x;
    x4 = x2 * x2;
    x6 = x2 * x4;
    x8 = x4 * x4;

    printf("x^2 = %d\n", x2);
    printf("x^4 = %d\n", x4);
    printf("x^6 = %d\n", x6);
    printf("x^8 = %d\n", x8);
}