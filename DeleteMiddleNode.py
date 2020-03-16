class Node():
    def __init__(self, val , next = None ):
        self.val = val
        self.next = next


def getmiddleNode(node):
    slow, fast = node, node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def deletemiddleNode(node):

    todel = getmiddleNode(node)
    print("The middle node is ", todel.val)
    prev = Node(-1)
    prev.next = node
    while node.next.val != todel.val:
        node = node.next
    # delete the middle node here
    node.next.val = node.next.val
    node.next = node.next.next

    return prev.next
head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,None))))))

#print(head.val)
slow = getmiddleNode(head)
print(slow.val)
res = (deletemiddleNode(head))
while res.next:
    print(res.val)
    res = res.next

