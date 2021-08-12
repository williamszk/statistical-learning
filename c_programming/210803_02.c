#include <stdio.h>
#include <stdlib.h>

int main(){
    char first_name[10];
    char last_name[10];

    printf("Enter your first name: ");
    fgets(first_name, 10, stdin);

    printf("Enter your last name: ");
    fgets(last_name, 10, stdin);

    printf("Hi, %s %s!\n", first_name, last_name);
    // there is a problem with this program
    // 1. when I enter the first_name and the last_name
    // the print will show them in different lines
    // 2. and if I enter a long string the output
    // is not as I expect

    // the fgets function terminates with \0
    // which are null termined strings

    return 0;
}