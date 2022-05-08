#include <stdio.h>

int calculateGcd(int numA, int numB)
{
    int remainder = 1; // set to 1 just to pass the first while condition
    int answer;

    while (remainder != 0)
    {
        remainder = numA % numB;

        numA = numB;
        numB = remainder;
    }
    answer = numA; // the last remainder before it became 0;

    return answer;
}

int calculateGcdRecur(int numA, int numB)
{
    if (numB == 0)
        return numA;

    return calculateGcdRecur(numB, numA % numB);
}


void main()
{
    int numA;
    int numB;
    int expectedAnsw;

    printf("\n// ================ Experiment 1 ========================//\n");
    numA = 102;
    numB = 38;
    expectedAnsw = 2;
    printf("Result: \t%d\nExpected: \t%d\n", calculateGcd(numA, numB), expectedAnsw);
    
    printf("\n// ================ Experiment 2 ========================//\n");
    numA = 42823;
    numB = 6409;
    expectedAnsw = 17;
    printf("Result: \t%d\nExpected: \t%d\n", calculateGcd(numA, numB), expectedAnsw);

    printf("\n// ================ Experiment 3 ========================//\n");
    numA = 102;
    numB = 38;
    expectedAnsw = 2;
    printf("Result: \t%d\nExpected: \t%d\n", calculateGcdRecur(numA, numB), expectedAnsw);

    printf("\n// ================ Experiment 4 ========================//\n");
    numA = 42823;
    numB = 6409;
    expectedAnsw = 17;
    printf("Result: \t%d\nExpected: \t%d\n", calculateGcdRecur(numA, numB), expectedAnsw);

}