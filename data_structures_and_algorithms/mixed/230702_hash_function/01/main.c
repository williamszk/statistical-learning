// https://www.youtube.com/watch?v=xrLNoduAZfM&ab_channel=d8dataworks
#include <stdio.h>
#include <inttypes.h>

void print_str(char *str, int length)
{
    char c;
    for (int i = 0; i < length; i++)
    {
        c = str[i];
        printf("%c", c);
    }
    printf("\n");
}

int main()
{

    // build a string which is an array of chars
    char my_string[] = {'k',
                        'e',
                        'y',
                        ' ',
                        's',
                        't',
                        'r',
                        'i',
                        'n',
                        'g'};

    // this is a more compact way of creating a string in C:
    char my_string_2[] = "key string";
    // in this string there is a special character '\0' a the end

    printf("printing my_string: ");
    print_str(my_string, 10);

    printf("printing my_string_2: ");
    print_str(my_string_2, 10);

    // uint8
    int length = 10;
    int magic = 87;
    char c1;
    // char c2;
    uint64_t hash = 0;
    for (int i = 0; i < length; i++)
    {
        c1 = my_string_2[i];
        if (i == 0)
            hash = c1;
        else
            hash = hash * magic + c1;
    }

    printf("hash: %lu\n", hash);

    return 0;
}

// for the next step we can improve this code
// and use more magic values