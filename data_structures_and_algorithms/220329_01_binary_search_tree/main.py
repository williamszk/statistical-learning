

class Node:
    def __init__(self, value, parent=None, child_left=None, child_right=None) -> None:
        self.value = value
        self.parent = parent
        self.child_left = child_left
        self.child_right = child_right
    
    def __repr__(self) -> str:
        repr_child_left = self.child_left
        repr_child_right = self.child_right
        repr_parent = self.parent

        if repr_child_left:
            repr_child_left = hex(id(repr_child_left))

        if repr_child_right:
            repr_child_right = hex(id(repr_child_right))

        if repr_parent:
            repr_parent = hex(id(repr_parent))

        return (
            f"+-----------------------------------------+\n"
            f"| A Node instance: {hex(id(self))}\n"
            f"| value = {self.value}\n"
            f"| parent = {repr_parent}\n"
            f"| child_left = {repr_child_left}\n"
            f"| child_right = {repr_child_right}\n"
            f"+-----------------------------------------+"
        )

class BinaryTree:
    def __init__(self, root_node: Node) -> None:
        self.root_node = root_node

    def __repr__(self) -> str:
        """
        
        """
        # inlcude in the number of nodes in the tree
        return f"An instance of Binary Tree"

    def find_node(self, value):
        pass

    def insert_node(self, new_node: Node):
        node = self.root_node
        while node:
            last_node = node
            if new_node.value > node.value:
                node = node.child_right
            else:
                node = node.child_left

        if new_node.value > last_node.value:
            last_node.child_right = new_node
        else:
            last_node.child_left = new_node

root_node = Node(10, parent=None, child_left=None, child_right=None)
binary_tree = BinaryTree(root_node)
# print(binary_tree)
# print(binary_tree.root_node)

binary_tree.insert_node(Node(4))
binary_tree.insert_node(Node(6))
binary_tree.insert_node(Node(18))


print("finished")
