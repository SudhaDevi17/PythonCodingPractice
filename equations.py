import collections

## UNION FIND SOLUTION
# class Solution:
#     def equationsPossible(self, equations):
#         graph = collections.defaultdict(list)
#         nonmatch = set()
#
#         for eq in equations:
#             v1 = eq[0]
#             v2 = eq[-1]
#
#             sign = eq[1:3]
#
#             if sign == '==':
#                 graph[v1].append(v2)
#                 graph[v2].append(v1)
#             else:
#                 nonmatch.add((v1, v2))
#
#         parent = dict()
#
#         def find(x):
#             parent.setdefault(x, x)
#             if x != parent[x]:
#                 parent[x] = find(parent[x])
#             return parent[x]
#
#         def union(x, y):
#             px = find(x)
#             py = find(y)
#             if px != py:
#                 parent[px] = py
#
#         for key, val in graph.items():
#             px = find(key)
#             for y in val:
#                 py = find(y)
#                 if px != py:
#                     union(key, y)
#
#         for x, y in nonmatch:
#             px = find(x)
#             py = find(y)
#             if px == py:
#                 return False
#         return True
# DFS SOLUTION
# class Solution(object):
#     def equationsPossible(self, equations):
#         graph = [[] for _ in range(26)]
#
#         for eqn in equations:
#             if eqn[1] == '=':
#                 x = ord(eqn[0]) - ord('a')
#                 y = ord(eqn[3]) - ord('a')
#                 graph[x].append(y)
#                 graph[y].append(x)
#
#         color = [None] * 26
#         t = 0
#         for start in range(26):
#             if color[start] is None:
#                 t += 1
#                 stack = [start]
#                 while stack:
#                     node = stack.pop()
#                     # why are we poppping upto 26 integers. Ugh!
#                     for nei in graph[node]:
#                         if color[nei] is None:
#                             color[nei] = t
#                             stack.append(nei)
#
#         for eqn in equations:
#             if eqn[1] == '!':
#                 # dont know  what is happening here with this ord(a) and eqn[0] , eqn[3]
#                 x = ord(eqn[0]) - ord('a')
#                 y = ord(eqn[3]) - ord('a')
#                 if x == y: return False # lee
#                 if color[x] is not None and color[x] == color[y]:
#                     return False
#         return True
# s = Solution()
# print(s.equationsPossible(["a==b", "b!=a"]))
#
#

# self practice
from collections import defaultdict
class Solution:
    def equations_solver(self, equations):

        graph = defaultdict(list)
        nonmatches = set()
        parents = dict()

        # create a graph
        for eqn in equations:
            left, right = eqn[0], eqn[-1]
            if '==' in eqn:
                graph[left].append(left)
                graph[right].append(right)
            else:
                nonmatches.add((left, right))
        # def find
        def find(x):
            parents.setdefault(x,x)
            if parents[x]!=x:
                parents[x] = find(parents[x])
            return x

        # def union
        def union(a ,b ):
            px = find(a)
            py = find(b)
            if px!=py:
                parents[px] = py
        # do the union operations
        for key,val in graph.items():
            px = find(key)
            for y in val:
                py = find(y)
                if px!=py:
                    union(key , y )


        # find the mismatch pairs
        for key,val in nonmatches:
            px = find(key)
            py = find(val)
            if px!=py:
                return False
        return  True


s = Solution()
print(s.equations_solver(['a==b', 'b==c', 'c==a']))

# create test cases
#["a==b","b!=a"]

# learnings
# lookup of key before its created in find should be avoided
# we can set default vlue in dict
# we can save tuple in set
# we merge the parents of y into parents of x
# start solving from small plms, accomodate the corner cases as you grow the solution


