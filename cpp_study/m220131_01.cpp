/* Do a regex for e-mail and password.
 * The e-mail should have and @ sign, characters before and after
 * It should have a [].[] characters.
 * For the password it should have capital letters, numbers and
 * some special symbol.
 *
 * https://www.youtube.com/watch?v=9K4N6MO_R1Y&ab_channel=DerekBanas
 * */

#include <iostream>
#include <regex>

void printMatches(std::string myString, std::regex myRegular)
{
    std::smatch myMatches;
    std::cout << std::boolalpha;
    while(std::regex_search(myString, myMatches, myRegular))
    {
        std::cout << "Is there a match: " << myMatches.ready() << std::endl;

    }
}


int main()
{
    std::string myString = "The ape was at the apex.";
    std::regex myRegular ("(ape[^ ]?)");




    return 0;
}



// this is video is too advanced for me right now...
















