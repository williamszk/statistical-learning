// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27919494#overview

#include <stdio.h>

int main()
{
    // create a pointer to a file
    FILE *filePtr;

    int num;
    filePtr = fopen("myFirstFile2.txt", "r");

    if (filePtr == NULL) // file open was failure
        printf("Opening of file has failed.\n");
    else
    {
        printf("The file is open for writing.\n");

        fscanf(filePtr, "%d", &num);
        // we can use fprintf(stdout, "%d", num);
        // fscanf(stdin, "%d", &num);

        printf("number from file: %d\n", num);


        fclose(filePtr);
    }
    return 0;
}