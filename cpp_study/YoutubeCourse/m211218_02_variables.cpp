#include <iostream>
// variables

using namespace std;

int main() {

     

     
     // an example of how to input values in the program
     cout << "What is your annual salary?\n";
     
     // float annualSalary;
     // cin >> annualSalary;
     
     float annualSalary = 50000.99;

     float monthlySalary = annualSalary / 12;

     cout << "Your monthly salary is: $" << monthlySalary << endl;

     cout << "In 10 years will earn: $" << annualSalary*10 << endl;
     // we can write expression after the << 
     // can we include any type of data? boolean, float and int?

     // in c++ we can include an array as an argument of a function?

     char myCharacter = 'a';

}