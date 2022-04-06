/*
 * https://www.udemy.com/course/java-the-complete-java-developer-course/learn/quiz/4585756#overview
 */
#include <iostream>
#include <math.h>

long toMilesPerHour(double kilometersPerHour)
{
    if (kilometersPerHour < 0)
    {
        return -1;
    }
    else
    {
        return (long)std::round(kilometersPerHour / 1.609);
    }
}

void printConversion(double kilometersPerHour)
{
    double milesPerHour = toMilesPerHour(kilometersPerHour);
    if (milesPerHour == -1)
    {
        std::cout << "Invalid Value" << std::endl;
    }
    else
    {
        std::cout << kilometersPerHour << " km/h = " << milesPerHour << " mi/h" << std::endl;
    }
}

int main()
{
    std::cout << "Should be 1 |  " << toMilesPerHour(1.5) << std::endl;
    std::cout << "Should be 6 |  " << toMilesPerHour(10.25) << std::endl;
    std::cout << "Should be -1 |  " << toMilesPerHour(-5.6) << std::endl;
    std::cout << "Should be 16 |  " << toMilesPerHour(25.24) << std::endl;
    std::cout << "Should be 47 |  " << toMilesPerHour(75.114) << std::endl;

    std::cout << std::endl;

    printConversion(1.5);
    printConversion(10.25);
    printConversion(-5.6);
    printConversion(25.42);
    printConversion(75.114);
}