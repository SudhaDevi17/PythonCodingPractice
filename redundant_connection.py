class DisjointSets:

    def __init__(self):
        self.parent = list(range(1001))
        self.rank = [0]*1001

    def find(self, node ):
        if self.parent[node]!= node :
            node = self.find(self.parent[node])
        return node
    def union(self, node_x , node_y ):
        parent_x , parent_y = self.find(node_x), self.find(node_y)

        # if cycle, the parents of both the nodes will be same
        if parent_x == parent_y:
            return False
        elif self.rank[node_x] > self.rank[node_y]:
            self.parent[node_y] = node_x
        elif self.rank[node_y] > self.rank[node_x]:
            self.parent[node_x] = node_y
        else:
            self.parent[node_y] = node_x
            self.rank[node_x]+=1
        return True
class Solution:
    def findRedundantConnection(self, edges):
        ds = DisjointSets()
        for edge in edges :
            if not ds.union(*edge):
                return edge

s = Solution()
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
