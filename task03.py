def sum_of_values(node):
    """Calculates the sum of all values in the AVL tree."""
    if node is None:
        return 0
    return node.key + sum_of_values(node.left) + sum_of_values(node.right)