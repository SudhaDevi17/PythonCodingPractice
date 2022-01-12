

def search( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            if nums[mid] > target and nums[l] <= target:
                r = mid - 1
            else:
                l = mid + 1

        else:
            if nums[mid] < target and nums[r] >= target:
                l = mid + 1
            else:
                r = mid - 1
    return -1
#print(search([4,5,6,7,0,1,2], 0))
#print(search([4,5,6,7,0,1,2], 3))
#print(search([1],0))
print(search([4,5,6,7,8,1,2,3], 8))
