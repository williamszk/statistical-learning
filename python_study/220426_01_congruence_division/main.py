"""
This script experiments with some calculations of divisibility 
congruence and finding X in modular arithmentic.
"""

import pandas as pd


def main():
    mod = 4
    numA = 2
    numB = 2

    solution_vals_X = list(range(20))
    # solution_vals_X = [5, 6]

    is_congruent_01 = []
    is_congruent_02 = []

    for x in solution_vals_X:
        is_congruent_inst = is_congruent(numA*x, numB, mod)
        is_congruent_01.append(is_congruent_inst)
        # the second congruent is used to test the case of
        # division by both sides to see if they share the same
        # valid values for X
        is_congruent_02.append(is_congruent(x, 1, mod))

    df_output = pd.DataFrame(
        {"x_value": solution_vals_X,
         f"{numA}x={numB}(mod{mod})": is_congruent_01,
         f"x=1(mod{mod})": is_congruent_02})

    print(df_output)


def is_congruent(numA: int, numB: int, mod: int) -> bool:
    """ This function tells `numA` is congruent to `numB`
    with module as `mod`.

    """
    # we use the defition of congruence
    if (numA - numB) % mod == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

# Some notes in auto formating in Python using autopep8
# autopep8 --in-place main.py
