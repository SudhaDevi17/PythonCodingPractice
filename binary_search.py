
def searchRange( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ## handle corner cases
    n = len(nums)
    if n<1:
        return [-1,-1]

    def binary(nums , target):
        l , r = 0 , len(nums)-1

        while l<r:

            mid = (l+r-1)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid +1
            elif nums[mid]> target:
                r = mid -1

        if nums[-1]==target:
            return len(nums) -1
        else :
            return -1

    l_idx = binary(nums, target)
    print(l_idx)

    # handle 1 length
    if l_idx==0 and n==1:
        return [0,0]

    # temp = l_idx
    # r_idx =-1
    #
    # if l_idx!=-1 :
    #     # begin searching
    #     while l_idx<=(n-1):
    #         if (nums[l_idx]==target):
    #             r_idx = l_idx
    #             l_idx+=1
    #             #r_idx = l_idx
    # else:
    #     return [-1,-1]
    # return [temp, r_idx]

print(searchRange([1,2,3,3,3,3,4,5,9],3))

## fix comments
# recursive approach should be followed -
# Since there are duplicates now splitting by mid point doesn't work.
# We should solve for sub plms - recursive solution can solve left anad right and return the minimum max index of matching values