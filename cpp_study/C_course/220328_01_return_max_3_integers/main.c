// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203588#overview

#include <stdio.h>

int findMaxThreeNums()
{
    int num1, num2, num3, max;
    printf("Write a number (1/3):");
    scanf("%d", &num1);
    printf("Write a number (2/3):");
    scanf("%d", &num2);
    printf("Write a number (3/3):");
    scanf("%d", &num3);
    
    if (num1 > max) max = num1;
    if (num2 > max) max = num2;
    if (num3 > max) max = num3;

    return max;
}

void main()
{
    int maxNum = findMaxThreeNums();
    printf("The max number is: %d\n", maxNum);

}