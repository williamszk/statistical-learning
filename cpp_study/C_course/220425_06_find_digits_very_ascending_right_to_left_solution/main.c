// C:\Users\william.suzuki\Documents\statistical-learning\cpp_study\C_course\220425_05_find_digits_very_ascending_or_not

#include <stdio.h>


// When calling for the firs time this function
// use prevAnsw = 2
// so that the program will know that it is the first time
// to run the recursion.
int ascenDescOtherwise(uint32_t num, int prevAnsw)
{
	unsigned int leftDigit;
    unsigned int rightDigit;

	if (num < 100)
	{
		leftDigit = num / 10;
		rightDigit = num % 10;

		if (leftDigit > rightDigit)
			return -1;
		else if (rightDigit > leftDigit)
			return 1;
	}

	if (prevAnsw == 2)
	{ // this means that we are at the beginning of the recursion
		
		leftDigit = num % 10;
		rightDigit = (num % 100) / 10;	

		num /= 10;	
			
		if (leftDigit > rightDigit)
			return ascenDescOtherwise(num, -1);
	    else if (leftDigit < rightDigit)
			return ascenDescOtherwise(num, 1);
	}


	// unsigned int currDigit = num % 10;
	// unsigned int prevDigit = (num % 100) / 10;	

	// num = num / 10;


	// return ascenDescOtherwise(num, )	
}




void main()
{
	// if very asceding -> 1
	// if very descing -> -1
	// otherwise -> 0
	
	
}

