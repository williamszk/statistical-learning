# https://leetcode.com/problems/regular-expression-matching/
#%%
def find_consecutive_trues(list_bool):
    list_output = [False]*len(list_bool)
    for j, bool_item in enumerate(list_bool):
        if j == 0:
            if bool_item:
                list_output[j] = True    
            else:
                break        
        elif bool_item:
            # only runs begining in index 1, the second run forwards
            list_output[j] = True        
        else:
            break

    return list_output


def keep_non_matching_characters(list_string, list_bool):
    """
    list_string = ["a", "b", "c", "d", "e"]
    list_bool = [True, False, False, False, False]
    """

    if len(list_string) != len(list_bool):
        raise Exception("list_string and list_bool should have the same length.")

    keep_list_string = [x for x,y in zip(list_string, list_bool) if y == False]

    return keep_list_string



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        answer = None
        list_string = [x for x in s]
        i = 0; letter = p[i]
        for i, letter in enumerate(p):
            print(i, letter)
            if letter != ".":
                if p[i+1] == "*":
                    list_bool = [x == letter for x in s]
                    list_bool = find_consecutive_trues(list_bool)
                    list_string = keep_non_matching_characters(list_string, list_bool)
                
                else:
                    # next character is not "*"

            
            else:
                # in case where letter == "."

#%%
list_string = ["a", "b", "c", "d"]
list_bool = [True, True, False, False]
keep_non_matching_characters(list_string, list_bool) == ["c", "d"]
#%%
list_bool = [True]
find_consecutive_trues(list_bool) == [True]
#%%
list_bool = [False]
find_consecutive_trues(list_bool) == [False]
#%%
list_bool = [False, False, False, True]
find_consecutive_trues(list_bool) == [False, False, False, False]
#%%
list_bool = [True, False, False, True]
find_consecutive_trues(list_bool) == [True, False, False, False]
#%%
list_bool = [True, True, False, True]
find_consecutive_trues(list_bool) == [True, True, False, False]
#%%
s = "baabbaacded"
p = "a*bb"
solution = Solution()
solution.isMatch(s, p) == False

#%%
s = "aaabbaacded"
p = "a*bb"
solution = Solution()
solution.isMatch(s, p) == False

#%%
s = "aa"
p = "a"
solution = Solution()
solution.isMatch(s, p) == False

#%%
s = "aa"
p = "a*"
solution = Solution()
solution.isMatch(s, p) == True

#%%
s = "ab"
p = ".*"
solution = Solution()
solution.isMatch(s, p) == True

#%%
s = "aab"
p = "c*a*b"
solution = Solution()
solution.isMatch(s, p) == True
#%%
s = "mississippi"
p = "mis*is*p*."
solution = Solution()
solution.isMatch(s, p) == False
#%%


