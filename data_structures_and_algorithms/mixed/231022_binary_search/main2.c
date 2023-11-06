// Objective: see the difference that ++ does when put before or after
// inside a loop and in assignment operator

// I know that in JS putting before or after will change how the return value 
// of the operator works.


#include <stdio.h>

int main(){

    int i;

    for (i=0; i<10;i++){
        printf("first: %d\n", i);
    }

    for (i=0; i<10;++i){
        printf("second: %d\n", i);
    }
    // Conclusion: inside a loop putting before or after will not make any difference.
    // 

    i = 0;
    int myVal1 = i++;
    printf("assignment 01: %d\n", myVal1); // 0

    i = 0;
    int myVal2 = ++i;
    printf("assignment 02: %d\n", myVal2); // 1

    // In the return value of the operator doing the ++ before will return the 
    // value after the operation is complete.
    // If the operation is done after, then the return value will be the value
    // before the operation is complete.


    return 0;
}