/*
Notes on Data Structures and Algorithms in c++
Adam Drozdek
*/

#include <iostream>
#include <cstring>

class myClass {
    public:
        myClass(char *myString = "", int myInt = 0, double myDouble = 1){
            strcpy(dataMember1, myString);
            dataMember2 = myInt;
            dataMember3 = myDouble;
        }
        
        void memberFunction1() {
            std::cout << dataMember1 << " " << dataMember2 << " " 
                << dataMember3 << std::endl; 
        }
        
        void memberFunction2(int i, char *s = "unknown") {
           dataMember2 = i;
           std::cout << i << " received from " << s << std::endl;
        }
    protected:
        char dataMember1[20];
        int dataMember2;
        double dataMember3;
};










