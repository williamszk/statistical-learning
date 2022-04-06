#include <stdio.h>
#include <stdlib.h>

int convertCharToInt(char char1, char char2, char char3)
{
    // 0 -> 48
    // 9 -> 57
    int convChar1 = (int) char1;
    int convChar2 = (int) char2;
    int convChar3 = (int) char3;

    if (convChar1 < 48 || convChar1 > 57) {
        printf("Error: The first argument is not a number. The given argument is: '%c'\n", char1);
        return -1;
    } else if (convChar2 < 48 || convChar2 > 57) {
        printf("Error: The second argument is not a number. The given argument is: '%c'\n", char2);
        return -1;
    } else if (convChar3 < 48 || convChar3 > 57) {
        printf("Error: The third argument is not a number. The given argument is: '%c'\n", char3);
        return -1;
    }

    int convCharNum1 = convChar1 - 48;
    int convCharNum2 = convChar2 - 48;
    int convCharNum3 = convChar3 - 48;

    int convertedNum = convCharNum1*100 + convCharNum2*10 + convCharNum3;

    return convertedNum;
}

int main()
{
    
    int convertedNum = convertCharToInt('9', '2', 'f');
    printf("The converted number is: %d\n", convertedNum);
    
    return 0;
}