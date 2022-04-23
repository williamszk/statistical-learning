// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168698#questions

#include <stdio.h>

void strcpyCustom(char *strCpy, char *strSrc)
{
    int j = 0;
    while (strSrc[j] != '\0')
    {
        strCpy[j] = strSrc[j];
        j++;
    }
    strCpy[j] = '\0';
}


void main()
{
    char myStr[] = "This is a string to be copied.";

    char strHold[100];

    strcpyCustom(strHold, myStr);
    
    printf("%s\n", myStr);
    printf("%s\n", strHold);

}