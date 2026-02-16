# Day 31 - Binary Tree Basics


# 1. Node Definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 2. DFS Traversals

# Inorder (Left, Root, Right)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


# Preorder (Root, Left, Right)
def preorder(root):
    if root is None:
        return
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)


# Postorder (Left, Right, Root)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")


# --------- Create Sample Tree ---------

#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# --------- Testing ---------

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)
