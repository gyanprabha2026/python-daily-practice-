# Day 34 - Delete Node in BST


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Insert
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# Inorder Traversal
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


# Find Minimum (Inorder Successor)
def find_min(root):
    while root.left:
        root = root.left
    return root


# Delete Node
def delete_node(root, key):
    if root is None:
        return None

    # Step 1: Search
    if key < root.value:
        root.left = delete_node(root.left, key)

    elif key > root.value:
        root.right = delete_node(root.right, key)

    else:
        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Case 3: Two children
        successor = find_min(root.right)
        root.value = successor.value
        root.right = delete_node(root.right, successor.value)

    return root


# --------- Testing ---------

values = [50, 30, 70, 20, 40, 60, 80]
root = None

for val in values:
    root = insert(root, val)

print("Original BST (Inorder):")
inorder(root)

# Delete examples
root = delete_node(root, 20)  # Leaf
root = delete_node(root, 30)  # One child
root = delete_node(root, 50)  # Two children

print("\n\nBST After Deletions:")
inorder(root)
