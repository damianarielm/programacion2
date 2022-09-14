def createBST(data_list):
    BST_tree = None

    while data_list:
        cargo = data_list.pop()
        BST_tree = insertBST(cargo,BST_tree)

    return BST_tree
