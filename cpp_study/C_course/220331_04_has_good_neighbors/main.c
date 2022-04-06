// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25785660?start=0#overview

#include <stdio.h>

void main()
{
    int arr1[] = {1, 3, 2, 6, 3}; // should return 1, there are good neighbors
    int arr2[] = {4, 4, 7, 4, 9}; // should return 0, there are no good neighbors

    int i;
    int hasGoodNeighbors;

    hasGoodNeighbors = 0;
    for (i = 1; i < 4; i++)
    {
        if (arr1[i - 1] * arr1[i + 1] == arr1[i])
        {
            printf("arr1 has good neighbors\n");
            hasGoodNeighbors = 1;
            break;
        }
    }
    if (hasGoodNeighbors == 0)
    {
        printf("arr1 doesn't have good neighbors\n");
    }

    hasGoodNeighbors = 0;
    for (i = 0; i < 4; i++)
    {
        if (arr2[i - 1] * arr2[i + 1] == arr2[i])
        {
            printf("arr2 has good neighbors\n");
            hasGoodNeighbors = 1;
        }
    }
    if (hasGoodNeighbors == 0)
    {
        printf("arr2 doesn't have good neighbors\n");
    }
}
