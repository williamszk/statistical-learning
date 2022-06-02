#include <iostream>

// https://www.udemy.com/course/datastructurescncpp/learn/lecture/13612044?start=0#overview

struct Rectangle
{
    int length;
    int breadth;
};

struct Complex
{
    int real;
    int imaginary;
};

struct Student
{
    int roll;            // 4 bytes
    char name[25];       // 25 bytes
    char department[10]; // 10 bytes
    char address[50];    // 50 bytes
};                       // this whole struct takes 89 bytes

struct Card
{
    int facevalue; // 4 bytes
    int shape;     // 4 bytes
    int color;     // 4 bytes
}; // a total of 12 bytes

int main()
{
    // delcaration and initialization
    struct Rectangle myRect = {
        10, // sizeof 4 bytes
        5,  // sizeof 4 bytes
    };
    // total size of struct is 8 bytes

    // the struct lives inside the stack frame of the memory

    std::cout << "Size of a structure: " << sizeof(myRect) << std::endl;

    // change value inside the structure
    myRect.length = 99;

    int areaRect = myRect.length * myRect.breadth;
    std::cout << "Area of rectangle: " << areaRect << std::endl;

    // another way to declare and assign values to the structure
    struct Student s;

    s.roll = 1111;
    // s.name = "Bob Martin";

    // this is another way we can give values to structures
    struct Card myCard = {
        .facevalue = 10,
        .shape = 1,
        .color = 3,
    };

    // we can create an array of strucutures, which in our case
    // will be a deck
    struct Card myDeck[52];
    // each card will occupy a total of 12*52 = 624 bytes

    return 0;
}