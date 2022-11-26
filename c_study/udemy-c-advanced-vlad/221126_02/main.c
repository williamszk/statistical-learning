
// generic swap function
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void genericSwap(void *num1, void* num2, unsigned int size)
{
    void *tempMem = malloc(size);

    // memory copy
    // void * memcpy(void *dest, const void *src, size_t, num)
    memcpy(tempMem, num1, size);

    memcpy(num1, num2, size);
    memcpy(num2, tempMem, size);
    free(tempMem);
}

int main(){
    printf("Swap example using int:\n");
    int num1 = 13;
    int num2 = 44;
    printf("before: \tnum1=%d, num2=%d\n", num1, num2);
    genericSwap(&num1, &num2, sizeof(num1));
    printf("after:  \tnum1=%d, num2=%d\n", num1, num2);

    printf("\nSwap example using double:\n");
    double num11 = 13.0;
    double num21 = 44.0;
    printf("before: \tnum11=%lf, num21=%lf\n", num11, num21);
    genericSwap(&num11, &num21, sizeof(num11));
    printf("after:  \tnum11=%lf, num21=%lf\n", num11, num21);
}
