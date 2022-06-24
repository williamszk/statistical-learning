// https://www.youtube.com/watch?v=GQp1zzTwrIg&t=8474s&ab_channel=CodeBeauty

#include <iostream>

int main()
{

    int hostUserNum, guestUserNum;
    std::cout << "Host: ";
    std::cin >> hostUserNum;
    // system will pass a command to the terminal
    // this will depend on the operating system
    // that will be running
    system("clear");

    std::cout << "Guest: ";
    std::cin >> guestUserNum;

    (hostUserNum == guestUserNum) ? std::cout << "Correct!" : std::cout << "Failed!";

    std::cout << std::endl;

    return 0;
}

// stopped at:
// https://youtu.be/GQp1zzTwrIg?t=10891
