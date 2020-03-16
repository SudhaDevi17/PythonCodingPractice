class Solution(object):
    def compress(self, chars):
        fast = slow = 0
        for curr, c in enumerate(chars):
            if curr + 1 == len(chars) or chars[curr + 1] != c: #if same characters
                chars[slow] = chars[fast]
                slow += 1
                if curr > fast:
                    for digit in str(curr - fast + 1):
                        chars[slow] = digit
                        slow += 1
                fast = curr + 1
        return slow

s  = Solution()
print(s.compress(["a","a","b","b","b","c","c","d","b","b","b","b","b"]))