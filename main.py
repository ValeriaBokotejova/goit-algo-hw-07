from avl_tree import AVLNode, insert
from task01 import find_max_value
from task02 import find_min_value
from task03 import sum_of_values

# Creating the AVL tree and inserting values
root = None
keys = [10, 20, 30, 25, 28, 27, -1, 2, 32, 14, 5, 11]

for key in keys:
    root = insert(root, key)

# Task 1: Find the maximum value in the tree
max_value = find_max_value(root)
print(f"Maximum value in the tree: {max_value}")

# Task 2: Find the minimum value in the tree
min_value = find_min_value(root)
print(f"Minimum value in the tree: {min_value}")

# Task 3: Calculate the sum of all values in the tree
total_sum = sum_of_values(root)
print(f"Sum of all values in the tree: {total_sum}")