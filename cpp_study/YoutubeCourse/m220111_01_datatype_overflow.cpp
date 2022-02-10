// https://www.youtube.com/watch?v=GQp1zzTwrIg&t=3718s&ab_channel=CodeBeauty
// this class
// data type overflow

#include <iostream>
using namespace std;

int main()
{
    int intMax = INT32_MAX;
    cout << intMax << endl;
    // 2147483647
    // this is the max number of int32

    // an example of int32 overflow
    cout << intMax + 1 << endl;
    // -2147483648
    // it returns to the back
}