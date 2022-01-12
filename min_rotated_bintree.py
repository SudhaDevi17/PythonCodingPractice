
def findMin( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if l == mid and mid == r:
            return nums[mid]
        elif nums[mid] > nums[r]:
            l = mid + 1

        elif nums[mid] < nums[r]:
            r = mid

print(findMin([3,4,5,1,2]))
print(findMin([5,1,2,3,4]))
print(findMin([2,1]))
print(findMin([1,2]))