from binary import BinaryTree

# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print("left child root val is " + r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())


def buildTree():
    r = BinaryTree('a')

    r.insertLeft('b')
    l = r.getLeftChild()
    l.insertRight('d')

    r.insertRight('c')
    ri = r.getRightChild()
    ri.insertLeft('e')
    ri.insertRight('f')

    return r

ttree = buildTree()
print(ttree.getRootVal())
print(ttree.getRightChild().getRootVal())
print(ttree.getLeftChild().getRightChild().getRootVal())
print(ttree.getRightChild().getLeftChild().getRootVal())

# testEqual(ttree.getLeftChild().getRightChild().getRootVal(),'d')
# testEqual(ttree.getRightChild().getLeftChild().getRootVal(),'e')
