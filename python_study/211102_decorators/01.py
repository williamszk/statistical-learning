#%%

from typing import final


def goodbye_decorator(func):
    
    def func_output(x):
        func(x)
        print("Goodbye!")

    return func_output


# higher order function
# decotorator

@goodbye_decorator
def func1(x):
    print(x)

#%%

func1_test = goodbye_decorator(func1)


def func2(x):
    print(x+", Bob")



func1("Hello")

func2("Hello")

func1_test("Hello")

#%%
# create a higher order function for derivative


def func_linear(x: float) -> float:
    y = x*2
    return y


func_linear(2)

#%%

def derivative(func):

    def func_return(x, delta=0.00001):
        return (func(x+delta) - func(x))/delta
    
    return func_return


func_deriv = derivative(func_linear)

func_deriv(1)
func_deriv(2)


#%%

def derivative(func, delta=0.0001):

    def func_return(x, delta=delta):
        return (func(x+delta) - func(x))/delta
    
    return func_return

@derivative
def func_linear(x: float) -> float:
    y = x*2
    return y

#%%
func_linear(2)
func_linear(3)
func_linear(4)


# %%

def execute_complete_reservation(test_case,insurance_mode):
    def inner_function(self,*args,**kwargs):
        self.test_create_qsf_query()
        test_case(self,*args,**kwargs)
        self.test_select_room_option()
        if insurance_mode:
            self.test_accept_insurance_crosseling()
        else:
            self.test_decline_insurance_crosseling()
        self.test_configure_pax_details()
        self.test_configure_payer_details

    return inner_function

#%%

def decorator_factory(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):
            funny_stuff()
            something_with_argument(argument)
            result = function(*args, **kwargs)
            more_funny_stuff()
            return result
        return wrapper
    return decorator

#%%

def decorator_factory(argument="Goodbye!"):
    def final_message_decorator(func):

        def func_output(*args, **kwargs):
            func(*args, **kwargs)
            print(argument)
        
        return func_output  

    return final_message_decorator


@decorator_factory(argument="Goodbye!")
def hello_func(name):
    print(f"Hello, {name}!")

hello_func("Prinzecinha")
hello_func("Amorzinha")


@decorator_factory(argument="Sayounara!")
def ohayou_func(name):
    print(f"Ohayou, {name}!")

ohayou_func("Prinzecinha")
ohayou_func("Amorzinha")


#%%

def final_message_decorator(func):

    def func_output(*args, **kwargs):
        output = func(*args, **kwargs)
        print("Goodbye!")
    
    return func_output


@final_message_decorator
def hello_func(name):
    print(f"Hello, {name}!")


hello_func("Bob")
