# https://leetcode.com/problems/longest-substring-without-repeating-characters/

#%%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            max_counter = 0
        
        elif len(s) == 1:
            max_counter = 1
        
        else:
            list_lengths = []
            for i in range(len(s)):
                counter = 0
                set_chars = set()
                string_2 = s[i:]
                for char in string_2:
                    if char in set_chars:
                        list_lengths.append(counter)
                        break
                    else:
                        counter += 1
                        set_chars = set_chars.union({char})
                                                
                list_lengths.append(counter)
            
            max_counter = max(list_lengths)

        return max_counter


# %%
s = "dvdf"
solution = Solution()
solution.lengthOfLongestSubstring(s) == 3

#%%
s = "abcabcbb"
solution = Solution()
solution.lengthOfLongestSubstring(s) == 3

#%%
s = ""
solution = Solution()
solution.lengthOfLongestSubstring(s) == 0
#%%
s = "pwwkew"
solution = Solution()
solution.lengthOfLongestSubstring(s) == 3

#%%
s = " "
solution = Solution()
solution.lengthOfLongestSubstring(s) == 1

#%%
s = "c"
solution = Solution()
solution.lengthOfLongestSubstring(s) == 1
    
# %%
s = "au"
solution = Solution()
solution.lengthOfLongestSubstring(s) == 2

# %%

# %%
