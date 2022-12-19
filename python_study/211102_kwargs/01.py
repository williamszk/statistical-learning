
my_dict = {
    "a":1,
    "b":2
}


def my_func(**kwargs):
    print(kwargs)


my_func(**my_dict)

# in **kwargs we pass a dictionary
# when we call the function we pass the dictionary
# with ** to "open" the dicionary
# we could just pass the arguments as key word arguments
