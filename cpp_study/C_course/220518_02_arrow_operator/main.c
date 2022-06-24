// https://www.geeksforgeeks.org/arrow-operator-in-c-c-with-examples/
// C program to show Arrow operator
// used in structure

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Creating the structure
struct student
{
    char name[80];
    int age;
    float percentage;
};

// Creating the structure object
struct student *emp = NULL;

// what happens when we declare a struct outside of a function?
// struct student emp2;


// Driver code
int main()
{
    // printf("emp->age = %d\n", emp->age);
    // this gives an error

    // printf("0. emp2.age = %d\n", emp2.age);
    // this will give some strange result on a piece of code below...
    // I don't understand

    // Why malloc is used?

    // Assigning memory to struct variable emp
    emp = (struct student *)
        malloc(sizeof(struct student));

    printf("1. emp->age = %d\n", emp->age); // gives meaningless value
    // malloc will allocate memory to a variable
    // this is necessary when we declare the variable outside a function

    // Assigning value to age variable
    // of emp using arrow operator
    emp->age = 18;
    printf("1. emp->age = %d\n", emp->age);
    // printf("(*emp).age = %s\n", (*emp).age); // this will give an error
    // the terminal becomes unresponsive   

    // Printing the assigned value to the variable
    printf("emp->name = %s\n", emp->name); // gives meaningless value
    // emp->name = "Bob Martin";
    strcpy(emp->name, "Bob Martin"); // we use strcpy to assign a string to the struct field
    printf("emp->name = %s\n", emp->name);

    struct student stud2;
    printf("stud2.age = %d\n", stud2.age); // this will return meaningless value, given that 
    // in the case wehre we declare the struct inside the function, there is no need to do memory allocation

    // the arrow operator "->" is used when we want to access the property
    // of a struct, but we want to use the pointer to the struct

    // below already gives an error
    // printf("stud2->age = %d\n", stud2->age);



    return 0;
}