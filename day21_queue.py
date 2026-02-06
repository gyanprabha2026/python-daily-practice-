# Day 21 - Queue (FIFO)

# Queue implementation using list
queue = []

# Enqueue operation
def enqueue(element):
    queue.append(element)
    print(f"Enqueued: {element}")

# Dequeue operation
def dequeue():
    if is_empty():
        print("Queue is empty. Cannot dequeue.")
        return
    removed = queue.pop(0)
    print(f"Dequeued: {removed}")

# Peek operation
def peek():
    if is_empty():
        return "Queue is empty"
    return queue[0]

# Check if queue is empty
def is_empty():
    return len(queue) == 0

# Display queue
def display():
    print("Queue:", queue)


# ---------- Real Problems ----------

# 1. Simple ticket system simulation
def ticket_system(customers):
    q = []
    for c in customers:
        q.append(c)

    while q:
        print("Serving:", q.pop(0))


# ---------- Testing ----------
enqueue(10)
enqueue(20)
enqueue(30)
display()

dequeue()
display()

print("Front element:", peek())
print("Is queue empty?", is_empty())

print("\nTicket System:")
ticket_system(["Amit", "Neha", "Ravi"])
