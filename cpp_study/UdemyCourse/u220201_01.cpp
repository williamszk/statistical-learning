
// https://www.udemy.com/course/the-modern-cpp-20-masterclass/learn/lecture/21293132?start=15#overview

#include <iostream>
#include <string>


int main()
{
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


    return 0;
}












