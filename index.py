
#   a             a
#  / \  ==>      / \
# b   c         c   b


def showBinaryTree(head, level=0):
    current = head
    print(level,' - ',current.value)

    if(current.left != None):
        showBinaryTree(current.left, level+1)

    if(current.right != None):
        showBinaryTree(current.right, level+1)

def invertBinaryTree(head):
    if(head == None):
        return

    auxNode = head.right
    head.right = head.left
    head.left = auxNode

    invertBinaryTree(head.left)
    invertBinaryTree(head.right)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BinaryTree(10)
a0 = BinaryTree(2)
a1 = BinaryTree(3)
b0 = BinaryTree(4)
b1 = BinaryTree(5)
b2 = BinaryTree(215)
b3 = BinaryTree(53)

root.left = a0
root.right = a1
a0.left = b0
a0.right = b1
a1.left = b2
a1.right = b3

showBinaryTree(root)
print()
invertBinaryTree(root)
showBinaryTree(root)