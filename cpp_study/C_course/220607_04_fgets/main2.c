// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/27919502#overview 

#include <stdio.h>

int main()
{
    FILE *filePtr;

    filePtr = fopen("myFirstFile.txt", "r");

    if (filePtr == NULL) 
        printf("Opening of file has failed.\n");
    else
    {
        printf("The file is open for writing.\n");

        char myString[10];

        while(fgets(myString, 10, filePtr))
            printf("%s", myString);
        
        fclose(filePtr);
    }

    return 0;
}

