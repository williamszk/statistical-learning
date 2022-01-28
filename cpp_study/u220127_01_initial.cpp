/* Notes on the C++ course:
 * https://www.udemy.com/course/the-modern-cpp-20-masterclass/learn/lecture/24458218#overview
 * How to compile for C++ 20
 * g++ -std=c++2a main.cpp
 * */
#include <iostream>

constexpr int get_value() {
    return 3;
}

int main(int argc, char **argv) {
    std::cout << "Hello World in C++!" << std::endl;
    return 0;
}

