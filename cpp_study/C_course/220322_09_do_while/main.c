// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203422#overview

#include <stdio.h>

void main()
{
    int price, totalPrice = 0;

    printf("This program will ask for the price of products.\nWrite 0 to finish it.\n");

    do
    {
        printf("Enter a price: ");
        scanf("%d", &price);
        totalPrice += price;
    } while (price != 0);

    printf("Total price is %d.\n", totalPrice);
}