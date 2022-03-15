#include <stdio.h>

float calculateEmpWage(float hourlyWage, int totalHours)
{
    return hourlyWage * totalHours;
}

int main()
{
    float hourlyWage = 10.0;
    int totalHours = 120;
    float totalWage = calculateEmpWage(hourlyWage, totalHours);
    printf("hourlyWage = %.2f\n", hourlyWage);
    printf("totalHours = %d\n", totalHours);
    printf("Total wage: %.2f\n", totalWage);
}