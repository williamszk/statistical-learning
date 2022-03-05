#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float derivative(float slopecoeff, float xvar, float powercoeff)
{
    float derivativeValue = slopecoeff*powercoeff*pow(xvar, powercoeff-1);
    return derivativeValue;
}

int main()
{
    float derivativeValue = derivative(2,2,2);

    printf("The derivative of c*n^2: %f\n", derivativeValue);

    return 0;
}

// gcc main.c -lm