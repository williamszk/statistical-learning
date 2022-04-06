// https://youtu.be/GQp1zzTwrIg?t=4696

#include <iostream>
using namespace std;

// exercise: enters integer number
// the program needs to tell if the number is even or odd

int main()
{
    int userNumber;
    cout << "What is your number?: ";
    cin >> userNumber;
    if (userNumber % 2 == 0)
    {
        cout << "Your number is even." << endl;
    }
    else
    {
        cout << "Your number is odd." << endl;
    }
}

// https://youtu.be/GQp1zzTwrIg?t=5753
// next class