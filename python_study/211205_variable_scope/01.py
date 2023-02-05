"""
We want to test how Python deals with scope and how variables can observe inside or
outside of it self.
"""

import module_211205_01 as mm

print(__name__)
print(mm.__name__)




mm.count1 = 10
mm.count2 = 20

mm.my_func_logger()

# def my_func_logger():
#     total_count = count1 + count2
#     print(total_count)

# print(total_count)

# mm.my_func_logger()
# suprisingly the function can see the variables
# what if we change the order when the function was created?
# it also works
# what if the function is defined inside a module that is not in the same script?
# when we define the function in another module, the function can't be run
# 

# if we call the function before the internal variables are defined
# the function will not work

# in this sense python functions can observe outside variables
# when they are in the same scope


# another interesting thing to notice is that Python and JavaScript will run the script
# even if there are some error in the middle of the program
# in compiled programming languanges would this happen?
















