# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# %%
from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            list_possible_letters = []
        else:
            dict_number_letters = {
                "2":["a","b","c"],
                "3":["d","e","f"],
                "4":["g","h","i"],
                "5":["j","k","l"],
                "6":["m","n","o"],
                "7":["p","q","r","s"],
                "8":["t","u","v"],
                "9":["w","x","y","z"]
            }
            list_letters = []

            for number in digits:
                list_letters.append(dict_number_letters.get(number))

            list_possible_letters = ["".join(x) for x in product(*list_letters)]

        return list_possible_letters

# %%
digits = "23"
expected_answer = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
solution = Solution()
list_letter_combination = solution.letterCombinations(digits)
all([x in expected_answer for x in list_letter_combination])
# %%
digits = ""
expected_answer = []
solution = Solution()
list_letter_combination = solution.letterCombinations(digits)
all([x in expected_answer for x in list_letter_combination])
# %%
digits = "2"
expected_answer = ["a","b","c"]
solution = Solution()
list_letter_combination = solution.letterCombinations(digits)
all([x in expected_answer for x in list_letter_combination])
# %%
