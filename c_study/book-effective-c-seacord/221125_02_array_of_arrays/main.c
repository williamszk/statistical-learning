#include <stdio.h>

int main()
{
    int i, j;
    int n[5][3] = {
        {1, 2, 3},
        {1, 2, 3},
        {1, 2, 3},
        {1, 2, 3},
        {1, 2, 3}};

    printf("sizeof n: %ld\n", sizeof(n));

    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 3; j++)
        {
            printf("%d ", n[i][j]);
        }
        printf("\n");
    }

    return 0;
}