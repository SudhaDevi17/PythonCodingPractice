class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.l.append(x)


    def pop(self):
        """
        :rtype: int
        """
        return self.l.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]


    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.l)


    def popMax(self):
        """
        :rtype: int
        """
        self.l = self.l[::-1]
        max_num = self.l.pop(self.l.index(max(self.l)))
        self.l = self.l[::-1]
        return max_num
# Your MaxStack object will be instantiated and called as such:
obj = MaxStack()
obj.push(5)
obj.push(1)
param_5 = obj.popMax()

param_4 = obj.peekMax()
