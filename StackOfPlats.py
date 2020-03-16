class Multistack():
    def __init__(self, capacity = 0 ):
        self.capacity = capacity
        self.stack = []

    def push(self , item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            self.stack.append([item])
    def pop(self):
        if len(self.stack) == 0 : # when there is nothig to pop
            return None

        else:
            return self.stack.pop()

    def popAt(self , atindex ):
        if len(self.stack) == 0 :
            return None
        # when there is invlid atindex / stacknumber ? return None 
        else:
            item = self.stack.pop(atindex )
        return item


import unittest
class test(unittest.TestCase):
    def test_plates(self):
        plates = Multistack(3)
        plates.push(1)
        plates.push(2)
        plates.push(3)
        plates.push(4)
        self.assertEqual(plates.pop() , [4])
        self.assertEqual(plates.popAt(1) , 2)