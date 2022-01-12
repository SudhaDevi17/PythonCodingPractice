class Solution:

    def findCircleNum(self, M):
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            parents[find(x)] = find(y)

        n = len(M)
        parents = list(range(n))# it will have [0,1,2] to compare so [1,1] is not considered
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j]:
                    union(i, j)
        circle = set(find(i) for i in range(n))
        print(circle)
        return len(circle)

s= Solution()
print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))