
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head):
        dummy = pre = Node(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                head = head.next
                pre.next = head
                print("if true " , pre.next.val, head.val)
            else:
                pre = pre.next
                head = head.next
                print("else true " , pre.val, head.val)

        return dummy.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(3)
head.next.next.next.next = Node(4)
s = Solution()
newhead = s.deleteDuplicates(head)
while newhead:
    print(newhead.val)
    newhead = newhead.next