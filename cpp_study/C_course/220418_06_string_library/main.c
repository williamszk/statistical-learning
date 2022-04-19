// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20428473#overview

#include <stdio.h>
#include <string.h>

void main()
{

    char name[] = "Bob";

    int nameLen = strlen(name); // strlen comes from the string.h library

    printf("nameLen: %d\n", nameLen);

    char anotherName[strlen(name)];
    strcpy(anotherName, name); // string copy function

    printf("anotherName: %s\n", anotherName);

    char firstName[100] = "Ken"; // we need to reserve enough memory in firstName so that the concat will not overwrite the memory
    char lastName[] = "Thompson";

    strcat(firstName, lastName);

    printf("%s\n", firstName);

    // string compare
    char word1[] = "aa";
    char word2[] = "ab";

    int answerOrder = strcmp(word1, word2);
    // if firstArg comes after then it returns 1
    // if firstArg comes before then it returns -1
    // if they are equal it returns 0

    printf("%d\n", answerOrder);
    // strcmp is used a lot for string comparison
    // to see if two strings are the same
}