// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27919516?start=15#overview

#include <stdio.h>

int main()
{

    FILE *pFile;

    pFile = fopen("exerciseFile.txt", "r");

    if (pFile == NULL)
        printf("Error: failed to open the file.");

    else
    {
        char hold;
        int count = 0;

        while ((hold = fgetc(pFile)) != EOF)
        {
            if (hold == '\n')
                ++count;
        }

        printf("The number of lines in the file is: %d\n", count);
    }

    return 0;
}
