# Day 20 - Stack (LIFO)

# ---------- Stack Implementation using List ----------
stack = []

# Push operation
def push(element):
    stack.append(element)
    print(f"Pushed: {element}")

# Pop operation
def pop():
    if is_empty():
        print("Stack is empty. Cannot pop.")
        return
    removed = stack.pop()
    print(f"Popped: {removed}")

# Peek operation
def peek():
    if is_empty():
        return "Stack is empty"
    return stack[-1]

# Check if stack is empty
def is_empty():
    return len(stack) == 0

# Display stack
def display():
    print("Stack:", stack)


# ---------- Real Problems ----------

# 1. Reverse a string using stack
def reverse_string(s):
    temp_stack = []
    for ch in s:
        temp_stack.append(ch)

    reversed_str = ""
    while temp_stack:
        reversed_str += temp_stack.pop()

    return reversed_str


# 2. Check balanced parentheses
def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expression:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0


# ---------- Testing ----------
push(10)
push(20)
push(30)
display()

pop()
display()

print("Top element:", peek())
print("Is stack empty?", is_empty())
display()
print("Reverse of 'python':", reverse_string("python"))
print("Is balanced '({[]})'?", is_balanced("({[]})"))
