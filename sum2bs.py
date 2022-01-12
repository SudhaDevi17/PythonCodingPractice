def twoSum( numbers, target):
    n = len(numbers)

    for index in range(n):

        T = target - numbers[index]

        l, r = index + 1, n

        while l <r:

            mid = (l + r) // 2

            if numbers[mid] == T:
                return [index + 1, mid + 1]

            elif numbers[mid] < T:
                l = mid + 1

            elif numbers[mid] > T:
                r = mid - 1

    return [index + 1, mid]



print(twoSum([5,25,75], 100 ))
#print(twoSum([1,2,3,4,4,9,56,90], 8 ))
#print(twoSum([2,7,11,15],9))

