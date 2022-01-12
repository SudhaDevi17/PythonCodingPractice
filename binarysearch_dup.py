def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:

        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1

    return -1

nums, target = [5,7,7,8,8,10], 8
# l_idx = binary_search(nums, target)
# print(l_idx)
#print(binary_search([], 1))
print(binary_search([2,2], 2))

