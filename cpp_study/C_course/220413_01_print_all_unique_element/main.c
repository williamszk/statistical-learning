// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30378214#overview

#include <stdio.h>
#define SIZE_STORE 100

void printUniqElemArray(int *arr, int n)
{
    int i, j, currElem;
    int arrStore[SIZE_STORE] = {0};
    int zeroExist = 0;
    int elemIsStored = 0;
    int qtdElemStored = 0;

    for (i = 0; i < n; i++)
    {
        currElem = arr[i];
        if (currElem == 0)
        {
            if (zeroExist == 0)
            {
                zeroExist = 1;
                printf("%d\n", currElem);
            }
        }
        else
        {
            // the currElem is not 0 (the corner case)

            // verify if currElem is in the arrStore
            elemIsStored = 0;
            for (j = 0; j < qtdElemStored; j++)
            {
                if (arrStore[j] == currElem)
                {
                    elemIsStored = 1;
                    break;
                }
            }
            // if not include this new element and print in the screen
            if (elemIsStored == 0)
            {
                printf("%d\n", currElem);
                arrStore[qtdElemStored] = currElem;
                qtdElemStored++;
            }
            // if the currElem is in arrStore, do nothing
        }
    }

    printf("Quantity of unique elements in the array: %d\n", qtdElemStored + zeroExist);
}

void main()
{

    int myArr[] = {8, 7, 3, 4, 5, 6, 8, 9, 10, 3, 0, 0, 0, 0};
    int arrLen = sizeof(myArr) / sizeof(myArr[0]);
    printUniqElemArray(myArr, arrLen);
}
