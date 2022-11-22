#include <stdio.h>

void findMinMax(int a, int b, int *pMin, int *pMax)
{
    if (a > b)
    {
        *pMax = a;
        *pMin = b;
    }
    else
    {
        *pMax = b;
        *pMin = a;
    }
}

int main()
{
    int a = -1233, b = 10239;
    int min = 0;
    int max = 0;

    printf("min=%d, max=%d\n", min, max);

    findMinMax(a, b, &min, &max);

    printf("min=%d, max=%d\n", min, max);


    return 0;
}
