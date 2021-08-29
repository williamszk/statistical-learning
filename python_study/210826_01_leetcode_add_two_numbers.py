

#%%
# -----------------------------------------------------------
# https://leetcode.com/problems/add-two-numbers/
# 210826_01_leetcode_add_two_numbers.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        return f"ListNode(val: {self.val}, next: {self.next})"


l1 = [2,4,3]
l2 = [5,6,4]

l1 = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(val = 3, next=None)))
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
print(l1)

ListNode(2, ListNode(4, ListNode(3, None)))

#%%
# create a function where we pass an argument as a list
# then we create a linked list of ListNode
def create_linked_list(array):
    array.reverse()
    for i, x in enumerate(array):
        if i == 0:
            my_list_node = ListNode(x, None)
        else:
            my_list_node = ListNode(x, my_list_node)
    
    return my_list_node

#%%
array = [2,4,3]
create_linked_list(array)
#%%
array = [5,6,4]
create_linked_list(array)
#%%

l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        list_1 = []
        list_2 = []
        while True:    
            list_1.append(l1.val)
            l1 = l1.next

            if l1 == None:
                break    

        while True:    
            list_2.append(l2.val)
            l2 = l2.next

            if l2 == None:
                break    

        # this snipped transform the linked list into a python list

        list_1.reverse()
        list_2.reverse()

        number_1 = int("".join([str(x) for x in list_1]))
        number_2 = int("".join([str(x) for x in list_2]))

        sum_output = number_1 + number_2        
        list_int_output = [int(x) for x in str(sum_output)]        
        list_int_output.reverse()
        linked_list_output = create_linked_list(list_int_output)

        return linked_list_output

#%%

9_999_999 + 9_999


l1 = create_linked_list([5,6])
l2 = create_linked_list([5,4,9])
my_solution = Solution()
my_solution.addTwoNumbers(l1, l2)

945 + 65
101

# %%
# --------------------------------------------
# I have the impression that Python's type hitting is giving exceptions

def myfunc(x: int) -> str:
    return None

myfunc("hello")

# no, my hypothesis is not correct. 
# the phenomenon occured because I was working on the __repr__ method
# and it forces the user to have a string as return value

#%%
