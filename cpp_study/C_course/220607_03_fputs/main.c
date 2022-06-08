// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27919500#overview

#include <stdio.h>

int main()
{
    // putc = put character
    // fputc = file put character
    // puts = put string
    // fputs = file put string

    FILE *filePtr;

    puts("Hey man");
    puts("A test using puts function");

    filePtr = fopen("myFirstFile.txt", "w");

    if (filePtr == NULL) // file open was failure
        printf("Opening of file has failed.\n");
    else
    {
        printf("The file is open for writing.\n");

        fputs("Hey man\n", filePtr);
        fputs("A test using puts function\n", filePtr);

        // it is better to include strings in file using fputs

        fclose(filePtr);
    }

    return 0;
}

