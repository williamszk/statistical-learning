#include <stdio.h>

int *answer()
{
    int x = 42;
    return &x;
}

int main()
{

    return 0;
}

// https://stackoverflow.com/questions/8743411/return-address-of-local-variable-in-c
// You should always be careful when returning addresses to local variables;
// as a rule, you could say that you never should.
// static variables are a whole different case though, which is being discussed in this thread.

// https://stackoverflow.com/questions/453696/is-returning-a-pointer-to-a-static-local-variable-safe
//

