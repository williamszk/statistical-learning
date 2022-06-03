// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27919494#overview

#include <stdio.h>

int main()
{
    // create a pointer to a file
    FILE *filePtr;

    filePtr = fopen("myFirstFile.txt", "w");
    int num = 512;

    if (filePtr == NULL) // file open was failure
        printf("Opening of file has failed.\n");
    else
    {
        printf("The file is open for writing.\n");

        // this function will write a number to the file
        fprintf(filePtr, "%d", num);

        fprintf(filePtr, "\t%d %d\n", num, 9999);

        // this is just a different way to write a file instead of using
        // fputc()

        fclose(filePtr);
    }
    return 0;
}