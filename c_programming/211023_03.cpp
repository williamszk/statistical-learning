// https://www.educative.io/edpresso/pass-by-value-vs-pass-by-reference
#include <iostream>


void incrementCount(int & count)//& to pass by reference
{
  count=count+1;//increments the value of count
}
int main()
{
  int count=0;//initialize the variable count
  int result=0;// initialize the variable result
  incrementCount(count);//increment value of count
  std::cout<<"Pass by Reference\n";
  std::cout<<"Count:";
  std::cout<<count;//prints count after the function call
  return 0;
}