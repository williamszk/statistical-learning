# https://leetcode.com/problems/valid-parentheses/

#%%
class Solution:
    def isValid(self, s: str) -> bool:
        # Is "s" an expression?
        # Yes, it is because, it arrives at a value.
        # Are declaration and assignment expressions?
        # No they are not, because they do not arrive 
        # at a value.
        output = None

        dict_special_characters = {
            "(":0,
            ")":0,
            "[":0,
            "]":0,
            "{":0,
            "}":0
        }
        
        list_characters = [x for x in s]

        for character in list_characters:
            dict_special_characters[character] += 1
        
        if all([
            dict_special_characters["("] == dict_special_characters[")"],
            dict_special_characters["["] == dict_special_characters["]"],
            dict_special_characters["{"] == dict_special_characters["}"]
        ]):
            output = True
        else:
            output = False

        return output


#%%
s = "()"
solution = Solution()
solution.isValid(s) == True
#%%
s = "()[]{}"
solution = Solution()
solution.isValid(s) == True
#%%
s = "(]"
solution = Solution()
solution.isValid(s) == False
#%%
s = "([)]"
solution = Solution()
solution.isValid(s) == False
#%%
s = "{[]}"
solution = Solution()
solution.isValid(s) == True
#%%








