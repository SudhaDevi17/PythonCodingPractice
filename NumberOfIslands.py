class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid[0]), len(grid)
        numIsland = 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        print(visited)

        def isIsland(r, c):
            print(r, c)
            if r < 0 or c < 0 or r > m or c > n or grid[r][c] == '0' or visited[r][c]:
                return

            visited[r][c] = True
            isIsland(r + 1, c)
            isIsland(r - 1, c)
            isIsland(r, c + 1)
            isIsland(r, c - 1)

        # for indexiing go from 0-3
        for r in range(m - 1):
            for c in range(n - 1):
                if not visited[r][c] and grid[r][c] == '1':
                    isIsland(r, c)
                    numIsland += 1
        return numIsland

