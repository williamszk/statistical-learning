"""Experiment with class variables
Hypothesis: We create n instance, if we change the class variable of one of them
we change all this class variable for all instances"""

class MyClass:
    a_class_variable = 1

def main():
    instances = []

    for i in range(5):
        instances.append((i, MyClass))

    for i in range(5):
        print("A. ", instances[i][1].a_class_variable)

    # change the first instance, change its class variable value
    instances[0][1].a_class_variable = 2

    for i in range(5):
        print("B. ", instances[i][1].a_class_variable)

# We can see that with class variables, if we change it inside one instance
# we'll change them in all instances

if __name__ == "__main__":
    main()

# A.  1
# A.  1
# A.  1
# A.  1
# A.  1
# B.  2
# B.  2
# B.  2
# B.  2
# B.  2