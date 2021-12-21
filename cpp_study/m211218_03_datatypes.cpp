#include <iostream>
// https://youtu.be/GQp1zzTwrIg?t=3579
// datatypes

using namespace std;

int main() {
    
    int yearOfBirth = 1995;
    char gender = 'F';
    bool isOlderThan18 = true;
    float averageGrade = 4.2;

    double balance = 92831231;


    cout << "Size of int: " << sizeof(yearOfBirth) << " B" << endl;
    cout << "Size of char: " << sizeof(gender) << " B" << endl;
    // it seems that c++ can only use ascii characters
    // that is the characters are 8 bit size

    cout << "Int min value is " << INT32_MIN << endl;
    cout << "Int max value is " << INT32_MAX << endl;

    cout << "Unsigned int max value is: " << UINT32_MAX << endl;
    cout << "Size used by unsigned int is: " << sizeof(unsigned int) << " bytes\n";

    cout << "Size of bool is: " << sizeof(bool) << " bytes\n";
    cout << "Size of float is: " << sizeof(float) << " bytes\n";
    cout << "Size of double is: " << sizeof(double) << " bytes\n";

}

// next class:
// https://www.youtube.com/watch?v=GQp1zzTwrIg&t=3718s&ab_channel=CodeBeauty