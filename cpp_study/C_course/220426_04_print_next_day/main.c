
// https://www.udemy.com/course/c-programming-for-beginners-programming-in-c/learn/lecture/24168574#questions

#include <stdio.h>


typedef struct Date {
	int day;
	int month;
	int year;
} Date;

Date printNextDay(Date date)
{
	Date nextDay;
	if (date.month == 1 || date.month == 3 || date.month == 5 ||
		date.month == 7 || date.month == 8 || date.month == 10 ||
		date.month == 12)
	{
		if (date.day == 31)
		{
			nextDay.day = 1;
			if (date.month == 12)
			{
				nextDay.month = 1;
				nextDay.year = date.year + 1;
		
			}
			else
				nextDay.month = date.month + 1;
		}	
		else
 			nextDay.day = date.day + 1;
	
	}
	else if (date.month == 4 || date.month == 6 || date.month == 9 ||
			 date.month == 11)
	{
		if (date.day == 30)
		{
			nextDay.day = 1;	
			nextDay.month = date.month + 1;
		}		
		else
			nextDay.day = date.day + 1;
	}
	else if (date.month == 2)
	{
		if (date.day == 28)
		{
			nextDay.day = 1;
			nextDay.month = 3;	
		}
		else
		{
			nextDay.day = date.day + 1;	
		}
	}

	if (date.month != 12)
		nextDay.year = date.year;
	
	return nextDay;
}	


void main()
{
	Date date;
	date.day = 28;
	date.month = 2;
	date.year = 1990;
	Date nextDay = printNextDay(date);
	printf("Year: %d, Month: %d, Day: %d\n", nextDay.year, nextDay.month, nextDay.day);


	// this is how we assign values to a struct
	Date lastDate = {31, 12, 2010};
	nextDay = printNextDay(lastDate);
	printf("Year: %d, Month: %d, Day: %d\n", nextDay.year, nextDay.month, nextDay.day);
}

