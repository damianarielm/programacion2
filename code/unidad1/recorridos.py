def printTreePreOrder(tree):
    if tree == None: return
    print(tree.cargo)
    printTreePreOrder(tree.left)
    printTreePreOrder(tree.right)
def printTreeInOrder(tree):
    if tree == None: return
    printTreeInOrder(tree.left)
    print(tree.cargo)
    printTreeInOrder(tree.right)
def printTreePostorder(tree):
    if tree == None: return
    printTreePostorder(tree.left)
    printTreePostorder(tree.right)
    print(tree.cargo)
