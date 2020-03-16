class MinOfStack():
    def __init__(self):
        self.top , self._min = None , None

    def min(self):
        if not self._min:
            return None
        return self._min.data

    def push(self , item ):
        if self._min and item> self._min.data:
            self._min =Node(self._min.data , self._min)
        else:
            self._min=  Node(item , self._min)
        self.top = Node(item  , self.top )
    def pop(self):
        if not self.top:
            return None
        item = self.top.data
        self.top = self.top.next
        self._min = self._min.next
        return item
class Node():
    def __init__(self, data = None, next = None):
        self.data , self.next = data , next
    def __str__(self):
        string  = str(self.data)
        if self.next :
            string+=','+str(self.next)
        return string
import unittest
class Test(unittest.TestCase):
    def testNode(self):
        Node1 = Node(1)
        minstack = MinOfStack()
        self.assertEqual(minstack.min() , None)
        minstack.push(7)
        self.assertEqual(minstack.min() , 7)
        minstack.push(1)
        self.assertEqual(minstack.min() , 1)
if __name__ =="__main__":
    unittest.main()

