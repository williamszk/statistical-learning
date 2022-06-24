// https://www.youtube.com/watch?v=kjBOesZCoqc&ab_channel=3Blue1Brown

#include <stdio.h>

void printVecInt(int *vec)
{
    printf("[%d, %d]\n", vec[0], vec[1]);
}

void addVecInt(int *out, int *vec1, int *vec2)
{
    out[0] = vec1[0] + vec2[0];
    out[1] = vec1[1] + vec2[1];
}

void scalarMult(int *out, int *vec, int scalar)
{
    // should we work with floats all along?
    // we can implement float operations later
    // how to increase the precision of float operations?
    out[0] = scalar * vec[0];
    out[1] = scalar * vec[1];
}

int main()
{

    // a vector represents an arrow
    int vec1[] = {1, 2}; // this is a two-dimensional vector
    // we can represent it in 2-dimenstions

    int vec2[] = {3, -1};

    printf("Vector 1: \t");
    printVecInt(vec1);

    printf("Vector 2: \t");
    printVecInt(vec2);

    int outSumVec[2] = {0};
    addVecInt(outSumVec, vec1, vec2);
    printf("Vector out: \t");
    printVecInt(outSumVec);

    printf("Experiment with scalar multiplication\n");
    int outScalarMult[2] = {0};
    int scalar = 2;
    printf("scalar = %d\n", scalar);

    scalarMult(outScalarMult, vec1, scalar);
    printf("Vector out: \t");
    printVecInt(outScalarMult);

    return 0;
}