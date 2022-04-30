"""
Build a program that can take any integer and include it into a different 
equivalence class.
This is an exercise to understand the concept of a 
'Complete System of Residues'
"""


def main():

    mod = 7

    complete_system = build_complete_system_residues(mod)

    for a_integer in range(100):

        congru_class = a_integer % mod

        # we use [] instead of .get because there must be a key given
        # that we are using %
        complete_system[congru_class].add(a_integer)

    print(complete_system)


def build_complete_system_residues(mod: int) -> dict[int: set]:
    """ The mod is a number that specifies the module
    of this system.

    If mod = 7 then the system will have 7 values
    0, 1, ..., 6
    Each one represents a set

    Example:
    ```
    mod = 5
    complete_system = {
        0: set([0, 5, 10]),
        1: set([1, 6, 11]),
        2: set([2, 7, 12]),
        3: set([3, 8, 13]),
        4: set([4, 9, 14]),
    }
    ```
    """

    complete_system = {x: set([x]) for x in range(mod)}

    return complete_system


if __name__ == "__main__":
    main()
