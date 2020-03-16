class QueueViaStacks():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def add(self, item ):
        self.in_stack.push(item)
    def remove(self):
        if not len(self.out_stack):
            while len(self.in_stack):
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()


class Stack():
    def __init__(self):
        self.array = []
    def __len__(self):
        return len(self.array)
    def push(self, item ):
        self.array.append(item)
    def pop(self ):
        if not len(self.array):
            return None
        return self.array.pop()

import unittest
class Test(unittest.TestCase):
    def test_queue(self):
        qs = QueueViaStacks()
        qs.add(1)
        qs.add(2)
        qs.add(3)
        self.assertEqual(qs.remove() , 1)
