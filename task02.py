def find_min_value(node):
    """Finds the minimum value in the AVL tree."""
    current = node
    while current.left is not None:
        current = current.left
    return current.key