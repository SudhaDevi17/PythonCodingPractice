class Solution(object):
    def removeDuplicates(self, S, K):
        stack = []
        for c in S:
            if not stack:
                stack.append([c, 1])
            elif stack[-1][0] != c:
                stack.append([c, 1])
            elif stack[-1][1] + 1 < K:
                stack[-1][1] += 1
            else:
                stack.pop()

        ans = []
        for c, ct in stack:
            ans.extend([c] * ct)
        return "".join(ans)
s = Solution()
print(s.removeDuplicates("pbbcggttciiippooaais", 2))
