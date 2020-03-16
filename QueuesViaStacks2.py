class QueueViaStacks():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    def add(self, item):
        self.in_stack.push(item)
    def remove(self):
        if not len(self.out_stack):
            while len(self.in_stack):
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

class Stack():
    def __init__(self):
        self.arr = []
    def push(self , item ):
        self.arr.append(item)
    def pop(self):
        if not len(self.arr):
            return None
        return self.arr.pop()
    def __len__(self):
        return len(self.arr)

import unittest
class testcases(unittest.TestCase):
    def testq(self):
        s = QueueViaStacks()
        s.add(1)
        s.add(11)
        s.add(111)
        self.assertEqual(s.remove(), 1)
