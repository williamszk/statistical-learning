// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27901960?start=15#overview

#include <stdio.h>

int main()
{
    // create a pointer to a file
    FILE *filePtr;

    // filePtr = fopen("myFirstFile.txt", "r");
    filePtr = fopen("mySecondFile.txt", "r"); // this should give some error

    if (filePtr == NULL) // file open was failure
        printf("Opening of file has failed.\n");
    else
    {
        printf("The file is open for writing.\n");

        fclose(filePtr);
    }
    return 0;
}