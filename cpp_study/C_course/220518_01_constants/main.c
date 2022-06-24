// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25774624?start=15#questions
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25774626#questions
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/25774634#questions

#include <stdio.h>

int main()
{
    // ========================================================================== //
    const int myAge = 10;

    printf("myAge = %d\n", myAge);

    // this will give an error
    // myAge = 20;

    // if we write const without the type, C will put an int by default
    const temp = 22;
    printf("temp = %d\n", temp);

    // ========================================================================== //

    // a pointer to a constant
    // the value can't be changed but we can change the pointer
    const int *ptr;

    // an example
    int aValue = 30;
    ptr = &aValue;

    printf("*ptr = %d\n", *ptr);

    // can we change the value of aValue using the pointer?
    // *ptr = 34;
    // this gives an error, because the pointer is defined with a constant

    aValue = 34;
    // but using the variable aVlaue itself we can change the value of the variable
    // but we can't use the pointer to change the value of the variable

    // const int *ptr; simply means that we can't use the *ptr to change the value of the variable
    // but we can assign other variable's address to the pointer

    // ========================================================================== //

    // an example of a pointer that is constant
    int age1 = 99;

    int *const ptr1 = &age1;
    
    printf("*ptr1 = %d\n", *ptr1);

    // we can change the content of the variable using the pointer
    *ptr1 = 44;

    printf("*ptr1 = %d\n", *ptr1);
    
    // but we can't assign another variable's address to the constant pointer
    // ptr1 = &aValue; // this will give an error

    // we have two different concepts: "Constant Pointer", "A Pointer to a Constant"

    // ========================================================================== //

    int aVal3 = 88;
    const int *const ptr3 = &aVal3;

    // this is a constant pointer which points to a constant value
    // neither the pointer can the changed nor the value
    // of the variable that is pointed be changed through the pointer

    int aVal4 = 87;
    // ptr3 = &aVal4; // this is not allowed
    // *ptr3 = 87; // this is also not allowed

    aVal3 = 76;
    // but this is allowed

    // ========================================================================== //    

    const int aVal5 = 78;
    const int *const ptr5 = &aVal5;
    // this is an example of a constant pointer, which points to a value that is also a constant
    // 
    // *const ptr means that the pointer it self can't be assigned any new value
    // we statement also means that we can't change the content of the pointer using the pointer
    // and also that we can't alter the content of variable


    return 0;
}