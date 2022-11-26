#include <stdio.h>

int main(){

    int a = 12;

    void *ptr = &a;

    // explicit type casting
    printf("%d\n", *(int*)(ptr) );
    // first do an explicit casting
    // and then make a dereferencing

    return 0;
}