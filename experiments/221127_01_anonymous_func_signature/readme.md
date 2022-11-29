The idea: We need to pass some variables to a function. One way is to define the function in an outer scope and then pass the relevant parameters.
Another is to build an anonymous function inside the other function, and then we don’t have to pass all parameters to the function. This could save space in the signature of the function.
Another way to make the signature of the function smaller is to use some kind of struct, dictionary or object.
If we are facing a situation where we are passing the same set of parameters to many functions we could bundle this set of parameters inside a class/struct/object. And/or make those functions as methods.
