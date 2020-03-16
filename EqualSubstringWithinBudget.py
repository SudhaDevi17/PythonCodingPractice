#Get Equal Substrings Within Budget.
#You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.
#You are also given an integer maxCost.
#Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.
#If there is no substring from s that can be changed to its corresponding substring from t, return 0.
# ref  ;  https://leetcode.com/contest/weekly-contest-156/problems/get-equal-substrings-within-budget
class Solution(object):
    def equalSubstring(self, S, T, maxCost):
        N = len(S)
        A = [abs(ord(S[i]) - ord(T[i])) for i in  range(N)]
        left = 0
        windowsum = 0
        ans = 0
        for right, x in enumerate(A):
            windowsum += x
            while windowsum > maxCost and left < N:
                windowsum -= A[left]
                left += 1
            cand = right - left + 1   # only count the forward moves, left is wen u go back and adjust the currCost acc to maxCost
            if cand > ans: ans = cand
        return ans
s = Solution()
print(s.equalSubstring("pxezla", "loewbi",25))