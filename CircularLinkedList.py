class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.tail.next = self.head  # Points back to head to make it circular
        self.length = 1

    def print(self):
        if self.length == 0:
            print("List is empty.")
            return
        temp = self.head
        for _ in range(self.length):
            print(f"({temp.value})", end=" -> ")
            temp = temp.next
        print(f"({self.head.value})")  # To show circularity

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular link
        self.length += 1
        print(f"Appended {value}:")
        self.print()

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head  # Circular link
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
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
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
            self.tail.next = self.head  # Circular link
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
            new_node.next = prev_node.next
            prev_node.next = new_node
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
        prev = None
        current = self.head
        next_node = current.next
        for _ in range(self.length):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.tail = self.head
        self.head = prev
        self.tail.next = self.head  # Circular link
        print("Reversed list:")
        self.print()


# Test and Debug
my_clist = CircularLinkedList(1)
my_clist.print()

# Append values to the list
my_clist.append(2)
my_clist.append(3)

# Prepend value to the list
my_clist.prepend(0)

# Pop last element
my_clist.pop()

# Pop first element
my_clist.pop_first()

# Get value at index 1
my_clist.get(1)

# Set value at index 1
my_clist.set(1, 99)

# Insert value at index 1
my_clist.insert(1, 10)

# Insert at head
my_clist.insert(0, -1)

# Insert at tail
my_clist.insert(my_clist.length, 100)

# Reverse the list
my_clist.reverse()
