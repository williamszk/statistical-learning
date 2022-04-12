// Can we return a pointer in a function
// and then use the pointer to dereference and find its value?

#include <stdio.h>

int *funcRetPtrInt()
{
    int myInt = 12345;
    int *ptrMyInt = &myInt;
    return ptrMyInt;
}

void main()
{
    int *ptrMyIntReturn = funcRetPtrInt();

    printf("Returned pointer: %d\n", *ptrMyIntReturn);
}

// root@d03aa4273aef:~/statistical-learning/cpp_study/C_course/220411_01_return_pointer_function# ./a.out 
// Returned pointer: 12345

// It works!
// we can just return the pointer to a object
// can we do this using arrays?
// and using structs?