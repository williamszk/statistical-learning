#include <stdio.h>
#include <stdlib.h>

int main()
{

    int money, grade;
    printf("Enter money and grade: \n");
    scanf("%d%d", &money, &grade);

    // and logical operator
    if (money < 50 && grade > 90)
    {

    }

    // or logical operator
    if (money < 50 || grade > 90)
    {

    }

    // not logical operator
    if (!(grade > 80))
    {

    }

    return 0;
}