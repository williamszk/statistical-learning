#include <stdio.h>

int main()
{
    FILE *pfile;

    pfile = fopen("powers_num.txt", "w");

    if (pfile == NULL)
        printf("Error: failed to open file.");
    else
    {
        for (int i = 1; i <= 10; i++)
        {
            fprintf(pfile, "%d\t%d\n", i, i * i);
        }
    }

    return 0;
}