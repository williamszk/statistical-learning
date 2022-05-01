// https://www.youtube.com/watch?v=jEK3J_Ezb_E&ab_channel=BogdanBudaca

#include <stdio.h>

typedef struct alphabet
{
    int A;
    int B;
    int C;
    int D;
    int E;
    int F;
    int G;
    int H;
    int I;
    int J;
    int K;
    int L;
    int M;
    int N;
    int O;
    int P;
    int Q;
    int R;
    int S;
    int T;
    int U;
    int V;
    int W;
    int X;
    int Y;
    int Z;
} Alphabet;

void main()
{

    Alphabet alphabet = {
        .A = 0,
        .B = 1,
        .C = 2,
        .D = 3,
        .E = 4,
        .F = 5,
        .G = 6,
        .H = 7,
        .I = 8,
        .J = 9,
        .K = 10,
        .L = 11,
        .M = 12,
        .N = 13,
        .O = 14,
        .P = 15,
        .Q = 16,
        .R = 17,
        .S = 18,
        .T = 19,
        .U = 20,
        .V = 21,
        .W = 22,
        .X = 23,
        .Y = 24,
        .Z = 25,
    };

    // printf("A: %d\n", alphabet.A);

    // https://en.wikipedia.org/wiki/Caesar_cipher
    char plainText[] = "I AM JULIUS CAESAR";
    // what is the cipher text?


    int shift = 1;

    int shift2 = 3;
    char plainText2[] = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG";
    char expectedCipherText2[] = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD";

    // https://www.dcode.fr/
    // https://www.dcode.fr/caesar-cipher

    // we could use the ASCII enconding to do the Caesar Cipher
    // or we could build the dictionary by hand where A -> 0, B -> 1, ... Z -> 26
    // we'll go with the later first

    // Maybe we can use ASCII directly we just need to subtract the necessary values...
}
