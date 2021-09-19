# https://leetcode.com/problems/reverse-integer/

#%%
class Solution:
    def reverse(self, x: int) -> int:
        MAX_RANGE = [-2**31, 2**31 - 1]
        str_x = str(x)
        if str_x[0] == "-":
            str_x_unsigned = str_x[1:]
        else:
            str_x_unsigned = str_x
        
        list_str = [x for x in str_x_unsigned]

        list_str.reverse()

        reversed_str = "".join(list_str)
        
        if str_x[0] == "-":
            reversed_str = "-"+reversed_str
        
        converted_int = int(reversed_str)

        if converted_int < MAX_RANGE[0]:
            converted_int = 0
        elif converted_int > MAX_RANGE[1]:
            converted_int = 0

        return converted_int

    

#%%
x = 10982
solution = Solution()
solution.reverse(x) == 28901
# %%
x = 99999999999
solution = Solution()
solution.reverse(x) == 0
# %%
x = -123
solution = Solution()
solution.reverse(x) == -321

# %%
x = 120
solution = Solution()
solution.reverse(x) == 21
# %%
x = 0
solution = Solution()
solution.reverse(x) == 0
# %%
