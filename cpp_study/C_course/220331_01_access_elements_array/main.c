// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20350935#overview

#include <stdio.h>
#include <limits.h>

void main()
{
    // what happens if we try to access an element that has its index larger than the array?
    int myarr[4] = {1, 2, 3, 4};

    printf("%d\n", myarr[4]); // it returns: 1333465552, -1882390288
    // it seems that it returns a random number...
    // this should be an access violation error
    // but C doesn't give an error

    int i;

    int testArray[] = {2, 5, 3, 7, 10};
    
    printf("Size of int: %lu\n", sizeof(int));
    printf("Number of elements in array: %lu\n", sizeof(testArray)/sizeof(int));

    printf("{");
    for (i = 0; i < sizeof(testArray)/sizeof(int); i++)
    {
        printf("%d, ", testArray[i]);
    }
    printf("} \n");

    // modifying a value of the array
    testArray[4] = 10000;

    printf("{");
    for (i = 0; i < sizeof(testArray)/sizeof(int); i++)
    {
        printf("%d, ", testArray[i]);
    }
    printf("} \n");

    // find lowest grade
    int grades[5];
    int lowest_grade = INT_MAX;

    for (i = 0; i < 5; i++)
    {
        printf("Enter grade no.%d: \n", i+1);
        scanf("%d", &grades[i]);
    }

    printf("{");
    for (i = 0; i < sizeof(grades)/sizeof(int); i++)
    {
        printf("%d, ", grades[i]);
    }
    printf("} \n");    

    for (i = 0; i < 5; i++)
    {
        if (lowest_grade > grades[i])
        {
            lowest_grade = grades[i];
        }
    }

    printf("The lowest grade is: %d\n", lowest_grade);

}
