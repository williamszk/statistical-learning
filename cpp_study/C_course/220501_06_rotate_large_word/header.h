typedef struct word128
{
    unsigned long A0;
    unsigned long A1;
} Word128;

void printWor128(Word128 arr);
Word128 shiftLeftWord128(Word128 arr, int shift);
Word128 shiftRightWord128(Word128 arr, int shift);
Word128 applyOrWord128(Word128 arrA, Word128 arrB);
Word128 rotateLeftWord128(Word128 arr, int shift);

