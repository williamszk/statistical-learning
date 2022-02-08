/* Cookbook for C++
 * */


// -------------------------------------------------------- //




// -------------------------------------------------------- //
// Some arguments that we can include in the compiler command
// -O can make the executable run faster, but compiling may take
// longer.
g++ -O -o HelloWorld HelloWorld.cpp
g++ -g -o HelloWorld HelloWorld.cpp

// -------------------------------------------------------- //

const double density = 45.621;
double tolerance = 0.000000000001;
double tolerance = 1.0e-12;

// -------------------------------------------------------- //

int integer1;
short int integer2;
long int integer3;

// -------------------------------------------------------- //

signed long int integer4; // signed is unnecessary
unsigned int integer5;

// -------------------------------------------------------- //
#include <cmath>
int main(int argc, char * argv[])
{
    double x = 7.8, y = 1.65, u = -3.4, z;
    z = fmod(x, y);
    // remainder when x is divided by y
    // z is 1.2 since 7.8 = 4*1.65 + 1.2
    z = atan2(y, x); // inverse tangent (in radians) of
    // angle between the vector
    // (x, y) and the positive x-axis
    // note the ordering of y and x in
    // calling the function atan2
    // z is 0.208465
    z = fabs(u);
    // Absolute value of u
    // z is 3.4
    // note fabs should not be confused
    // with abs (the integer equivalent)
    return 0;
}


// -------------------------------------------------------- //

#include <cmath>
int main(int argc,
{
    double x = 1.0,
    z = x/y;
    z = x*y;
    z = sqrt(x);
    z = exp(y);
    z = pow(x, y);
    z = M_PI;
    char * argv[])
    y = 2.0, z;
    // division
    // multiplication
    // square root
    // exponential function
    // x to the power of y
    // z stores the value of pi

    return 0;
}

// -------------------------------------------------------- //

int array1[2];
double array2[2][3];

array1[0] = 1; // Note that indexing begins from 0
array1[1] = 10;
array2[0][0] = 6.4;
array2[0][1] = -3.1;
array2[0][2] = 55.0;
array2[1][0] = 63.0;
array2[1][1] = -100.9;
array2[1][2] = 50.8;

array1[0]++; // increments the value of this entry by 1
array2[1][2] = array2[0][1] + array2[1][0];


// -------------------------------------------------------- //
// https://www.cpp.edu/~elab/ECE114/Array.html#:~:text=A%20typical%20declaration%20for%20an,the%20size%20of%20the%20array.
int foo [5] = { 16, 2, 77, 40, 12071 }; 

// -------------------------------------------------------- //

std::cout << "Hello C++" << std::endl;

int age {21};

std::cout << "Age: " << age << std::endl;

std::cerr << "Error message: Something is wrong." << std::endl;

std::clog << "Log message: Something happened." << std::endl;

int age1;
std::string name;

std::cout << "Please type your name and age: " << std::endl;
std::cin >> name;
std::cin >> age1;

std::cout << "Hello, " << name << ". You are " << age1 << " years old." << std::endl;


std::string fullName;
std::cout << "Please type your full name: " << std::endl;
std::getline(std::cin, fullName);

std::cout << "Hi from Mars, " << fullName << std::endl;


// -------------------------------------------------------- //






// -------------------------------------------------------- //





// -------------------------------------------------------- //





// -------------------------------------------------------- //








// -------------------------------------------------------- //








// -------------------------------------------------------- //











// -------------------------------------------------------- //





// -------------------------------------------------------- //




// -------------------------------------------------------- //







// -------------------------------------------------------- //




// -------------------------------------------------------- //


// -------------------------------------------------------- //


















