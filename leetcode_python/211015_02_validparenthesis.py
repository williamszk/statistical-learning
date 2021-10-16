# https://www.youtube.com/watch?v=WTzjTskDFMg&ab_channel=NeetCode
#%%
class Solution:
    def isValid(self, s: str) -> bool:
        # Is "s" an expression?
        # Yes, it is because, it arrives at a value.
        # Are declaration and assignment expressions?
        # No they are not, because they do not arrive 
        # at a value.
        output = None
        dict_open_close = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        open_keys = list(dict_open_close.keys())

        list_characters = [x for x in s]
        if list_characters[0] in [")", "]", "}"]:
            output = False
        elif list_characters[-1] in ["(", "[", "{"]:
            output = False
        else:
            list_open = []
            for char in list_characters:
                if list_open == []:
                    list_open.append(char)
                else:
                    if char in open_keys:
                        list_open.append(char)
                    else:
                        if char == dict_open_close.get(list_open[-1]):
                            list_open.pop()
                        else:
                            output = False
                            break
                        
            if list_open == []:
                output = True

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