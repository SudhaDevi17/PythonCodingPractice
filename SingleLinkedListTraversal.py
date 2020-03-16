class Node:
    def __init__(self , val ):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    def displaylist(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next
    def insertbeginning(self, newval):
        newnode = Node(newval)
        if self.head is None:
            self.head = newnode
        else:

            newnode.next = self.head
            self.head = newnode



element1 = Node(1)
element2 = Node(2)
element3 = Node(3)

linkedlist = SingleLinkedList()
linkedlist.head = element1
linkedlist.head.next = element2
element2.next = element3

# test if new node got inserted in the beginning
element4 = 0
linkedlist.insertbeginning(element4)

linkedlist.displaylist()
