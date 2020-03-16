class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
def printlist(head):
    while head:
        print(head.val)
        head = head.next
class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        print("\n Found mid noded" , printlist(slow) , printlist(fast ))
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        print("\n After reversing the second half :" , printlist(slow) , printlist(node))
        print("\n To compare the two nodes :", printlist(node), printlist(head))
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next

        return True
l = ListNode(1, ListNode(1, ListNode(2, ListNode(1, ListNode(5 , ListNode(7 , ListNode(1 , None)))))))
s = Solution()
print(s.isPalindrome(l))