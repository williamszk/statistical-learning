// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24147866#overview

#include <stdio.h>

void main()
{   
    int theInt;
    int theAbsInt;
    printf("Write an integer number:\n");
    scanf("%d", &theInt);

    if (theInt < 0)
    {
        theAbsInt = -1*theInt;
    } else {
        theAbsInt = theInt;
    }
    
    printf("|%d| = %d\n", theInt, theAbsInt);
}