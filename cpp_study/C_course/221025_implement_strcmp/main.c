#include <stdio.h>
#include <string.h>

// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168704#questions

// int strcmp (const char* str1, const char* str2);

// https://www.programiz.com/c-programming/library-function/string.h/strcmp
/**
 * @brief
 * 0	if strings are equal
 * >0	if the first non-matching character in str1 is greater (in ASCII) than that of str2.
 * <0	if the first non-matching character in str1 is lower (in ASCII) than that of str2.
 * @param str1
 * @param str2
 * @return int
 */
// int strcmpUser(char *str1, char *str2)
// {
//     int i;
//     int lenStr1 = sizeof(str1) / sizeof(char);
//     int lenStr2 = sizeof(str2) / sizeof(char);

//     // printf("lenStr1 = %d\n", lenStr1);
//     // printf("lenStr2 = %d\n", lenStr2);

//     for (i = 0; i < lenStr1; i++)
//     {
//         if (str1[i] > str2[i])
//         {
//             return 1;
//         }
//         else
//         {
//             return -1;
//         }
//     }

//     return 0;
// }

int main()
{
    // char str1[100] = "Banana";
    // char str2[100] = "Banana";

    // printf("01 is equal? %d\n", strcmpUser(str1, str2));
    printf("Hello World\n");
}