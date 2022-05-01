// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30378230?start=0#overview

#include <stdio.h>

void printUniqueElem(int *arr, int n)
{
    int i, j;
    int currElem, compElem;
    int isRepeated = 0;
    int countUnique = 0;

    for (i = 0; i < n; i++)
    {
        currElem = arr[i];
        isRepeated = 0;
        for (j = i + 1; j < n; j++)
        {
            compElem = arr[j];
            if (currElem == compElem)
            {
                isRepeated = 1;
                break;
            }
        }

        if (isRepeated == 0 || i == n)
        {
            printf("%d\n", currElem);
            countUnique++;
        }
    }

    printf("There are %d unique elements.\n", countUnique);
}

void main()
{
    int myarr[] = {8, 7, 3, 4, 5, 6, 8, 9, 10, 3, 0, 0, 0, 0};
    int arrLen = sizeof(myarr) / sizeof(myarr[0]);

    printUniqueElem(myarr, arrLen);
}
