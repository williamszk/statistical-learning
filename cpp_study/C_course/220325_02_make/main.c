// https://www.youtube.com/watch?v=ix5jPkxsr7M&list=PL6GTh-pvTWynG3kf_chsN2MZ2qLcuKe78&index=52&ab_channel=freeCodeCamp.org

#include <stdio.h>


void main()
{
    // *hi is accessing the value slot 
    // where hi is a pointer (an address) it self
    char *hi = "Hello World, this is a new form of declaring a string";
    printf("%s\n", hi);

    float afloat = 0.10;
    printf("%f\n", afloat);
    printf("%.50f\n", afloat);
    // 0.10000000149011611938476562500000000000000000000000
    // this is the maximum precion of a float

    double adouble = 0.10;
    printf("%f\n", adouble);
    printf("%.50f\n", adouble);
    // 0.10000000000000000555111512312578270211815834045410
    // we can see that the double can be more precise compared to the float

}

// make main
// by default it looks for a c file