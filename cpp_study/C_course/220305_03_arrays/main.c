#include <stdio.h>
#include <stdlib.h>

int main()
{
    // When we try to use declared but not assigned itens in the array
    // they show strange numbers, so we need to be careful with
    // unassigned values of arrays
    int myGrades[5];

    for (int i = 0; i < 5; i++)
    {
        printf("%d\n", myGrades[i]);
    }
    return 0;
}