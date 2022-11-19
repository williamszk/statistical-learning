using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp03_Decisions
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bob's big giveaway");
            Console.Write("Choose a door: 1, 2 or 3: ");
            string userValue = Console.ReadLine();
            string message;

            if (userValue == "1")
            {
                message = "You won a new car!";

            }
            else if (userValue == "2")
            {
                message = "You won a new boat!";
            }
            else if (userValue == "3")
            {
                message = "You won a new cat!";
            }
            else
            {
                message = "Sorry we didn't understand.";
                message += " You lose.";
            }

            Console.WriteLine(message);
            Console.ReadLine();

            Console.WriteLine("\n\n============================================\n");
            Console.WriteLine("Using Ternary Operator");
            // Ternary operator
            Console.WriteLine("Bob's big giveaway");
            Console.Write("Choose a door: 1, 2 or 3: ");
            userValue = Console.ReadLine();
            message = (userValue == "1") ? "boat" : "strand of lint";
            // string interpolation
            Console.WriteLine("Congratulations! You entered {0}. Therefore, you won a {1}.", userValue, message);


            Console.ReadLine();
        }
    }
}
