#include <stdio.h>
#include "header.h"

/**
 * Make numerator negative, if denominator is negative.
 *
 * Sometimes the #calculateGcd function will make the denominator negative.
 * So, for uniformity, we make the numerator negative in this scenarios.
 */
Rational makeNumNeg(Rational num)
{
    if (num.denominator < 0)
    {
        num.numerator *= -1;
        num.denominator *= -1;
    }

    return num;
}

void printRational(Rational num)
{
    printf("%d/%d\n", num.numerator, num.denominator);
}

Rational incrementRational(Rational num)
{
    Rational result;

    int newNum = num.numerator + num.denominator;
    int newDen = num.denominator;

    int gcd = calculateGcd(newNum, newDen);
    newNum /= gcd;
    newDen /= gcd;

    result.numerator = newNum;
    result.denominator = newDen;

    return result;
}

Rational decrementRational(Rational num)
{
    Rational result;

    int newNum = num.numerator - num.denominator;
    int newDen = num.denominator;

    int gcd = calculateGcd(newNum, newDen);
    newNum /= gcd;
    newDen /= gcd;

    result.numerator = newNum;
    result.denominator = newDen;

    result = makeNumNeg(result);

    return result;
}

Rational addRational(Rational numA, Rational numB)
{
    Rational result;

    int newNum = numA.numerator * numB.denominator + numB.numerator * numA.denominator;
    int newDen = numA.denominator * numB.denominator;

    int gcd = calculateGcd(newNum, newDen);
    newNum /= gcd;
    newDen /= gcd;

    result.numerator = newNum;
    result.denominator = newDen;

    result = makeNumNeg(result);

    return result;
}

Rational subRational(Rational numA, Rational numB)
{
    Rational result;

    int newNum = numA.numerator * numB.denominator - numB.numerator * numA.denominator;
    int newDen = numA.denominator * numB.denominator;

    int gcd = calculateGcd(newNum, newDen);
    newNum /= gcd;
    newDen /= gcd;

    result.numerator = newNum;
    result.denominator = newDen;

    result = makeNumNeg(result);

    return result;
}

Rational multRational(Rational numA, Rational numB)
{
    Rational result;

    int newNum = numA.numerator * numB.numerator;
    int newDen = numA.denominator * numB.denominator;

    int gcd = calculateGcd(newNum, newDen);
    newNum /= gcd;
    newDen /= gcd;

    result.numerator = newNum;
    result.denominator = newDen;

    result = makeNumNeg(result);

    return result;
}

Rational divRational(Rational numA, Rational numB)
{
    Rational result;

    int newNum = numA.numerator * numB.denominator;
    int newDen = numA.denominator * numB.numerator;

    int gcd = calculateGcd(newNum, newDen);
    newNum /= gcd;
    newDen /= gcd;

    result.numerator = newNum;
    result.denominator = newDen;

    result = makeNumNeg(result);

    return result;
}

Rational smallerRational(Rational numA, Rational numB)
{
    int newNumA = numA.numerator * numB.denominator;
    int newNumB = numB.numerator * numA.denominator;

    if (newNumA > newNumB)
        return numB;
    else
        return numA;
}

Rational biggerRational(Rational numA, Rational numB)
{
    int newNumA = numA.numerator * numB.denominator;
    int newNumB = numB.numerator * numA.denominator;

    if (newNumA > newNumB)
        return numA;
    else
        return numB;
}

/**
 * Returns 1 if the two rational numbers are equal.
 * Returns 0, otherwise.
*/
int equalRational(Rational numA, Rational numB)
{
    int newNumA = numA.numerator * numB.denominator;
    int newNumB = numB.numerator * numA.denominator;

    if (newNumA == newNumB)
        return 1;
    else
        return 0;
}

/**
 * Returns 1 if the two rational numbers are not equal.
 * Returns 0, otherwise.
*/
int notEqualRational(Rational numA, Rational numB)
{
    int newNumA = numA.numerator * numB.denominator;
    int newNumB = numB.numerator * numA.denominator;

    if (newNumA != newNumB)
        return 1;
    else
        return 0;    
}
