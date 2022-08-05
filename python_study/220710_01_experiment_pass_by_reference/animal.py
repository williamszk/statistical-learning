class Animal:
    def __init__(self, name: str, size: int) -> None:
        self.name = name 
        self.size = size
    
    def handle_from_inside(self) -> None:
        print(f"Calling from inside handle_from_inside: \t{hex(id(self))}")


