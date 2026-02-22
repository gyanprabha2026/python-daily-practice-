# Day 36 - Advanced Tree Problems (LCA & Maximum Path Sum)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 1️⃣ Lowest Common Ancestor (LCA)

def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root.value == p or root.value == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right


# 2️⃣ Maximum Path Sum

def max_path_sum(root):
    max_sum = [float("-inf")]

    def dfs(node):
        if node is None:
            return 0

        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)

        # Update global max
        max_sum[0] = max(max_sum[0], node.value + left + right)

        return node.value + max(left, right)

    dfs(root)
    return max_sum[0]


# --------- Create Sample Tree ---------

#         10
#        /  \
#       2    10
#      / \     \
#     20  1    -25
#               /  \
#              3    4

root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)


# --------- Testing ---------

lca_node = lowest_common_ancestor(root, 20, 1)
print("LCA of 20 and 1:", lca_node.value if lca_node else None)

print("Maximum Path Sum:", max_path_sum(root))
