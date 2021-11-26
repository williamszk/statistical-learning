"""
The objective of this script is to build an implementation of 
binary search tree.

Here are some attempts to implement trees in Python...
Not so sure if those are good ones, but are some attempts, 
just for fun and exercise.
"""

import json
import my_helper_module as my

# how to represent a tree?
# how to represent a binary tree?

# given an array, build a function that can make a binary search tree 
# using the array as argument

class TreeNode:
    def __init__(
            self, 
            value: float = None, 
            parent = None, 
            left_child = None, 
            right_child = None
        ):
        # I can't reference the class inside of itself, before defining it
        # Maybe this is an characteristics of all OOP languanges
        # The attributes/properties of a class can't be of the class
        # that is itself
        # We should try to do this in Java and C++ too
        self.value = value 
        self.parent = parent 
        self.left_child = left_child
        self.right_child = right_child


    def __repr__(self):
       return (
          f"Intance of TreeNode class\n"
          f"Value: {self.value}\n"
          f"Parent tree: \n" # I don't know how to show some representation of the parent node
          f"Left child: \n"
          f"Right child: \n"
        )

    # the root_node doesn't have a parent node


class Tree:
    def __init__(self, root_node=None):
        self.root_node: TreeNode = root_node 

# leafs are TreeNodes without children
# but leafs must contain a parent


root_node = TreeNode(value=2)
node_1 = TreeNode(value=3, parent=root_node)

#  value: float = None, 
#  parent = None, 
#  left_child = None, 
#  right_child = None

my_array = [20, 2, 3, 8, 4, 12, 9, 4, 2]
print(
    "My original array to be included into a binary tree:\n"
    f"{my_array}"
)


root_node = TreeNode(value=20)

node_1 = TreeNode(value=2, parent=root_node)
root_node.left_child = node_1



# let's try to use a dictionary as the data structure
# to hold the information of a tree
# another try

dict_tree = {}

# first element of the array is 20
# so 20 is the nodo root
dict_tree["root_node"] = {
        "value": 20,
        "parent": None,
        "left_child":None,
        "right_child": None
        }

print("\n""Iteration 1:")
my.printdict(dict_tree)


# next element of the array is 2


dict_tree["node_1"] = {
        "value": 2,
        "parent": "root_node",
        "left_child": None,
        "right_child": None
        }
# on the same time that I insert this new node I need to
# update the parent node, in this case it is the root itself

name_parent_node = dict_tree["node_1"].get("parent")
dict_tree[name_parent_node]["left_child"] = "node_1"

print("\n""Iteration 2:")
my.printdict(dict_tree)


name_new_node = "node_2"


dict_tree[name_new_node] = {
        "value": 3,
        "parent": "node_1",
        "left_child": None,
        "right_child": None
        }

name_parent_node = dict_tree[name_new_node].get("parent")
dict_tree[name_parent_node]["right_child"] = name_new_node

print("\n""Iteration 3:")
my.printdict(dict_tree)































