# Python Object-Oriented Programming


class Employee:    
    # down here are class variabls
    raise_amount = 1.04
    
    # variable to keep control of the number of employees
    num_emp = 0

    def __init__(self, first, last, pay) -> None:
        # down here are instance variables
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + "." + last + "@company.com"

        # increase the num of employees when we instantiate new employees
        Employee.num_emp += 1
        # We use the class name "Employee" here instead of self
        # because we want to make the num_emp equal to all instances of Employee
        # this is how we get it



    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # a class method uses the class itself as the first argument
    # of the function
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # operation overloading
    # use + with a custom class
    # dunder methods
    # special methods
    def __repr__(self) -> str:
        """
        For __repr__ try to output something that can easily
        be copy pasted to reproduce the object. 
        repr is meant to be used by programmers, not users.

        Employee('Corey','Schafer','50000')
        """
        return f"Employee('{self.first}','{self.last}','{self.pay}')"

    def __str__(self) -> str:
        """
        In __str__ we output a string that can be a nice user friendly
        representation of the object.

        - Employee:
        - Name: Corey Schafer
        - Email: Corey.Schafer@company.com
        """
        return (
            "- Employee:\n"
            f"- Name: {self.fullname()}\n"
            f"- Email: {self.email}"
        )
    
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    # the @property decorator will make the method act like an attribute
    # in the senes that we don't need to use () to call it
    @property
    def email(self):
        return self.first + "." + self.last + "@company.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        """
        # how to make this allowed?
        emp_1.fullname = "Corey Schafer"
        """
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        """
        del emp_1.fullname
        """
        print("Delete name.")
        self.first = None
        self.last = None




def main():
    # attributes and methods
    # methods -> function
    # attribute -> data
    print(f"{Employee.num_emp = }")
    emp_1 = Employee("Corey", "Schafer", 50000)
    print(f"{Employee.num_emp = }")
    emp_2 = Employee("John", "McCarthy", 100000)
    print(f"{Employee.num_emp = }")

    # print(emp_1.fullname())
    # print(emp_2.fullname())

    # print(Employee.fullname(emp_1))

    print("Test with changing attribute with apply_raise()")
    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)

    # to access the namespace of an instance
    # is to find out their attribute values
    print(f"Find name spase of instance:\n {emp_1.__dict__ = }")
    # notice that the namespace using __dict__ does
    # not contain the raise_amount which is a class variable
    print("")
    print(f"{Employee.__dict__ = }")
    # In the class namespace we can find the class variable
    # raise_amount

    # an experiment with the classmethod
    emp_1 = Employee("Corey", "Schafer", 50000)
    emp_2 = Employee("John", "McCarthy", 100000)
    print(emp_1.raise_amount)
    # this will set set the raise amount to the whole class
    Employee.set_raise_amount(1.10)
    print(emp_2.raise_amount)

    print(emp_1)
    print(repr(emp_1))

    print(emp_1 + emp_2)

    del emp_1


if __name__ == "__main__":
    main()

# there are things called:
# regular methods
# class methods 
# static methods

# next class
# https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6&ab_channel=CoreySchafer