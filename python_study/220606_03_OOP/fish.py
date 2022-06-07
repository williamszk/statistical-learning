class Fish:
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


class Trout(Fish):
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False, water="freshwater"):
        self.water = water
        super().__init__(first_name, last_name, skeleton, eyelids)
    # here we'll just accept the methods and attributes of the
    # parent class
    # but a child class can overrite or change classes
    # that were inherited


class Clownfish(Fish):
    # this child class is using the __init__ method from the parent class
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")


class Shark(Fish):
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")


class Coral:

    def community(self):
        print("Coral lives in a community.")


class Anemone:

    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


class CoralReef(Coral, Anemone):
    pass


def main():
    terry = Trout("Terry")
    print(terry.first_name + " " + terry.last_name)
    print(terry.skeleton)
    print(terry.eyelids)
    print(terry.water)
    terry.swim()
    terry.swim_backwards()

    casey = Clownfish("Casey")
    print(casey.first_name + " " + casey.last_name)
    casey.swim()
    casey.live_with_anemone()

    sammy = Shark("Sammy")
    print(sammy.first_name + " " + sammy.last_name)
    sammy.swim()
    sammy.swim_backwards()
    print(sammy.eyelids)
    print(sammy.skeleton)

    great_barrier = CoralReef()
    great_barrier.community()
    great_barrier.protect_clownfish()



if __name__ == "__main__":
    main()
