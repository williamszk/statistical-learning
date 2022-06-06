// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27919490#overview

#include <stdio.h>

int main()
{
    // create a pointer to a file
    FILE *filePtr;

    filePtr = fopen("myFirstFile.txt", "w");

    char myChar1;

    if (filePtr == NULL) // file open was failure
        printf("Opening of file has failed.\n");
    else
    {
        printf("The file is open for writing.\n");

        fputc('H', filePtr);
        fputc('e', filePtr);
        fputc('y', filePtr);

        // fputc('h', stdout); // this will output to the terminal, the standard output

        fclose(filePtr);
    }
    return 0;
}