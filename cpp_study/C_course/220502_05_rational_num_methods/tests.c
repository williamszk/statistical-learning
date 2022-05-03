#include <stdio.h>
#include "header.h"

void main()
{
    Rational numRational;
    Rational numRationalA;
    Rational numRationalB;
    Rational answerRational;
    int numA;
    int numB;
    int expectedAnsw;

    printf("\n// ================ Test 1 ========================//\n");
    numA = 102;
    numB = 38;
    expectedAnsw = 2;
    printf("Result: \t%d\nExpected: \t%d\n", calculateGcd(numA, numB), expectedAnsw);

    printf("\n// ================ Test 2 ========================//\n");
    numA = 38;
    numB = 102;
    expectedAnsw = 2;
    printf("Result: \t%d\nExpected: \t%d\n", calculateGcd(numA, numB), expectedAnsw);

    printf("\n// ================ Test 3 ========================//\n");
    numRational.numerator = 2;
    numRational.denominator = 3;

    answerRational = incrementRational(numRational);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "5/3");

    printf("\n// ================ Test 4 ========================//\n");
    numRational.numerator = 10;
    numRational.denominator = 15;

    answerRational = incrementRational(numRational);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "5/3");

    printf("\n// ================ Test 5 ========================//\n");
    numRational.numerator = 10;
    numRational.denominator = 15;

    answerRational = decrementRational(numRational);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "-1/3");

    printf("\n// ================ Test 6 ========================//\n");
    numRationalA.numerator = 4;
    numRationalA.denominator = 5;

    numRationalB.numerator = 3;
    numRationalB.denominator = 4;

    answerRational = addRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "31/20");

    printf("\n// ================ Test 7 ========================//\n");
    numRational.numerator = 2;
    numRational.denominator = 98;

    answerRational = decrementRational(numRational);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "-48/49");

    printf("\n// ================ Test 8 ========================//\n");
    numRationalA.numerator = 4;
    numRationalA.denominator = 5;

    numRationalB.numerator = 11;
    numRationalB.denominator = 5;

    answerRational = addRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "3/1");

    printf("\n// ================ Test 8 ========================//\n");
    printf("//  What happens if one number is negative? \n");
    numRationalA.numerator = 4;
    numRationalA.denominator = 5;

    numRationalB.numerator = 11;
    numRationalB.denominator = -5;

    answerRational = addRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "-7/5");

    printf("\n// ================ Test 9 ========================//\n");
    numRationalA.numerator = 4;
    numRationalA.denominator = 5;

    numRationalB.numerator = 11;
    numRationalB.denominator = 5;

    answerRational = subRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "-7/5");

    printf("\n// ================ Test 10 ========================//\n");
    numRationalA.numerator = 99;
    numRationalA.denominator = 5;

    numRationalB.numerator = 8;
    numRationalB.denominator = 13;

    answerRational = subRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "1247/65");

    printf("\n// ================ Test 11 ========================//\n");
    numRationalA.numerator = 8;
    numRationalA.denominator = 5;

    numRationalB.numerator = 8;
    numRationalB.denominator = 13;

    answerRational = subRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "64/65");

    printf("\n// ================ Test 12 ========================//\n");
    numRationalA.numerator = 8;
    numRationalA.denominator = 5;

    numRationalB.numerator = 8;
    numRationalB.denominator = -13;

    answerRational = multRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "-64/65");

    printf("\n// ================ Test 13 ========================//\n");
    numRationalA.numerator = 8;
    numRationalA.denominator = 5;

    numRationalB.numerator = 8;
    numRationalB.denominator = 13;

    answerRational = multRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "64/65");

    printf("\n// ================ Test 14 ========================//\n");
    numRationalA.numerator = 2;
    numRationalA.denominator = 3;

    numRationalB.numerator = 4;
    numRationalB.denominator = 5;

    answerRational = divRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "5/6");

    printf("\n// ================ Test 15 ========================//\n");
    numRationalA.numerator = 8;
    numRationalA.denominator = 5;

    numRationalB.numerator = 8;
    numRationalB.denominator = 13;

    answerRational = divRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "13/5");

    printf("\n// ================ Test 16 ========================//\n");
    numRationalA.numerator = 8;
    numRationalA.denominator = 5;

    numRationalB.numerator = 8;
    numRationalB.denominator = 13;

    answerRational = smallerRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "8/13");

    printf("\n// ================ Test 17 ========================//\n");
    numRationalA.numerator = 2;
    numRationalA.denominator = 3;

    numRationalB.numerator = 4;
    numRationalB.denominator = 5;

    answerRational = smallerRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "2/3");

    printf("\n// ================ Test 18 ========================//\n");
    numRationalA.numerator = 2;
    numRationalA.denominator = 3;

    numRationalB.numerator = 4;
    numRationalB.denominator = 5;

    answerRational = biggerRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "4/5");

    printf("\n// ================ Test 19 ========================//\n");
    numRationalA.numerator = 978;
    numRationalA.denominator = 23;

    numRationalB.numerator = 22;
    numRationalB.denominator = 22222;

    answerRational = biggerRational(numRationalA, numRationalB);
    printf("Result: \t");
    printRational(answerRational);
    printf("Expected: \t%s\n", "978/23");

    printf("\n// ================ Test 20 ========================//\n");
    numRationalA.numerator = 4;
    numRationalA.denominator = 5;

    numRationalB.numerator = 4;
    numRationalB.denominator = 7;

    expectedAnsw = equalRational(numRationalA, numRationalB);
    printf("Result: \t%d\n", expectedAnsw);
    printf("Expected: \t%s\n", "0");

    printf("\n// ================ Test 21 ========================//\n");
    numRationalA.numerator = 4312;
    numRationalA.denominator = 5;

    numRationalB.numerator = 4312;
    numRationalB.denominator = 5;

    expectedAnsw = equalRational(numRationalA, numRationalB);
    printf("Result: \t%d\n", expectedAnsw);
    printf("Expected: \t%s\n", "1");

    printf("\n// ================ Test 22 ========================//\n");
    numRationalA.numerator = 4;
    numRationalA.denominator = 5;

    numRationalB.numerator = 20;
    numRationalB.denominator = 25;

    expectedAnsw = equalRational(numRationalA, numRationalB);
    printf("Result: \t%d\n", expectedAnsw);
    printf("Expected: \t%s\n", "1");

    printf("\n// ================ Test 23 ========================//\n");
    numRationalA.numerator = 4;
    numRationalA.denominator = 5;

    numRationalB.numerator = 20;
    numRationalB.denominator = 25;

    expectedAnsw = notEqualRational(numRationalA, numRationalB);
    printf("Result: \t%d\n", expectedAnsw);
    printf("Expected: \t%s\n", "0");

    printf("\n// ================ Test 24 ========================//\n");
    numRationalA.numerator = 421;
    numRationalA.denominator = 522;

    numRationalB.numerator = 20;
    numRationalB.denominator = 25;

    expectedAnsw = notEqualRational(numRationalA, numRationalB);
    printf("Result: \t%d\n", expectedAnsw);
    printf("Expected: \t%s\n", "1");
}