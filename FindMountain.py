class Solution:
    def validMountainArray(self, A):
        if len(A) <= 2:
            return False

        # findmaxindex
        def findmaxindex(A):
            for i in range(len(A)):
                if A[i] == max(A):
                    return i

        # findthe left right arr
        def findmiddle(A, middleindex):
            left = A[:middleindex]
            right = A[middleindex:]
            print(left, right)
            if A[middleindex] == A[len(A) - 1] or A[middleindex] == A[0]:
                return False

            return True

        for i in range(len(A)):
            from collections import Counter
            uni = len(list(Counter(A).keys()))
            if uni < 3:
                return False
            else:
                midindex = findmaxindex(A)
                print(findmiddle(A, midindex))
                return findmiddle(A, midindex)
A = [1,3,2 ]
s = Solution()
s.validMountainArray(A)




