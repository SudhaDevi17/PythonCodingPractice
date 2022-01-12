
def rotate1(nums , k )  :
    """
    Do not return anything, modify nums in-place instead.
    """

    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

print(rotate1([1,5,8,7,9], 2))
