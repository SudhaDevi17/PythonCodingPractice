class Solution:
    def maxPoints(self, points):

        cost, row_max = (0, 0), (float('-inf'), 0)

        m, n = len(points), len(points[0])

        for r in range(m):
            row_max = (float('-inf'), 0)

            for c in range(n):

                if r == 0:
                    if points[r][c]>= row_max[0]:
                        row_max = (max(row_max[0], points[r][c]), c)

                else:
                    cost_col = cost[1]
                    val = points[r][c] - abs(cost_col - c)
                    if val > row_max[0]:
                        row_max = (val, c)

            print(row_max)
            cost = ((cost[0] + row_max[0]), row_max[1])
            print(cost)
        return cost[0]


s = Solution()
#s.maxPoints([[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]])
#s.maxPoints([[1,2,3],[1,5,1],[3,1,1]])
#s.maxPoints([[1,5],[2,3],[4,2]])
#s.maxPoints([[2,4,0,5,5],[0,5,4,2,5],[2,0,2,3,1],[3,0,5,5,2]])
#s.maxPoints([[1,5],[3,2],[4,2]])  #11