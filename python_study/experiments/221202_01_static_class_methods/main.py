

class Base:
    @staticmethod
    def foo():
        print("This is foo from Base")

class Child(Base):
    def foo(self):
        print("This is foo from Child")

    @classmethod 
    def bar(cls):
        print("This is bar from Child")

def main():
    child = Child()
    child.foo()

    Child.bar()

if __name__ == "__main__":
    main()