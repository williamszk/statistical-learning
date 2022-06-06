// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27898000#questions

#include <stdio.h>

int main()
{
    FILE *filePtr;

    filePtr = fopen("test.txt", "w");
    // "w": Writing
    // "r": Reading
    // "a": Appending

    if (filePtr != NULL)
    {
        printf("File open, ready.\n");
    }

    fclose(filePtr);

    return 0;
}