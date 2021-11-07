// squared_yeah = (*yeah) * (*yeah);
// https://www.quora.com/What-does-mean-when-I-use-it-in-C-language
#include <stdio.h>

int mult_custom(int *num1) {
    int squared_num = (*num1) * (*num1);
    return squared_num;
}

void main() {
    int yeah = 3;
    
    int squared_yeah = mult_custom(&yeah);

    printf("squared_yeah = %d.\n", squared_yeah);
}

