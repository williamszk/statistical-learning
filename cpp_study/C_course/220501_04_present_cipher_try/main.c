// https://www.youtube.com/watch?v=tLa0IBpOE_I&ab_channel=CihangirTezcan

#include <stdio.h>
#define LONG_SIZE 64


void main()
{
    // the master key has 128 bits, which are 2 x 64 bits, and 2 x 16 hex.
    unsigned long key[2] = {0x0000000000000000, 0x0000000000000000};
    // given that the size of long is 64bits, we need to use an array to store all necessary bits

    // the round key are the 64 left most bits of the master key
    unsigned long roundKey = key[1];

    // how to rotate 67 times an array of words?
    unsigned long keyExeperiment1[2] = {0x0000000000000000, 0x000000000000000F};

    // just an experiment...
    unsigned long exper01 = 0xF000000000000000;
    printf("%lx\n", exper01 >> 64 - 3);

    
    
    // a simpler question is how to make a bit shift with array representation of unsigned long?
    // an experiment with 1 left bit shift
    unsigned long keyExeperiment2[2] = {0x0000000000000000, 0xF000000000000000};
    printf("Original Array: 0x%lx 0x%lx\n", keyExeperiment2[0], keyExeperiment2[1]);

    int shift = 1;
    unsigned long newA0 = keyExeperiment2[0] << shift | keyExeperiment2[1] >> LONG_SIZE - shift;
    unsigned long newA1 = keyExeperiment2[1] << shift;

    unsigned long keyExperiment1Shifted1[2] = {newA0, newA1};
    printf("After 1 left bit shift: 0x%lx 0x%lx\n", keyExperiment1Shifted1[0], keyExperiment1Shifted1[1]);
}