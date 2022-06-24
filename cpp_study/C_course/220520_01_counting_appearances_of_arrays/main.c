// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30802552?start=0#questions
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/30802554#questions

#include <stdio.h>

int main()
{
    int i;
    int lenArr;
    int arr[] = {0, 1, 0, 1, 0, 0, 1, 0};
    // 0 1 0 1 0 0 1 0

    int count0 = 0, count1 = 0;

    lenArr = sizeof(arr) / sizeof(arr[0]);

    for (i = 0; i < lenArr; i++)
    {
        if (arr[i] == 0)
            count0++;
        else if (arr[i] == 1)
            count1++;
    }

    printf("Qtd of 1s: %d\n", count1);
    printf("Qtd of 0s: %d\n", count0);

    printf("// ================================ //\n");

    // we want to count the frequency of numbers
    // we'll use countArr as a sort of Python dictionary to keep
    // record of occurences, we also could use a struct
    // in the case of the struct it would make more sense
    // if the keys are not numbers from 0 to 9;
    int countArr[3] = {0};

    int arr2[] = {0, 1, 2, 2, 1, 1, 0, 2, 1};
    lenArr = sizeof(arr2) / sizeof(arr2[0]);
    for (i = 0; i < lenArr; i++)
    {
        countArr[arr2[i]]++;
    }

    lenArr = sizeof(countArr) / sizeof(countArr[0]);
    printf("Frequency table:\n");
    for (i = 0; i < lenArr; i++)
    {
        printf("%d : %d\n", i, countArr[i]);
    }


    return 0;
}