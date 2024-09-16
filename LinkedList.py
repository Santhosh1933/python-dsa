class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
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
            self.head = new_node
        self.length += 1
        print(f"Prepended {value}:")
        self.print()

    def pop(self):
        if self.length == 0:
            print("Nothing to pop, list is empty.")
            return None
        after = self.head
        curr = self.head
        while after.next:
            curr = after
            after = after.next
        self.tail = curr
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        print(f"Popped value {after.value}:")
        self.print()
        return after.value

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
            if prev_node:
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
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        print("Reversed list:")
        self.print()


# Test and Debug
my_list = LinkedList(1)
my_list.print()

# Append values to the list
my_list.append(2)
my_list.append(3)

# Prepend value to the list
my_list.prepend(0)

# Pop last element
my_list.pop()

# Get value at index 1
my_list.get(1)

# Set value at index 1
my_list.set(1, 99)

# Insert value at index 2
my_list.insert(2, 10)

# Insert at head
my_list.insert(0, -1)

# Insert at tail
my_list.insert(my_list.length, 100)

# Reverse the list
my_list.reverse()
