// https://youtu.be/GQp1zzTwrIg?t=5753

#include <iostream>
using namespace std;

int main()
{
    // the user enters side lenghts of the triangle
    // the program should be able to tell if the triangle is equilateral
    // isosceles or scalene

    float triLength1, triLength2, triLength3;

    cout << "This program determines if a triangle is equilateral, isosceles or scalene." << endl;
    cout << "Type one of the lenghts of the triangle (1/3): ";
    cin >> triLength1;
    cout << "Type one of the lenghts of the triangle (2/3): ";
    cin >> triLength2;
    cout << "Type one of the lenghts of the triangle (3/3): ";
    cin >> triLength3;

    if (triLength1 == triLength2 && triLength2 == triLength3) {
        cout << "The triangle is equilateral." << endl;
    } else if (triLength1 == triLength2 || triLength1 == triLength3 || triLength2 == triLength3) {
        // this option excludes the possibility of all sides being equal
        // because the first if already captures this
        cout << "The triangle is isosceles." << endl;
    } else {
        // scalene triangle is a triangle that has no equal sides
        cout << "The triangle is scalene." << endl;
    }
}


// This program determines if a triangle is equilateral, isosceles or scalene.
// Type one of the lenghts of the triangle (1/3): 1
// Type one of the lenghts of the triangle (2/3): 2
// Type one of the lenghts of the triangle (3/3): 3
// The triangle is scalene.

// This program determines if a triangle is equilateral, isosceles or scalene.
// Type one of the lenghts of the triangle (1/3): 1
// Type one of the lenghts of the triangle (2/3): 1
// Type one of the lenghts of the triangle (3/3): 2
// The triangle is isosceles.

// This program determines if a triangle is equilateral, isosceles or scalene.
// Type one of the lenghts of the triangle (1/3): 10
// Type one of the lenghts of the triangle (2/3): 10
// Type one of the lenghts of the triangle (3/3): 10
// The triangle is equilateral.
