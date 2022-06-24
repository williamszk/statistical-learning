"""
This program receives an integer and returns the divisors of this integer.


https://www.cyberciti.biz/faq/python-command-line-arguments-argv-example/

"""

import sys

# print(sys.argv)
# ['find_divisors.py', '10']

def main():

    if len(sys.argv) > 2:
        raise Exception("Incorrect number of arguments. Include just one argument which should be an integer number.")

    number = sys.argv[1]
    number = int(number)
    print("\n===============================")
    print(f"   The divisors of {number} are:")
    for divisor in range(1, number):
        if number % divisor == 0:
            print(f"       {divisor}")

    print("===============================")



if __name__ == "__main__":
    main()

