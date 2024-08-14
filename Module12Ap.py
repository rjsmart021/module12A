"""
This module implements and tests various tree traversal algorithms on a binary tree.
"""

class Node:
    """
    A class to represent a node in a binary tree.
    """
    def __init__(self, key):
        """
        Initialize the node with a key, and left and right children as None.
        """
        self.left = None
        self.right = None
        self.val = key


def print_inorder(root):
    """
    Perform in-order traversal of the binary tree.
    """
    if root:
        # First recur on left child
        print_inorder(root.left)
        # Then print the data of node
        print(root.val, end=' ')
        # Now recur on right child
        print_inorder(root.right)


def print_preorder(root):
    """
    Perform pre-order traversal of the binary tree.
    """
    if root:
        # First print the data of node
        print(root.val, end=' ')
        # Then recur on left child
        print_preorder(root.left)
        # Now recur on right child
        print_preorder(root.right)


def print_postorder(root):
    """
    Perform post-order traversal of the binary tree.
    """
    if root:
        # First recur on left child
        print_postorder(root.left)
        # Then recur on right child
        print_postorder(root.right)
        # Now print the data of node
        print(root.val, end=' ')


# Construct the binary tree
root_node = Node(50)
root_node.left = Node(30)
root_node.right = Node(70)
root_node.left.left = Node(40)
root_node.left.right = Node(20)
root_node.right.left = Node(60)
root_node.right.right = Node(80)

# Test traversals
print("In-order traversal:")
print_inorder(root_node)

print("\nPre-order traversal:")
print_preorder(root_node)

print("\nPost-order traversal:")
print_postorder(root_node)