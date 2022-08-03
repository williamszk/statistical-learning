// https://www.udemy.com/course/the-modern-cpp-20-masterclass/learn/lecture/21293132?start=0#overview
#include <iostream>
#include <string>

int main()
{
    int age;

    std::string name;

    std::cout << "Please type in your last name: " << std::endl;
    std::cin >> name;
    // with cin we can't include space between names
    // cin will consider it to be the next entry.

    std::cout << "Please type in your age: " << std::endl;
    std::cin >> age;

    std::cout << "Hello " << name << "! You are " << age << " years old." << std::endl;

    std::cerr << "This is an error message." << std::endl;

    std::clog <<  "This is a log message: Something happened." << std::endl;

    std::string fullName;

    std::getline(std::cin, fullName);    

    std::cout << "Hello " << fullName << std::endl;


    return 0;
}