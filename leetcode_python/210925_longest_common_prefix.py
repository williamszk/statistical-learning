# https://leetcode.com/problems/longest-common-prefix/
#%%
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = [""]
        is_max_array = False
        i = 0
        while True:
            list_letters = []
            for word in strs:
                try:
                    list_letters.append(word[i])
                except IndexError as e:
                    # we reached the max index 
                    is_max_array = True
                    break            
            if is_max_array:
                break
                        
            list_unique_letters = list(set(list_letters))
            if len(list_unique_letters) == 1:
                output.append(list_unique_letters[0])
                i += 1
            else:
                break
        
        return "".join(output)

#%%
strs = ["flower","flow","fl"]
solution = Solution()
solution.longestCommonPrefix(strs) == "fl"
#%%
strs = ["flower","flow","flight"]
solution = Solution()
solution.longestCommonPrefix(strs) == "fl"
#%%
strs = ["dog","racecar","car"]
solution = Solution()
solution.longestCommonPrefix(strs) == ""
#%%

#%%

#%%

#%%

