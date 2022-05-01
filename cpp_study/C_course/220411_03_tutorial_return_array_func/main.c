// https://www.tutorialspoint.com/cprogramming/c_return_arrays_from_function.htm#:~:text=C%20programming%20does%20not%20allow,array's%20name%20without%20an%20index.

#include <stdio.h>

/*
C programming does not allow to return an entire array as an argument 
to a function. However, you can return a pointer to an array by specifying 
the array's name without an index.
*/

/*
Second point to remember is that C does not advocate to return the 
address of a local variable to outside of the function, so you would 
have to define the local variable as static variable.
*/
// So the keyword static makes the local variable global?
// What does static do in C?

void main()
{
    
}