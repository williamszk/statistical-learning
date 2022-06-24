#include <stdio.h>
#include "doubleLinAlg.h"

void printVector(double *a, int lenArr)
{
    int i;

    printf("lenArr: %d\n", lenArr);

    printf("[ ");
    for (i = 0; i < lenArr; i++)
    {
        printf("%.2lf", a[i]);
        if (i != lenArr - 1)
            printf(" ");
        else
            printf(" ]");
    }
    
    printf("\n");
}

int main()
{
    int lenArr;
    double a[2] = {0.5, 0.1};
    double b[] = {0.5, 0.1};
    double out[2] = {0.0};

    // maybe C can't know the size of the array when we pass 
    // a pointer for the array, we need to pass the length of
    // the array as an argument to the function
    lenArr = sizeof(a)/sizeof(a[0]);
    printVector(a, lenArr);

    addVector(out,  a,  b);



    return 0;
}
