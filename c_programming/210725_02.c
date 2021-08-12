

#include <stdio.h>
#define SERVICE_CHARGE 15

int calculate_grand_total(int subtotal){
    int grand_total;
    grand_total = subtotal + SERVICE_CHARGE;
    return grand_total;
}

int main(){
    printf("The grand total is: %d.\n", calculate_grand_total(22));
}