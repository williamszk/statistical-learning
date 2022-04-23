// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168548#questions
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168556#questions
struct date
{
    int day;
    int month;
    int year;
};
// can we include arrays inside structs?
// can we include structs inside structs?

struct point
{
    int x;
    int y;
};

struct address
{
    char state[20];
    char city[10];
    char street[15];
    int number;
};

// we can include arrays inside structs

void main()
{
    // declare a struct
    // it is like declaring a class instance
    struct date birthDate;
    // In Java we would use public methods to assign values to fields in a class
    // in Go we would create a struct instance using:
    // person := Person {
    // name: "Bob",
    // }
    struct point myFocalPoint;

    struct address myDogAddress;

    birthDate.day = 2;
    birthDate.month = 9;
    birthDate.year = 1993;
    // In C, I think we can't just print a struct
    // In Go we can print a struct
}
// Why do we use typedef when definig structs?

// Why do we include void as argument of a function instead of just let be empty
