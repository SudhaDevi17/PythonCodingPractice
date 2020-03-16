class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def displayNodes(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    def RemoveNodeInBetween(self , middleNode ):
        if middleNode is None :
            return "middle node cannot be Empty"
        node =self.head
        while node:
            if node.next.val == middleNode.val:
                node.next = node.next.next
                break
            else:
                print(node.val)
                node = node.next
        self.head = node


    def RemoveDuplicates(self):
        node = self.head
        if node:
            values = {node.val : True}
            while node.next:
                if node.next.val in values:
                    print("node.next.val: ", node.next.val, "values: ", values)
                    node.next = node.next.next
                    print(node.val)
                else:
                    values[node.next.val] = True
                    node = node.next

        return self.head

element1 = Node(1)
element2 = Node(2)
element3 = Node(3)
element4 = Node(2)
element5 = Node(2)

linkedlist = SingleLinkedList()
linkedlist.head = element1
linkedlist.head.next = element2
element2.next = element3
element3.next = element4
element4.next = element5
linkedlist.displayNodes()


# remove node 2
print("remove node2 ")
#linkedlist.RemoveNodeInBetween(element2 )
#linkedlist.displayNodes()
outlink = linkedlist.RemoveDuplicates()
#linkedlist.displayNodes()
while outlink.next:
    print(outlink.val)
    outlink= outlink.next