#include <stdio.h>

int add( int num1, int num2) {
    return num1 + num2;
}

void main() {
    int num1 = 10;
    int num2 = 3;
    printf("%d + %d = %d\n", num1, num2, add(num1, num2));
}








