class dsu:
    def __init__(self):
        self.parent = list(range(1000))
        self.count = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):

        px, py = self.find(x), self.find(y)
        if px == py:
            return 0
        if px != py:
            self.parent[px] = py
            return 1


class Solution(object):
    def makeConnected(self, n: int, connections) -> int:
        N = len(connections)
        du = dsu()

        for x, y in connections:
            print(x, y)
            m = du.union(x, y)
            n -= m

        return n

s = Solution()
print(s.makeConnected(4,[[0,1],[0,2],[1,2]]))









