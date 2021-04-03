def showLinkedList(head):
    current = head
    print(current.value)

    while(current.next != None):
        current = current.next
        print(current.value)


def reverseNode(current, nextNode):
    nextNextNode = nextNode.next
    nextNode.next = current

    current = nextNode
    nextNode = nextNextNode

    return (current, nextNode)


def reverseSequentNodes(current, nextNode):
    if(current != None):
        if(current.next != None):
            nodeTuple = reverseNode(current, current.next)
            current = nodeTuple[0]
            nextNode = nodeTuple[1]
            return reverseSequentNodes(current, current.next)

    return current

def reverseLinkedList(head):
    current = head
    
    newRoot = reverseSequentNodes(current, current.next)

    current.next = None

    return newRoot

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = LinkedList(10)
node2 = LinkedList(2)
node3 = LinkedList(3)
node4 = LinkedList(4)
node5 = LinkedList(5)
node6 = LinkedList(215)
node7 = LinkedList(53)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

showLinkedList(node1)
print()
node = reverseLinkedList(node1)
showLinkedList(node)