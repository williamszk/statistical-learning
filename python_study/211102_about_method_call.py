

class MyClass:
    def __init__(self, a) -> None:
        self.a = a

    def my_method_01(self, b):
        return self.a + b


my_instance = MyClass(10)

my_instance.a


my_instance.my_method_01(20)


MyClass.my_method_01(my_instance, 20)

my_function = MyClass.my_method_01

my_function(my_instance, 20)

# we can use methods using the . (dot) notation or we can we can use 
# them as usual functions

