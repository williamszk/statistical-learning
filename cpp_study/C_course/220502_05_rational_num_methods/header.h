typedef struct rational
{
    int numerator;
    int denominator;
} Rational;

int calculateGcd(int numA, int numB);

void printRational(Rational num);

Rational incrementRational(Rational num);

Rational decrementRational(Rational num);

Rational addRational(Rational numA, Rational numB);

Rational subRational(Rational numA, Rational numB);

Rational multRational(Rational numA, Rational numB);

Rational divRational(Rational numA, Rational numB);

Rational smallerRational(Rational numA, Rational numB);

Rational biggerRational(Rational numA, Rational numB);

int equalRational(Rational numA, Rational numB);

int notEqualRational(Rational numA, Rational numB);
