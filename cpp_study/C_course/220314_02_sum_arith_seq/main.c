// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147650#overview
#include <stdio.h>

int arithSeq(int initTerm, int difference, int n)
{
    return initTerm + (n - 1) * difference;
}

int sumArithSeq(int initTerm, int difference, int n)
{
    int nthTerm = arithSeq(initTerm, difference, n);
    return (initTerm + nthTerm) * (n / 2);
}

int main()
{
    int answer;
    answer = sumArithSeq(1, 2, 9);
    if (answer == 81)
    {
        printf("Correct\n");
    }
    else
    {
        printf("Incorrect\n");
        printf("%d\n", answer);
    }
}