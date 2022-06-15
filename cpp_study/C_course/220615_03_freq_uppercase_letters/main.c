// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30802622#overview

#include <stdio.h>

int main()
{
    int i;
    char sourceArr[] = "KIBRCKZMKKKK";
    int lenArr = sizeof(sourceArr) / sizeof(char);
    int map[26] = {0};
    char hold;

    for (i = 0; i < lenArr; i++)
    {
        hold = sourceArr[i];
        map[hold - 'A']++;
    }

    // find the most frequent value
    int maxIdx = 0;

    for (i = 0; i < 26; i++)
    {
        if (map[i] > map[maxIdx])
        {
            maxIdx = i;
        }
    }

    printf("The character %c is the most frequent appearing %d times.\n", maxIdx + 'A', map[maxIdx]);

    return 0;
}
