// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20745224#overview

#include <stdio.h>

void main()
{
    char userPhrase[1000];
    printf("Write a phrase: \n");
    gets(userPhrase);

    int wordCounter = 0;
    int isSpace = 0;

    if (userPhrase[0] != ' ')
    {
        wordCounter++;
    }

    int j = 1;
    while (userPhrase[j] != '\0')
    {
        isSpace = 0;
        if (userPhrase[j - 1] == ' ')
        {
            isSpace = 1;
        }

        if (userPhrase[j] != ' ' && isSpace == 1)
        {
            wordCounter++;
        }
        j++;
    }

    printf("Number of words in the string: %d\n", wordCounter);
}