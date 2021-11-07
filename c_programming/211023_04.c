#include <stdio.h>

int func_A(int num1) {
    num1 = num1 + 10;
    return num1;
}

int func_B(int *num2) {
    *num2 = *num2 + 10;
    return *num2;
}

// https://www.tutorialspoint.com/cprogramming/c_function_call_by_reference.htm#:~:text=To%20pass%20a%20value%20by,pointed%20to%2C%20by%20their%20arguments.
void main(){
    int num1 = 1;
    int num2 = 1;

    printf("Before:\n");
    printf("Pass value: %d\n", num1);
    printf("Pass reference: %d\n", num2);

    printf("---------------------\n");
    printf("Apply functions...\n");
    func_A(num1);
    func_B(&num2);

    printf("---------------------\n");
    printf("After:\n");
    printf("Pass by value: %d\n", num1);
    printf("Pass reference: %d\n", num2);

}





