

union info
{
    char firstName[20];
    int age;
};

typedef union info2_s
{
    char firstName[20];
    int age;
} info2_t;

typedef union Number {
    int numInt;
    float numFloat;
} Number;

Number sum(Number a, Number b){
    Number answer;    
    answer.numFloat = a.numFloat + b.numFloat;;
    answer.numInt = a.numInt + b.numInt;

    return answer;
}

int main()
{


}