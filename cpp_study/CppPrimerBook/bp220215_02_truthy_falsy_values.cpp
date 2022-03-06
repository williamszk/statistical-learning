/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */


#include <iostream>

int main()
{

	int i = 42; // this is interpreted as a truthy value
	if (i)
	{
		std::cout << "i is considered truth" << std::endl;
	}

	int j = 0;
	if (j)
	{
		std::cout << "j is considered truth" << std::endl;
	}
	else
	{
		std::cout << "j is considered false" << std::endl;
	}

	return 0;
}