class Solution(object):
    def countSteppingNumbers(self, low, high):
        ans = set()
        def search(x):
            if x > high: return
            if x >= low: ans.add(x)
            last = x % 10
            for d in (last-1, last+1):
                if 0 <= d < 10:
                    search(10 * x + d)
        for d in range(10): search(d)
        return sorted(ans)

s = Solution()
print(s.countSteppingNumbers(0,21))