#include <stdio.h>
#include <stdlib.h>

void flush_input(){
    int ch;
    while (
        (ch = getchar()) != '\n'
        &&
        ch != EOF
    );
    // I dint understood how this function works

}

void get_input_with_fgets(){
    char first_name[10];
    char last_name[10];

    printf("Enter your first name: ");
    fgets(first_name, 10, stdin);
    flush_input();
    // fflush(stdin);
    printf("Enter your last name: ");
    fgets(last_name, 10, stdin);
    flush_input();
    // fflush(stdin);
    printf("Hi, %s %s!\n", first_name, last_name);
}


int main(){

    get_input_with_fgets();
    // buffer: storage area that contains data waiting to be processed
    // 

    // how to empty the buffer?
    // we use the funcion flush_input() to empty the buffer
    // after a fgets()


    return 0;
}




