# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#%%
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(var: {self.val}, next: {self.next})"

    def __eq__(self, other: ListNode) -> bool:
        output = False
        if isinstance(other, ListNode):
            if self.val == other.val and self.next == other.next:
                output = True

        return output


def transform_list_into_list_node(my_list: List) -> ListNode:
    my_list_2 = [x for x in reversed(my_list)]
    output_list_node = ListNode(my_list_2[0], None)
    for item in my_list_2[1:]:
        output_list_node = ListNode(item, output_list_node) 

    return output_list_node


def length_of_node(list_node: ListNode) -> int:
    length_list_node = 0
    if list_node.next == None:
        length_list_node = 1
    else:
        length_list_node = length_of_node(list_node.next) + 1

    return length_list_node


def append_element_to_list_node(list_node: ListNode, element: object) -> ListNode:
    if list_node.next == None:
        list_node.next = ListNode(element, None) 
        return list_node
    else:
        pass
    


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_head = length_of_node(head)
        remove_index = len_head - n

        output_node_holder = ListNode(head.val, None)
        list_node_holder = head.next
        for i in range(len_head):
            print(i)
            if i != remove_index:
                print("passei aqui!")
                output_node_holder.next = ListNode(list_node_holder.val, None)
                output_node_holder 

                list_node_holder = list_node_holder.next

            print(output_node_holder)
        return output_node_holder

#%%
ListNode(1, None) == ListNode(1, None)
#%%
ListNode(1, None) != ListNode(1, ListNode(2, None))
#%%
ListNode(1, ListNode(2, None)) == ListNode(1, ListNode(2, None))
#%%
ListNode(10, ListNode(2, None)) != ListNode(1, ListNode(2, None))
#%%
ListNode(1, ListNode(4, None)) != ListNode(1, ListNode(2, None))
#%%
head = [1,2,3,4,5]
transform_list_into_list_node(head) == ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
#%%
list_node = ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))
length_of_node(list_node) == 4
#%%
list_node = ListNode(2, ListNode(3, None))
length_of_node(list_node) == 2
#%%
head = transform_list_into_list_node([1,2,3,4,5])
n = 2
solution = Solution()
solution.removeNthFromEnd(head, n) ==  transform_list_into_list_node([1,2,3,5])
#%%
head = [1]
n = 1
solution = Solution()
solution.removeNthFromEnd(head, n) == []
#%%
head = [1, 2]
n = 1
solution = Solution()
solution.removeNthFromEnd(head, n) == [1]
#%%



#%%



#%%



