class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp:
            print(f"({temp.prev.value if temp.prev else None}, {temp.value}, {temp.next.value if temp.next else None})", end=" <-> ")
            temp = temp.next
        print("None")

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        print(f"Appended {value}:")
        self.print()

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        print(f"Prepended {value}:")
        self.print()

    def pop(self):
        if self.length == 0:
            print("Nothing to pop, list is empty.")
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        print(f"Popped value {popped_node.value}:")
        self.print()
        return popped_node.value

    def pop_first(self):
        if self.length == 0:
            print("Nothing to pop, list is empty.")
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        print(f"Popped first value {popped_node.value}:")
        self.print()
        return popped_node.value

    def get(self, index):
        if index < 0 or index >= self.length:
            print(f"Index {index} out of bounds.")
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        print(f"Value at index {index} is {temp.value}")
        return temp

    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            print(f"Set index {index} to {value}:")
            self.print()
            return node
        print(f"Failed to set value at index {index}.")
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print(f"Cannot insert at index {index}, out of bounds.")
            return False
        if index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        else:
            new_node = Node(value)
            prev_node = self.get(index - 1)
            next_node = prev_node.next
            new_node.next = next_node
            new_node.prev = prev_node
            prev_node.next = new_node
            if next_node:
                next_node.prev = new_node
            self.length += 1
            print(f"Inserted {value} at index {index}:")
            self.print()
            return True
        print(f"Failed to insert {value} at index {index}.")
        return False

    def reverse(self):
        if self.length == 0:
            print("Nothing to reverse, list is empty.")
            return None
        temp = None
        current = self.head
        self.head = self.tail
        self.tail = current
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        print("Reversed list:")
        self.print()


# Test and Debug
my_dlist = DoublyLinkedList(1)
my_dlist.print()

# Append values to the list
my_dlist.append(2)
my_dlist.append(3)

# Prepend value to the list
my_dlist.prepend(0)

# Pop last element
my_dlist.pop()

# Pop first element
my_dlist.pop_first()

# Get value at index 1
my_dlist.get(1)

# Set value at index 1
my_dlist.set(1, 99)

# Insert value at index 1
my_dlist.insert(1, 10)

# Insert at head
my_dlist.insert(0, -1)

# Insert at tail
my_dlist.insert(my_dlist.length, 100)

# Reverse the list
my_dlist.reverse()
