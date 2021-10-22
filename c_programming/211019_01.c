#include <stdio.h>

#define STRLEN 5

// int read_line(char s[], int maxlen){
//     int len_s;
//     fgets(s, maxlen, stdin);
//     len_s = strlen(s)
//     if (s[len_s - 1] == '\n') {

//     }

//     return len_s;
// }

int readln(char s[], int maxlen) {
    char ch;
    int i;
    int chars_remain;
    i = 0;
    chars_remain = 1;
    while (chars_remain) {
        ch = getchar();
        if ((ch == '\n') || (ch == EOF)){
            chars_remain = 0;
        } else if (i < maxlen - 1) {
            s[i] = ch;
            i++;
        }
    }
    s[i] = '\0';
    return i;
}


void main(){


}

