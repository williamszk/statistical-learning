#include <stdio.h>

#define v 33

int my_func(int z){
    int t;
    t = z + v;
    return t;
}

int main(){
    printf("This is the result of my_func: %d.\n", my_func(22));
}