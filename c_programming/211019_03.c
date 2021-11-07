#include <stdio.h>

int add( int num1, int num2) {
    return num1 + num2;
}

void main() {
    int num1 = 10;
    int num2 = 3;
    int num3 = add(num1, num2);
    printf("%d + %d = %d\n", num1, num2, num3);
}


// parameters passed by reference
// parameters passed by value
// what is the difference?

// pass by address (reference)
// pass by value




