#include <stdio.h>
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203172#overview

void main()
{
    // accept: +, -, *, /, %

    // read 2 numbers from the user
    // use switch

    // if divide by zero, warn the user that the operation is not allowed

    char operator;
    int num1, num2;

    int keepWait = 1;
    while (keepWait == 1)
    {
        printf("Choose an operation: +, -, *, /, %%:\n");
        scanf("%c", &operator);
        if (operator== '+' || operator== '-' || operator == '*' || operator == '/' || operator == '%')
        {
            keepWait = 0;
        }
        else
        {
            printf("\nError: The given operator '%c' is invalid.\n\n", operator);
        }
    }

    printf("Choose a number:\n");
    scanf("%d", &num1);
    printf("Choose another number:\n");
    scanf("%d", &num2);

    switch (operator)
    {
    case '+':
        printf("%d + %d = %d\n", num1, num2, num1 + num2);
        break;
    case '-':
        printf("%d - %d = %d\n", num1, num2, num1 - num2);
        break;
    case '*':
        printf("%d * %d = %d\n", num1, num2, num1 * num2);
        break;
    case '/':
        if (num2 == 0)
        {
            printf("Warning: division by 0 is not allowed.\n");
        } else{
            printf("%d / %d = %d\n", num1, num2, num1 / num2);
        }
        break;     
    case '%':
        printf("%d %% %d = %d\n", num1, num2, num1 % num2);
        break;        
    default:
        break;
    }
    



}