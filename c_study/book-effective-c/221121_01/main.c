#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // puts returns EOF if something went wrong
    if (puts("Hello, world") == EOF)
    {
        return EXIT_FAILURE;
    }
    if (printf("%s\n", "Hello world again!") < 0){
        // printf will return the number of characters printed if everything went ok
        // otherwise it will return a negative number
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
// EXIT_SUCCESS and EXIT_FAILURE are macros from stdlib
// macros are defined in the preprocessor
