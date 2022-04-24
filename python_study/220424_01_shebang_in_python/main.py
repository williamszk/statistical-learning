#!/root/statistical-learning/python_study/220424_01_shebang_in_python/.venv/bin/python3

# this is one python kernel, inside a virtual environment
# it does not have numpy installed, let's experiment with using numpy inside the script
# /root/statistical-learning/python_study/220424_01_shebang_in_python/.venv/bin/python3

""" This is an experiment with the #! (shebang)


I'm doing an experiment with shebang for a python script.
But with which other languanges can use shebang?
"""


import numpy as np



# we need to make the .py file executable


# Result:
# [Traceback (most recent call last):
#   File "./main.py", line 15, in <module>
#     import numpy as np
# ModuleNotFoundError: No module named 'numpy'

