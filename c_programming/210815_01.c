#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// https://www.hackerrank.com/challenges/sum-numbers-c/problem



int main(){

    int int_first;
    int int_second;

    float float_first;
    float float_second;

    // printf("Type two integers, separated by space:");
    scanf("%d %d", &int_first, &int_second);

    // printf("Type two floats, separeted by space:");
    scanf("%f %f", &float_first, &float_second);

    printf("%d %d\n", int_first + int_second, int_first - int_second);
    printf("%.1f %.1f\n", float_first + float_second, float_first - float_second);



    return 0;
}