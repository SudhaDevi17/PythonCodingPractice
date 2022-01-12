class Solution:

    def findFriendCircle(self, M):
        n = len(M)
        seen = set()
        self.friends = 0

        # build graph
        import collections
        graph = collections.defaultdict(set)

        for i in range(n):
            for j in range(n):
                if M[i][j]==1:
                        graph[i].add( j)

        # def dfs
        def dfs(node):

            if node not in seen:
                seen.add(node)
                for i in graph[node]:
                    dfs(i)


        #find circles

        for i in range(n):
            if i not in seen:
                dfs(i)
                self.friends+=1


        return self.friends

s = Solution()
print(s.findFriendCircle([[1,1,0],[1,1,0],[0,0,1]]))

