"""\
# Created a simple Single Linked List
"""

class Node:
    def __init__(self , data ):
        self.data = data
        self.next  = None

class SingleLinkedList:
    def __init__(self):
        self.head  = None

element1 = Node(1)
element2 = Node(2)
element3 = Node(3)

linkedlist = SingleLinkedList()
linkedlist.head = element1
linkedlist.head.next = element2
element2.next = element3


print(linkedlist.head.val)
print(linkedlist.head.next.val)
print(linkedlist.head.next.next.val)
#print(linkedlist.head.next.next.next.val)
