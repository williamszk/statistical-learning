// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203762#overview

#include <stdio.h>

void printString(char *s)
{
    // we don't need to pass the length of the array because we can use
    // the end character \0 to know the length of the char array

    int j = 0;
    while (s[j] != '\0')
    {
        printf("%c", s[j]);
        j++;
    }

    printf("\n");
}

void main()
{
    printf("What is your name? ");
    char firstName[10];
    scanf("%s", firstName);                         
    
    printString(firstName);

    printf("Write another name: ");
    // limit the number of characters
    char anotherName[9];
    scanf("%9s", anotherName);
    // this will only read the first 9 characters of the string

    printString(anotherName);

    // how to print string instead of using a loop?
    printf("Here we print a string using just the printf function:\n");
    printf("%s\n", anotherName);
    // note that we are using the %s placeholder for the string

    char password[] = "1234567";
    printf("%s\n", password);
}

// the scanf can only read until a space appears " "
// we use the gets(str) function instead when we have spaces
//