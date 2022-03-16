// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147642#overview
#include <stdio.h>
#include <stdlib.h>

int arithSeq(int initTerm, int difference, int n)
{
    return initTerm + (n - 1) * difference;
}

int main()
{
    int answer;
    answer = arithSeq(1, 2, 9);
    if (answer == 17)
    {
        printf("Correct");
    }
    else
    {
        printf("Incorrect");
    }

    return 0;
}

// to compile the program in windows
// gcc main.c
// to run the c program in windows
// .\a.exe