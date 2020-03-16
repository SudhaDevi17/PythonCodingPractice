# Problem statement explanation : https://www.youtube.com/watch?v=OrS7PaJ-5ck
"""
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

"""

A1 = [[0]*3 for _ in range(  3)]
A1[0][0] = 1


A2 =[[0]*3 for _ in range(3)]
for r,row in enumerate(A1):
    #print(r,row)
    for c,val in enumerate(row):
        #print(c,val)
        for dr, dc in ((2, 1), (2, -1), (-2, 1), (-2, -1),
                       (1, 2), (1, -2), (-1, 2), (-1, -2)):
            if 0 <= r + dr < 3 and 0 <= c + dc < 3:
                #print(r + dr, c + dc)
                A2[r+dr][c+dc]+=val
                print(A2[r+dr][c+dc])

