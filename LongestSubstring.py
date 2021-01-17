class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            if s=='':
                return 1
            return len(s)

        slow, fast = 0, 1
        temp = ''
        n = len(s)
        seen = []
        while fast < n:

            if s[slow] not in temp:
                temp = temp + s[slow]

            # flip fast,slow if duplicate found
            if s[fast] in temp:
                # temp += s[slow]
                seen.append(temp)
                temp = ''
            slow = fast
            fast = slow + 1

            if fast == n :
                if s[slow] not in temp:
                    temp += s[slow]
                    seen.append(temp)


        curr = ''
        for s in seen:
            if len(s) > len(curr):
                curr = s
        return len(curr)

s = Solution()
print(s.lengthOfLongestSubstring('assdfdgfghghhadf'))