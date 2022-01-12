
def searchInsert(nums,target):

    l, r = 0, len(nums) - 1

    while l < r:

        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            r = mid
        elif nums[mid] < target:
            l = mid + 1

    print(l, r, mid)

    if nums[r]<target:
        return r +1
    elif nums[r]>target:
        return r

    if l==r and l==0:
        return 0

#nums , target = [1,3,5,6], 7
nums , target = [1,3], 0
print(searchInsert(nums, target))