# https://leetcode.com/problems/zigzag-conversion/

#%%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        if numRows ==1 :
            list_lists = [range(len_s)]
        else:
            jump_size = 2*numRows - 2
            list_lists = []
            for i in range(numRows):
                list_holder = []
                if i == 0 or i == numRows - 1:
                    j = i
                    counter = 1
                    while j < len_s:
                        list_holder.append(j)
                        j = jump_size*counter + i
                        counter += 1

                else:
                    j = i
                    counter = 1
                    alternate_holder = True
                    while j < len_s:                    
                        list_holder.append(j)
                        if alternate_holder:                        
                            j = jump_size*counter - i
                            alternate_holder = False
                        else:
                            j = jump_size*counter + i
                            counter += 1
                            alternate_holder = True
                    
                list_lists.append(list_holder)

        list_string = []
        for list_indiv in list_lists:
            for idx in list_indiv:
                list_string.append(s[idx])

        output_str = "".join(list_string)

        return output_str
                


#%%
s = "PAYPALISHIRING"
numRows = 3
solution = Solution()
solution.convert(s, numRows) == "PAHNAPLSIIGYIR"
#%%
s = "PAYPALISHIRING"
numRows = 4
solution = Solution()
solution.convert(s, numRows) == "PINALSIGYAHRPI"

#%%
s = "PAYPALISHIRING"
numRows = 5
solution = Solution()
solution.convert(s, numRows) == "PHASIYIRPLIGAN"

#%%
s = "A"
numRows = 1
solution = Solution()
solution.convert(s, numRows) == "A"

# %%
s = "AB"
numRows = 1
solution = Solution()
solution.convert(s, numRows) == "AB"

# %%
s = "ABCDEF"
numRows = 1
solution = Solution()
solution.convert(s, numRows) == "ABCDEF"
# %%
