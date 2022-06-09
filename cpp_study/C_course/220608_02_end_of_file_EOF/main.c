// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27919650#overview

#include <stdio.h>

int main()
{
    FILE *filePtr;

    filePtr = fopen("exerciseFile.txt", "r");

    char hold;
    int count = 0;
    if (filePtr == NULL)
        printf("Error: opening he file failed.\n");
    else
    {
        while ( (hold = fgetc(filePtr)) != EOF)
        {
            printf("%c", hold);
            ++count;
        }

        printf("\n");

        printf("\nThe number of characters in the file is %d\n", count);
    }

    return 0;
}
