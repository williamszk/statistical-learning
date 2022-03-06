#include <stdio.h>
#include <stdlib.h>

int main()
{
    int sizeArray = 10;
    double salaries[sizeArray];

    for (int i = 0; i < sizeArray; i++)
    {
        printf("%f\n", salaries[i]);
    }

    return 0;
    // from here we can notice that we can use a variable to assign the size of the array
    // when using double the default value for unassigned values is 0
}