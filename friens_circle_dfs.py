"""
reference:
https://leetcode.com/problems/number-of-provinces/discuss/201096/Pythonthe-classic-DFS-super-easy-to-understand-comments-the-whole-shabang!
"""

import  collections
class Solution:
    def findCircleNum(self, M):
        """
        The intuition here is to loop through each friend,
        and count the number of circles. We use DFS to ensure
        we count each circle once.
        """

        # define variables
        graph = collections.defaultdict(set)
        seen = set()
        result = 0

        # create graph
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    graph[i].add(j)

        # create dfs function
        def dfs(node):
            if node not in seen:
                seen.add(node)
                for i in graph[node]:
                    dfs(i)

        # find circles
        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                result += 1

        # return result
        return result
M=[[1,1,0], [1,1,0],[0,0,1]]
s = Solution()
print(s.findCircleNum(M))