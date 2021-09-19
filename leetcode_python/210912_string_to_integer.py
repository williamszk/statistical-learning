# https://leetcode.com/problems/string-to-integer-atoi/
#%%
import re

class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_RANGE = [-2**31, 2**31 - 1]

        string_transformed = s.strip()

        if string_transformed =="":
            output_int = 0
        
        else:
            if string_transformed[0] in ["-", "+"]:
                signal = string_transformed[0]
                string_transformed = string_transformed[1:]
            else:
                signal = ""
            
            split_string = re.split(r"(\D+)", string_transformed)
            string_transformed = split_string[0]

            if string_transformed == "":
                output_int = 0

            else:
                string_transformed = "".join([signal, string_transformed])
                output_int = int(string_transformed)
                
                if output_int < MAX_RANGE[0]:
                    output_int = MAX_RANGE[0]
                elif output_int > MAX_RANGE[1]:
                    output_int = MAX_RANGE[1]

        return output_int

#%%
s = ""
solution = Solution()
solution.myAtoi(s) == 0

#%%
s = "3.14159"
solution = Solution()
solution.myAtoi(s) == 3
#%%
s = "-91283472332"
solution = Solution()
solution.myAtoi(s) == -2147483648
#%%
s = "words and 987"
solution = Solution()
solution.myAtoi(s) == 0
#%%
s = "words and +987"
solution = Solution()
solution.myAtoi(s) == 0
#%%
s = "words and -987"
solution = Solution()
solution.myAtoi(s) == 0
#%%
s = "4193 with words"
solution = Solution()
solution.myAtoi(s) == 4193

#%%
s = "42"
solution = Solution()
solution.myAtoi(s) == 42

#%%
s = "   -42"
solution = Solution()
solution.myAtoi(s) == -42
#%%
s = "   -42"
s.strip()

#%%
import re
# re.split(pattern, str)
target_string = "99.887d sd9281231ki 9282 "
# split_string = re.split(r"([A-z]|\s)", target_string)
split_string = re.split(r"(\D+)", target_string)
split_string[0]

#%%






