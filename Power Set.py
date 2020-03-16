class Solution(object):

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

s = Solution()
print(s.subsets([1 ,2]))