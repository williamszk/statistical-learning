int calculateGcd(int numA, int numB)
{
    int remainder = 1; // set to 1 just to pass the first while condition
    int answer;

    if (numA < numB)
    { // we need to make numA is biggern than numB
        int tempC;
        tempC = numA;
        numA = numB;
        numB = tempC;
    }

    while (remainder != 0)
    {
        remainder = numA % numB;

        numA = numB;
        numB = remainder;
    }
    answer = numA; // the last remainder before it became 0;

    return answer;
}