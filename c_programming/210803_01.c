#include <stdio.h>
#include <stdlib.h>

int main(){
    char agestring[10];
    int age;
    int bonus;

    printf("Enter your age: ");
    fgets(agestring, 10, stdin);

    // printf("This is your age: %s", agestring);

    age = atoi(agestring);
    // atoi function will convert to 0 if an invalid argument is passed
    // so to avoid giving the wrong answer to the user we need to create
    // an if statement
    if (age == 0){
        printf("You entered an invalid age, so your bonus cannot be calculated.\n");
    } else {
        if (age > 45){
            bonus = 1000;
        } else {
            bonus = 500;
        }
        printf("Your age is %d, so your bonus is %d.\n", age, bonus);
    }


    return 0;
}