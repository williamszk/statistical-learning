# https://leetcode.com/problems/palindrome-number/

#%%
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        list_string_x = [i for i in string_x]
        list_string_x.reverse()

        reversed_string = ""    .join(list_string_x)

        return reversed_string == string_x

#%%
# Follow up: Could you solve it without converting the integer to a string?

def transform_int_into_list(the_integer):
    list_holder = []
    temp_integer = the_integer
    while True:
        rest = temp_integer % 10
        list_holder.append(rest)

        if temp_integer < 10:
            break

        temp_integer = temp_integer // 10

    return list_holder


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            output = False
        else:
            # take out the digits of an integer
            list_integers = transform_int_into_list(x)
            list_integers_copy = list_integers.copy()
            list_integers_copy.reverse()
            
            output = list_integers == list_integers_copy

        
        return output 


#%%
the_integer = 121
transform_int_into_list(the_integer) == [1,2,1]
#%%
the_integer = 10
transform_int_into_list(the_integer) == [0,1]

#%%
x = 10
solution = Solution()
solution.isPalindrome(x) == False
#%%
x = -101
solution = Solution()
solution.isPalindrome(x) == False
#%%
x = 121
solution = Solution()
solution.isPalindrome(x) == True
#%%



