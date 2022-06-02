#include <iostream>

// there are different ways to declare variables
struct Rectangle {
    int length;
    int breadth;
} r1, r2, r3;
// we can declare the rectangle strucuture just inside the definition
// those variables can be accessed by all functions

struct Card {
    int facevalue;
    int color;
    int shape;
};

// we can declare the the variable myCard01
//  and this variable can be accessed by all functions
struct Card myCard01;

int main()
{




    return 0;
}