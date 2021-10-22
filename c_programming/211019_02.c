#include <stdio.h>



void main() {
    int age;
    int number_of_children;
    double salary;

    age = 25;
    number_of_children = 1;
    salary = 40000.00;

    if (( age <= 30 ) && (salary >= 30000)) {
        printf("You are a rich and young person.\n");
    } else {
        printf("You are not a rich and young person.\n");
    }

    if (( age <= 30 ) || ( salary >= 30000 )) {
        printf("You are either rich or young or both.\n");
    } else {
        printf("You are not neither rich nor young.\n");
    }

    // if ((age <= 30) && (salary >= 30000) && (number_of_children != 0)) {
    if ((age <= 30) && (salary >= 30000) && !(number_of_children == 0)) {
        printf("You are a rich young parent.\n");
    } else {
        printf("You are not a rich and young parent.\n");
    }
}

