def insertBST(new_data, BST_tree):
    if tree == None:
        return BinaryTree(new_data, None, None)

    if new_data < BST_tree.cargo:
        x = insertBST(new_data,BST_tree.left)
        return BinaryTree(BST_tree.cargo, x, BST_tree.right)
    elif new_data > BST_tree.cargo:
        x = insertBST(new_data,BST_tree.right)
        return BinaryTree(BST_tree.cargo, BST_tree.left, x)
    else:
        return BST_tree
