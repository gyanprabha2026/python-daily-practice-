# Day 33 - Binary Search Tree (BST)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 1. Insert into BST
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


# 2. Search in BST
def search(root, key):
    if root is None:
        return False

    if root.value == key:
        return True
    elif key < root.value:
        return search(root.left, key)
    else:
        return search(root.right, key)


# 3. Inorder Traversal (Gives Sorted Order)
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


# 4. Find Minimum
def find_min(root):
    while root.left:
        root = root.left
    return root.value


# 5. Find Maximum
def find_max(root):
    while root.right:
        root = root.right
    return root.value


# --------- Testing ---------

values = [50, 30, 70, 20, 40, 60, 80]
root = None

for val in values:
    root = insert(root, val)

print("Inorder Traversal (Sorted):")
inorder(root)

print("\nSearch 40:", search(root, 40))
print("Search 100:", search(root, 100))

print("Minimum Value:", find_min(root))
print("Maximum Value:", find_max(root))
