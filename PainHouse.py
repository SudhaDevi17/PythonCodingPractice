class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int

        """
        prev = [0] * 3
        print(prev)
        for now in costs:
            prev = [now[i] + min(prev[:i] + prev[i + 1:]) for i in range(3)]
            print(prev)
        return min(prev)
s = Solution()
s.minCost([[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]])