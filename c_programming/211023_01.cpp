
// just an experiment from the site:
// https://www.educative.io/edpresso/pass-by-value-vs-pass-by-reference
#include <iostream>

using namespace std;

void incrementCount(int count)//pass by value
{
  count=count+1;//increments the value of count inside the function
}
int main()
{
  int count=0;// initialze the variable count
  int result=0;//  initialze the variable result
  incrementCount(count);//call increment function
  cout<<"Pass by value\n";
  cout<<"Count:";
  cout<<count;//prints the value of count after the function call
  return 0;
}