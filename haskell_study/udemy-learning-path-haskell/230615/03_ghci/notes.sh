
# to start the haskell REPL
stack ghci

# We should have a stack.yaml file in the same directory as we start the REPL

# [ inside ghci ]
x = 5
y = 6
x
y
x + y

# to call shell commands from ghci
:!ls
:!ls
:!mkdir TEMP
:!cd TEMP
:!ls
:!cd ..
:!ls
:!rm -rf TEMP

:type x
:type y

x + y
# `it` is the most recent value evaluated
it 

:type Num
:kind Num

:info it
:info Num





















