

# DoublyLinkedList 

## Overview

The `DoublyLinkedList` class implements a doubly linked list where each node has references to both the previous and next nodes. This allows for traversal in both directions.

## Node Class

### Definition
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
```

### Description
The `Node` class represents a node in the doubly linked list.

- **Attributes**:
  - `value`: The value stored in the node.
  - `next`: A reference to the next node in the list.
  - `prev`: A reference to the previous node in the list.

## DoublyLinkedList Class

### Definition
```python
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
```

### Description
The `DoublyLinkedList` class manages operations for the doubly linked list.

- **Attributes**:
  - `head`: A reference to the first node in the list.
  - `tail`: A reference to the last node in the list.
  - `length`: The number of nodes in the list.

### Methods

#### `print()`

```python
def print(self):
    temp = self.head
    while temp:
        print(f"({temp.prev.value if temp.prev else None}, {temp.value}, {temp.next.value if temp.next else None})", end=" <-> ")
        temp = temp.next
    print("None")
```

**Description**: 
Prints the values of all nodes in the doubly linked list, including references to the previous and next nodes, and ends with `None` to indicate the end of the list.

**Time Complexity**: O(n) where n is the number of nodes in the list. The method iterates through the list once to print each node.

#### `append(value)`

```python
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
```

**Description**: 
Adds a new node with the specified value to the end of the list. Updates the tail and maintains the previous and next references.

**Time Complexity**: O(1). Appending a node involves a constant number of operations regardless of the list's length.

#### `prepend(value)`

```python
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
```

**Description**: 
Adds a new node with the specified value to the beginning of the list. Updates the head and ensures the previous and next references are maintained.

**Time Complexity**: O(1). Prepending a node involves a constant number of operations regardless of the list's length.

#### `pop()`

```python
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
```

**Description**: 
Removes and returns the last node from the list. Updates the tail and maintains the previous and next references.

**Time Complexity**: O(1). Removing the tail node involves a constant number of operations.

#### `pop_first()`

```python
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
```

**Description**: 
Removes and returns the first node from the list. Updates the head and ensures the previous and next references are maintained.

**Time Complexity**: O(1). Removing the head node involves a constant number of operations.

#### `get(index)`

```python
def get(self, index):
    if index < 0 or index >= self.length:
        print(f"Index {index} out of bounds.")
        return None
    temp = self.head
    for _ in range(index):
        temp = temp.next
    print(f"Value at index {index} is {temp.value}")
    return temp
```

**Description**: 
Returns the node at the specified index. Indexing is zero-based.

**Time Complexity**: O(n) where n is the index. Retrieving a node requires traversing the list up to the given index.

#### `set(index, value)`

```python
def set(self, index, value):
    node = self.get(index)
    if node:
        node.value = value
        print(f"Set index {index} to {value}:")
        self.print()
        return node
    print(f"Failed to set value at index {index}.")
    return False
```

**Description**: 
Updates the value of the node at the specified index.

**Time Complexity**: O(n) where n is the index. Setting a value involves finding the node first, which is O(n).

#### `insert(index, value)`

```python
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
```

**Description**: 
Inserts a new node with the specified value at the given index. Uses `prepend` or `append` for indices at the beginning or end.

**Time Complexity**: O(n) where n is the index. Inserting involves finding the previous node, which requires traversal.

#### `reverse()`

```python
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
```

**Description**: 
Reverses the order of nodes in the list while maintaining the previous and next references.

**Time Complexity**: O(n) where n is the number of nodes in the list. Reversing requires traversing the entire list.

---
