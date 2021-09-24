# https://leetcode.com/problems/integer-to-roman/

#%%
class Solution:
    def intToRoman(self, num: int) -> str:
        list_chars = []
        num_thousand = num // 1000
        rest_thousand = num % 1000
        list_chars += ["M"] * num_thousand

        num_hundred = rest_thousand // 100
        rest_hundred = rest_thousand % 100

        if 1 <= num_hundred <= 3:
            list_chars += ["C"] * num_hundred
        elif num_hundred == 4:
            list_chars += ["CD"]
        elif 5 <= num_hundred <= 8:
            list_chars += ["D"] + ["C"] * (num_hundred - 5)
        elif num_hundred == 9:
            list_chars += ["CM"]

        num_ten = rest_hundred // 10
        rest_ten = rest_hundred % 10

        if 1 <= num_ten <= 3:
            list_chars += ["X"] * num_ten
        elif num_ten == 4:
            list_chars += ["XL"]
        elif 5 <= num_ten <= 8:
            list_chars += ["L"] + ["X"] * (num_ten - 5)
        elif num_ten == 9:
            list_chars += ["XC"]        

        if 1 <= rest_ten <= 3:
            list_chars += ["I"] * rest_ten
        elif rest_ten == 4:
            list_chars += ["IV"]
        elif 5 <= rest_ten <= 8:
            list_chars += ["V"] + ["I"] * (rest_ten - 5)
        elif rest_ten == 9:
            list_chars += ["IX"]

        return "".join(list_chars)

#%%
num = 200
solution = Solution()
solution.intToRoman(num) == "CC"
#%%
num = 100
solution = Solution()
solution.intToRoman(num) == "C"
#%%
num = 3800
solution = Solution()
solution.intToRoman(num) == "MMMDCCC"
#%%
num = 3876
solution = Solution()
solution.intToRoman(num) == "MMMDCCCLXXVI"
#%%
num = 3000
solution = Solution()
solution.intToRoman(num) == "MMM"
#%%
num = 1
solution = Solution()
solution.intToRoman(num) == "I"
#%%
num = 2
solution = Solution()
solution.intToRoman(num) == "II"
#%%
num = 5
solution = Solution()
solution.intToRoman(num) == "V"
#%%
num = 3
solution = Solution()
solution.intToRoman(num) == "III"
#%%
num = 4
solution = Solution()
solution.intToRoman(num) == "IV"
#%%
num = 58
solution = Solution()
solution.intToRoman(num) == "LVIII"
#%%
num = 1994
solution = Solution()
solution.intToRoman(num) == "MCMXCIV"
# %%

# %%
