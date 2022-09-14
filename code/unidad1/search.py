def searchBST(D, BST_tree):
    if BST_tree == None:
        return False
    else:
        if D < BST_tree.cargo:
            return searchBST(D, BST_tree.left)
        elif D > BST_tree.cargo:
            return searchBST(D, BST_tree.right)
        else:
            return True
