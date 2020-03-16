class Solution:
    def myAtoi(self, str: str) -> int:
        nowhite = list(str.strip())
        sign, string, res = nowhite[0], nowhite[1:],0
        sign = -1 if sign[0] =='-' else 1
        for i,c in enumerate(string):
            if c.isdigit():
                res = res*10 + ord(c) - ord('0')
            else:
                return 0
        return max(-2*31 , min(sign*res, 2**31))
s = Solution()
print(s.myAtoi("  -42"))