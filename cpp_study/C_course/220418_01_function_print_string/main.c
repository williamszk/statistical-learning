// Build a function that can print strings

#include <stdio.h>

// function to print strings
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
    char fullName[] = "Dennis Ritchie";
    printString(fullName);

    char author2[] = "Ken Thompson";
    printString(author2);

    char author3[] = "Brian Kernighan";
    printString(author3);
}