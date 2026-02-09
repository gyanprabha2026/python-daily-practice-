# Day 24 - Linked List Advanced Problems

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 1. Reverse Linked List
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    # 2. Detect Cycle (Floyd’s Cycle Detection)
    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 3. Remove Nth Node from End
    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        self.head = dummy.next

    # 4. Find Length
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


# ---------- Testing ----------
ll = LinkedList()
ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(4)
ll.insert_end(5)

print("Original List:")
ll.display()

print("\nReversed List:")
ll.reverse()
ll.display()

print("\nRemove 2nd node from end:")
ll.remove_nth_from_end(2)
ll.display()

print("\nCycle Detected:", ll.detect_cycle())
print("Length of Linked List:", ll.length())
