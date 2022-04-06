#include <stdio.h>

void sum1ToAllElemArr(int *ptrArr[], unsigned int n)
{
    for (int i = 0; i < n; i++)
    {
        *ptrArr[i]++;
    }
}

void main()
{
    int myarr[] = {1, 2, 3};
    sum1ToAllElemArr(myarr, 3);
    printf("%d\n", myarr[0]);
}