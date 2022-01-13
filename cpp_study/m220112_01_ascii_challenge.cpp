// https://youtu.be/GQp1zzTwrIg?t=4262
// input user info and code in ASCII

#include <iostream>
using namespace std;

int main()
{
    char character1, character2, character3, character4, character5;
    cout << "Enter 5 letters: ";
    cin >> character1 >> character2 >> character3 >> character4 >> character5;
    cout << "ASCII message: " << int(character1) << " - " << int(character2) << " - " << 
    int(character3) << " - " << int(character4) << " - " << int(character5) << endl;
}