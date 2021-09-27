# https://leetcode.com/problems/roman-to-integer/

#%%


class Solution:
    def romanToInt(self, s: str) -> int:
        sum_number = 0
        list_letters = [x for x in s]
        len_list = len(list_letters)
        i = 0
        while True:    
            letter = list_letters[i]

            if i >= len_list - 1:
                next_letter = None
            else:    
                next_letter = list_letters[i+1]

            if letter == "M":
                sum_number += 1000
                i += 1
            elif letter == "D":
                sum_number += 500
                i += 1
            elif letter == "C":
                if next_letter == "D":
                    sum_number += 400
                    i += 2
                elif next_letter == "M":
                    sum_number += 900
                    i += 2
                else:
                    sum_number += 100
                    i += 1
            elif letter == "L":
                sum_number += 50
                i += 1
            elif letter == "X":
                if next_letter == "L":
                    sum_number += 40
                    i += 2
                elif next_letter == "C":
                    sum_number += 90
                    i += 2
                else:
                    sum_number += 10
                    i += 1
            elif letter == "V":
                sum_number += 5
                i += 1
            elif letter == "I":
                if next_letter == "V":
                    sum_number += 4
                    i += 2
                elif next_letter == "X":
                    sum_number += 9
                    i += 2
                else:
                    sum_number += 1
                    i += 1
        
            if i >= len_list:
                break
        
        return sum_number

#%%
s = "XC"
solution = Solution()
solution.romanToInt(s) == 90
#%%
s = "CX"
solution = Solution()
solution.romanToInt(s) == 110
#%%
s = "I"
solution = Solution()
solution.romanToInt(s) == 1
#%%
s = "III"
solution = Solution()
solution.romanToInt(s) == 3
#%%
s = "IX"
solution = Solution()
solution.romanToInt(s) == 9
#%%
s = "LVIII"
solution = Solution()
solution.romanToInt(s) == 58
#%%
s = "MCMXCIV"
solution = Solution()
solution.romanToInt(s) == 1994
# %%

# %%
