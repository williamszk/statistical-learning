// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168564#questions

#include <stdio.h>

typedef int grade;

struct date {
	int day;
	int month;
	int year;
};


typedef struct date2 {
	int day;
	int month;
	int year;
} Date;


void printDate(Date dt)
{
	printf("Year=%d, Month=%d, Year=%d\n", dt.year, dt.month, dt.day);
}

Date inputDate()
{
	Date dt;
	
	printf("Enter the day: ");	
	scanf("%d", &dt.day);

	printf("Enter the month: ");
	scanf("%d", &dt.month);

	printf("Enter the year: ");
	scanf("%d", &dt.year);

	return dt;
}


void main()
{
	// for this case it is interesting to use a named type for int
	// because we give meaning to the number
	// it is for naming and meaning's sake that we define int like this
	grade math;
	grade physics;
	// but in the case of structs it is naming and meaning
	// but also structure, it is easier to manipulate data
	// that is in a dictionary, hash-map like structure
	
	// how to declare a struct?
	struct date mySpecialDate;

	Date myAnotSpecialDate;
	
	myAnotSpecialDate.year = 2020;
	myAnotSpecialDate.month = 5;
	myAnotSpecialDate.day = 10;

	printDate(myAnotSpecialDate);


	Date myDate2 = inputDate();
	printDate(myDate2);

}


