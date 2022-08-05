// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30802636?start=15#overview

#include <stdio.h>
#define ARR_SIZE 132

// hello this is a comment to test git diff
int main() {

    char hold;
    int i;
    char srcArr[] = "KKKKOcRC Kr     hdksKKK";

    int lenArr = sizeof(srcArr)/sizeof(char);

    // The letter K appeared most of the times. Total of 2 appearances.

    // space is 40
    // 'z' is 172
    // we need to accomodate 172 - 40 = 132 elements in the array

    int map[ARR_SIZE] = {0};

    for (i = 0; i < lenArr; i++)
    {
        hold = srcArr[i];
        map[hold - ' ']++;
    }

    // find the most frequent value
    int maxIdx = 0;

    for (i = 0; i < ARR_SIZE; i++) {
        if (map[i] > map[maxIdx])
            maxIdx = i;
    }

    printf("The letter '%c' appeared most of the times. Total of %d appearances.", maxIdx + ' ', map[maxIdx]);

    return 0;
}
