#include <stdio.h>
#define START_CHAR 65
#define MODULE 26

typedef struct text {
    char text[500];
} String;

String encryptCaesarCipher(char *plainText, int shift)
{
    String cipherText;
    int i;

    for (i = 0; plainText[i] != '\0'; i++)
    {
        if (plainText[i] == ' ')
            cipherText.text[i] = ' ';
        else
        {
            int newLetter = ((plainText[i] - shift - START_CHAR + MODULE) % MODULE) + START_CHAR;
            cipherText.text[i] = newLetter;
        }
    }
    cipherText.text[i] = '\0';

    return cipherText;
}

String decipherCaesarCipher(char *cipherText, int shift)
{
    String decipheredText;
    int i;

    for (i = 0; cipherText[i] != '\0'; i++)
    {
        if (cipherText[i] == ' ')
            decipheredText.text[i] = ' ';
        else 
        {
            int newLetter = ((cipherText[i] + shift - START_CHAR + MODULE) % MODULE) + START_CHAR;
            decipheredText.text[i] = newLetter;
        }
    }
    decipheredText.text[i] = '\0';

    return decipheredText;
}

void main()
{
    // printf("%c\n", 'C');
    // printf("%c\n", 'C'-3);


    char plainText2[] = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG";
    char expectedCipherText2[] = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD";
    String resultCipherText = encryptCaesarCipher(plainText2, 3);
    String descipheredTextResult = decipherCaesarCipher(resultCipherText.text, 3);

    printf("Plain Text: %s\n", plainText2);
    printf("Cipher Text: %s\n", resultCipherText.text);
    printf("Deciphered Text: %s\n", descipheredTextResult.text);

    printf("=====================\n");

    char plainText3[] = "I AM JULIUS CAESAR";
    String resultCipherText2 = encryptCaesarCipher(plainText3, 3);
    String descipheredTextResult2 = decipherCaesarCipher(resultCipherText2.text, 3);

    printf("Plain Text: %s\n", plainText3);
    printf("Cipher Text: %s\n", resultCipherText2.text);
    printf("Deciphered Text: %s\n", descipheredTextResult2.text);




}