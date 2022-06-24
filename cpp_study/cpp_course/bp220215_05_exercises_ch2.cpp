/* Book: C++ Primer
 * Stanley Lipman, Josée Lojoie, Barbara Moo
 * */

#include <iostream>
#include <string>
#include <cmath>

void messageCheck(bool answer, std::string id)
{
	if (answer)
	{
		std::cout << id << " prediction correct" << std::endl;
	}
	else
	{
		std::cout << id << " prediction wrong" << std::endl;
	}
}

int main()
{

	unsigned int u = 10, u2 = 42;
	messageCheck(u2 - u == 32, "01");
	messageCheck(u - u2 == pow(2,32) - 32, "02");

	int i = 42, i2 = 42;
	messageCheck(i2 - i == 0, "03");
	messageCheck(i - i2 == 0, "04");

	messageCheck(i - u == 32, "05");
	messageCheck(u - i == pow(2,32) - 32, "06");

}

// stoped at section 2.1.3 Literals p 67