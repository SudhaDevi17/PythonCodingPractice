import collections
class Solution(object):
    def minimumMoves(self, A):
        N = len(A)  # N>= 2
        R = C = N

        def neighbors(r, c, dire):
            # movement:
            if dire == RIGHT:  # occing r,c and r,c+1
                # slide right
                if c + 2 < N and A[r][c + 2] == 0:
                    yield r, c + 1, dire
                # slide down
                if r + 1 < N and A[r + 1][c] == 0 and A[r + 1][c + 1] == 0:
                    yield r + 1, c, dire

                # turn down
                if r + 1 < N and A[r + 1][c] == A[r + 1][c + 1] == 0:
                    yield r, c, dire ^ 1
            else:  # down - occing r,c and r+1, c
                # slide right
                if c + 1 < N and A[r][c + 1] == A[r + 1][c + 1] == 0:
                    yield r, c + 1, dire
                # slide down
                if r + 2 < N and A[r + 2][c] == 0:
                    yield r + 1, c, dire
                # turn up
                if c + 1 < N and A[r][c + 1] == A[r + 1][c + 1] == 0:
                    yield r, c, dire ^ 1

        RIGHT, DOWN = 0, 1
        Q = collections.deque([(0, 0, RIGHT, 0)])
        seen = {(0, 0, RIGHT)}
        while Q:
            r, c, dire, d = Q.popleft()
            if r == N - 1 and c == N - 2 and dire == RIGHT:
                return d
            if r == N - 2 and C == N - 1 and dire == DOWN:
                return d
            for nei in neighbors(r, c, dire):
                if nei not in seen:
                    seen.add(nei)
                    Q.append(nei + (d + 1,))
        return -1
