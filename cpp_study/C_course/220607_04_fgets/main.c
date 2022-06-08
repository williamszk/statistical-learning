// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27919502#overview

#include <stdio.h>

int main()
{
    // gets = get string
    // fgets = file get string

    FILE *filePtr;

    filePtr = fopen("myFirstFile.txt", "r");

    if (filePtr == NULL)
        printf("Opening of file has failed.\n");
    else
    {
        printf("The file is open for writing.\n");

        char myString[10];

        int count = 0;
        // stringname, size to store, pointer to file
        while (fgets(myString, 10, filePtr))
            printf("string #%d read: %s\n", ++count, myString);

        fclose(filePtr);
    }

    return 0;
}
