/*
 * https://www.udemy.com/course/java-the-complete-java-developer-course/learn/quiz/4426604#overview
 */

#include <iostream>

void printMegaBytesAndKiloBytes(int kiloBytes)
{
    const int CONVERTER_BYTES = 1024;

    if (kiloBytes < 0)
    {
        std::cout << "Invalid Value" << std::endl;
    }
    else
    {
        int megaBytes = kiloBytes / CONVERTER_BYTES;
        int kiloBytesRest = kiloBytes % CONVERTER_BYTES;
        std::cout << kiloBytes << " KB = " << megaBytes << " MB and " << kiloBytesRest << " KB" << std::endl;
    }
}

int main()
{
    printMegaBytesAndKiloBytes(2500);
    printMegaBytesAndKiloBytes(-1024);
    printMegaBytesAndKiloBytes(5000);
    return 0;
}
