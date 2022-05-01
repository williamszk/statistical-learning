// https://stackoverflow.com/questions/21958247/map-like-structure-in-c-use-int-and-struct-to-determine-a-value#:~:text=The%20C%20Programming%20Language%20by,struct%20Key%20and%20struct%20Value.

#include <stdio.h>

struct Dictionary
{
    char *key;
    int value;
};

void main()
{
    // https://stackoverflow.com/questions/32698293/assign-values-to-structure-variables
    struct Dictionary myDict = {
        "apples",
        18};

    struct Dictionary myArr[3];

    myArr[0] = myDict;

    // https://stackoverflow.com/questions/21293491/assign-to-array-in-struct-in-c

    struct Dictionary tempObj;

    tempObj.key = "Banana";
    tempObj.value = 20;

    myArr[1] = tempObj;

    tempObj.key = "Orange";
    tempObj.value = 90;

    myArr[2] = tempObj;

    int arrLen = sizeof(myArr) / sizeof(myArr[0]);

    for (int j = 0; j < arrLen; j++)
    {
        printf("%d\n", sizeof(myArr[j]));
    }

    for (int i = 0; i < arrLen; i++)
    {
        printf("Print Dictionary: key: %s, value: %d\n", myArr[i].key, myArr[i].value);
    }
}