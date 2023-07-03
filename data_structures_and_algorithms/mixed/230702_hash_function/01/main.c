// https://www.youtube.com/watch?v=xrLNoduAZfM&ab_channel=d8dataworks
// [x] for the next step we can improve this code
// [ ] use more magic values

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

// build hash function, receive a string and return an uint64_t
uint64_t hash_function(char *str, int length){
    // uint8
    // int length = 10;
    int magic = 87;
    char c1;
    // char c2;
    uint64_t hash = 0;
    for (int i = 0; i < length; i++)
    {
        c1 = str[i];
        if (i == 0)
            hash = c1;
        else
            hash = hash * magic + c1;
    }

    return hash;
}

// build hash function, receive a string and return an uint64_t
uint64_t hash_function_2(char *str, int length){
    // uint8
    // int length = 10;
    int magic[] = {87, 99, 17, 9};
    char c1;
    // char c2;
    uint64_t hash = 0;
    for (int i = 0; i < length; i++)
    {
        c1 = str[i];
        if (i == 0)
            hash = c1;
        else
            hash = hash * magic + c1;
    }

    return hash;
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

    uint64_t hash = hash_function(my_string_2, 10);
    printf("hash: %lu\n", hash);

    return 0;
}

// hash: 12442553457515755812







