#include <stdio.h>
#include <math.h>

int main(){

    // how to build constants in C?
    // # is used to change the preprocessor
    #define PI 3.141593
    printf("PI is %f\n", PI);

    printf("from the math library M_PI is %.10f\n", M_PI);

    return 0;
}