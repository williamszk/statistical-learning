"""This is an experiment creating a closure.
"""

from typing import Callable


def main():
    bob_amount_saved = 1000
    bob_spend = bank_account(bob_amount_saved)
    print(f"{type(bob_spend) = }")
    print(f"Bob starts with: {bob_amount_saved}")
    print(f"Bob spent 100, he has: {bob_spend(100)}")
    print(f"Bob spent 300, he has: {bob_spend(300)}")

    mary_amount_saved = 8000
    mary_spend = bank_account(mary_amount_saved)
    print(f"Mary starts with: {mary_amount_saved}")
    print(f"Mary spent 100, she has: {mary_spend(100)}")
    print(f"Mary spent 900, she has: {mary_spend(900)}")


def bank_account(amount_saved) -> Callable:

    def person_spend(amount_spent) -> None:
        nonlocal amount_saved
        amount_saved -= amount_spent
        return amount_saved

    return person_spend


if __name__ == "__main__":
    main()
