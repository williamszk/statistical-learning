// https://www.tutorialspoint.com/cprogramming/c_function_call_by_reference.htm

// Function definition to swap the values
/* function definition to swap the values */
void swap(int *x, int *y) {

   int temp;
   temp = *x;    /* save the value at address x */
   *x = *y;      /* put y into x */
   *y = temp;    /* put temp into y */
  
   return;
}

#include <stdio.h>

int main(){
    int a = 100;
    int b = 200;

    printf("Before swap value of a is: %d.\n", a);
    printf("Before swap value of b is: %d.\n", b);

    swap(&a, &b);

    printf("After swap value of a is: %d.\n", a);
    printf("After swap value of b is: %d.\n", b);

    return 0;
}




