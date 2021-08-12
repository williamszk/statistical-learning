#include <stdio.h>
#include <stdlib.h>

// assignment operator

int main(){

    char agestring[10];
    int age;
    int bonus;

    // https://www.mikedane.com/programming-languages/c/getting-input-from-users/#:~:text=In%20C%2C%20we%20can%20get%20user%20input%20like%20this%3A&text=%2F%2F%20strings%20char%20name%5B10,printf(%22Hello%20%25s!


    printf("Enter you age: ");
    fgets(agestring, 10, stdin);
    printf("Your age is: %s", agestring);

    // https://www.educative.io/edpresso/how-to-convert-a-string-to-an-integer-in-c
    
    age = atoi(agestring);
    // atoi needs stdlib.h
    if (age >= 45){
        bonus = 1000;
    } else {
        bonus = 500;
    }

    printf("Your bonus is: %d\n", bonus);

    return 0;
}