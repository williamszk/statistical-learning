/* Build a calculator that can receive the base and the power
and calculate the base ^ power
for any power and base
*/

#include <stdio.h>

void main()
{
    int base = 0;
    int power = 0;
    int result = 1;

    printf("Write a number for the base: ");
    scanf("%d", &base);

    printf("Write a number for the power: ");
    scanf("%d", &power);

    for (int i = 0; i < power; i++)
    {
        result *= base;
    }

    printf("Result: %d^%d = %d\n", base, power, result);
}

// C:\Users\william.suzuki\Documents\statistical-learning\cpp_study\C_course\220322_07_generic_power_calculator>.\a.exe
// Write a number for the base: 2
// Write a number for the power: 3
// Result: 2^3 = 8