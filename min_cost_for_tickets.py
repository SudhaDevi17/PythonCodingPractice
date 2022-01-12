from functools import  lru_cache

class Solution:
    def minCost(self, days, costs):

        N = len(days)
        durations = [1,7,30]

        @lru_cache(None )


        def dp(i): # i means index start
            """
            :param i: a function to get the next index for current cost-duration combo
            :return: returns the minimum cost so far
            """
            if i>=N:
                return 0

            ans = float('inf')
            j= i # j will be used to get end of index i based on duration 1,7,30
            for c,dur in zip(costs , durations):
                while j<N and days[j]< days[i]+ dur:
                    j+=1
                ans = min(ans, dp(j)+c)

            return ans

        return dp(0)

s = Solution()
print(s.minCost([1,4,6,7,8,20] , [2,7,15]))