
import random
import time
from statistics import median

def deterministic_select(arr, k):
    """
    Deterministic algorithm for selection in worst-case linear time (Median of Medians).
    Finds the k-th smallest element in the array.
    """
    if len(arr) <= 5:
        # Base case: Sort and return the k-th element
        return sorted(arr)[k]

    # Step 1: Divide into groups of 5 and find medians
    medians = [median(group) for group in (arr[i:i + 5] for i in range(0, len(arr), 5))]

    # Step 2: Recursively find the median of medians
    pivot = deterministic_select(medians, len(medians) // 2)

    # Step 3: Partition around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(low) - len(high)

    if k < len(low):
        return deterministic_select(low, k)
    elif k < len(low) + pivot_count:
        return pivot  # Pivot is the k-th element
    else:
        return deterministic_select(high, k - len(low) - pivot_count)


def randomized_select(arr, k):
    """
    Randomized algorithm for selection in expected linear time (Randomized Quickselect).
    Finds the k-th smallest element in the array.
    """
    if len(arr) == 1:
        return arr[0]

    # Step 1: Choose a random pivot
    pivot = random.choice(arr)

    # Step 2: Partition around the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(low) - len(high)

    if k < len(low):
        return randomized_select(low, k)
    elif k < len(low) + pivot_count:
        return pivot  # Pivot is the k-th element
    else:
        return randomized_select(high, k - len(low) - pivot_count)


# Empirical Analysis
def empirical_analysis():
    input_sizes = [10, 100, 1000, 10000]
    distributions = {
        "random": lambda n: [random.randint(1, 1000) for _ in range(n)],
        "sorted": lambda n: list(range(1, n + 1)),
        "reverse_sorted": lambda n: list(range(n, 0, -1))
    }

    print("{:<15} {:<10} {:<15} {:<15}".format("Input Type", "Size", "Deterministic (s)", "Randomized (s)"))
    for dist_name, dist_gen in distributions.items():
        for size in input_sizes:
            arr = dist_gen(size)
            k = size // 2  # Median

            # Measure deterministic algorithm
            start = time.time()
            deterministic_select(arr, k)
            deterministic_time = time.time() - start

            # Measure randomized algorithm
            start = time.time()
            randomized_select(arr, k)
            randomized_time = time.time() - start

            print("{:<15} {:<10} {:<15.6f} {:<15.6f}".format(dist_name, size, deterministic_time, randomized_time))


if __name__ == "__main__":
    # Example usage
    arr = [12, 3, 5, 7, 19, 1, 4, 10, 6]
    k = 4  # Find the 4th smallest element
    print("Deterministic Selection:", deterministic_select(arr, k))
    print("Randomized Selection:", randomized_select(arr, k))

    # Run empirical analysis
    empirical_analysis()

# Array Implementation
class Array:
    def __init__(self):
        self.array = []

    def insert(self, index, value):
        self.array.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.array):
            return self.array.pop(index)
        return None

    def access(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        return None

    def display(self):
        return self.array


# Matrix Implementation
class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        self.matrix[row][col] = value

    def access(self, row, col):
        return self.matrix[row][col]

    def display(self):
        for row in self.matrix:
            print(row)


# Stack Implementation (using Array)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack


# Queue Implementation (using Array)
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return self.queue


# Singly Linked List Implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if self.head is None:
            return None
        if self.head.value == value:
            self.head = self.head.next
            return value
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            deleted_node = current.next
            current.next = current.next.next
            return deleted_node.value
        return None

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


# Rooted Tree Implementation using Linked Lists
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print(" " * level * 4 + str(self.value))
        for child in self.children:
            child.display(level + 1)


# Example Usage
if __name__ == "__main__":
    # Array Example
    print("Array Example:")
    arr = Array()
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(2, 30)
    arr.delete(1)
    print("Access index 1:", arr.access(1))
    print("Array:", arr.display())

    # Matrix Example
    print("\nMatrix Example:")
    mat = Matrix(3, 3)
    mat.insert(0, 0, 5)
    mat.insert(1, 1, 10)
    mat.insert(2, 2, 15)
    mat.display()

    # Stack Example
    print("\nStack Example:")
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())
    print("Stack:", stack.display())

    # Queue Example
    print("\nQueue Example:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Dequeue:", queue.dequeue())
    print("Queue:", queue.display())

    # Singly Linked List Example
    print("\nSingly Linked List Example:")
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.traverse()
    sll.delete(2)
    sll.traverse()

    # Rooted Tree Example
    print("\nRooted Tree Example:")
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    grandchild1 = TreeNode("Grandchild 1")
    child1.add_child(grandchild1)
    root.add_child(child1)
    root.add_child(child2)
    root.display()