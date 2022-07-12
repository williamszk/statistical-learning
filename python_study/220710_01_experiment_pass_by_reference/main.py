from animal import Animal


def main() -> None:

    doggy: Animal = Animal("Doggy", 10)
    print(f"Calling from outside: \t\t\t\t{hex(id(doggy))}")
    handle_animal(doggy)
    doggy.handle_from_inside()

    # Calling from outside:                           0x7f24b7e42970
    # Calling from inside handle_animal():            0x7f24b7e42970
    # Calling from inside handle_from_inside:         0x7f24b7e42970


def handle_animal(animal: Animal) -> None:
    print(f"Calling from inside handle_animal(): \t\t{hex(id(animal))}");


if __name__ == "__main__":
    main()

