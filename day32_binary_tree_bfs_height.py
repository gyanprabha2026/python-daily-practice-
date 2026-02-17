# Day 32 - Binary Tree BFS & Height


from collections import deque


# 1. Node Definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 2. Level Order Traversal (BFS)
def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


# 3. Height of Binary Tree
def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1


# 4. Count Total Nodes
def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


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

print("Level Order Traversal:")
level_order(root)

print("\nHeight of Tree:", height(root))
print("Total Nodes:", count_nodes(root))
