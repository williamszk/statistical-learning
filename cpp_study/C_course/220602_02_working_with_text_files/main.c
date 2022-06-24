// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27901966#overview
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27919486#overview

#include <stdio.h>

int main()
{
    // create a pointer to a file
    FILE *filePtr;

    filePtr = fopen("myFirstFile.txt", "r");

    char myChar1;

    if (filePtr == NULL) // file open was failure
        printf("Opening of file has failed.\n");
    else
    {
        printf("The file is open for writing.\n");

        myChar1 = fgetc(filePtr);
        printf("The first char is: %c\n", myChar1);
        
        myChar1 = fgetc(filePtr);
        printf("The second char is: %c\n", myChar1);

        // fgetc(stdin); // we can use this to pass chars from the keyboard to the machine

        fclose(filePtr);
    }


    return 0;
}