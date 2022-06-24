
# this is called class constructor
class Shark:

    animal_type = "fish"
    location = "ocean"
    followers = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swim(self):
        print(f"{self.name} is swimming.")

    def be_awesome(self):
        print(f"{self.name} is being awesome.")


# sammy = Shark()
# sammy.swim()
# sammy.be_awesome()
# dot operator
# dot operator will get an attribute, tThe sharkhis attribute can be a value or a function
# if it is a function we can use () to call it

def main():
    sammy = Shark("Sammy", 5)
    sammy.swim()
    stevie = Shark("Stevie", 6)
    stevie.be_awesome()
    print(stevie.age)
    

    new_shark = Shark("Shakira", 10)
    print(new_shark.animal_type)
    print(new_shark.location)
    print(new_shark.followers)



if __name__ == "__main__":
    main()










