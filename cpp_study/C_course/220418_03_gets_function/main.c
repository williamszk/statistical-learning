// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/20203762#overview

#include <stdio.h>

void main()
{
    printf("Write your pets name: ");
    char petName[20];
    gets(petName);

    // Write your pets name: Pablo the Barn Cat
    // Your pet is called: Pablo the Barn Cat

    printf("Your pet is called: %s\n", petName);
}
// gets() reads input including spaces
// scanf() will ignore anything after a space

// we can use puts() function to print a string
// instead of using printf("%s")