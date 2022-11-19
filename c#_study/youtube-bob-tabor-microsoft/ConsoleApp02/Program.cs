using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp02
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World");

            int x;
            int y;

            Console.Write("What is your first name? ");
            string firstName = Console.ReadLine();


            Console.Write("What is your last name? ");
            string lastName = Console.ReadLine();

            Console.WriteLine("Hi, " + firstName + " " + lastName + ". How are you doing?");
            Console.ReadLine();
            



        }
    }
}
