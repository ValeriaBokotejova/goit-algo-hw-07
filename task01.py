def find_max_value(node):
    """Finds the maximum value in the AVL tree."""
    current = node
    while current.right is not None:
        current = current.right
    return current.key