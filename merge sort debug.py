def merge_sort(arr):

    if len(arr) > 1:
		#1. Find the middle point to divide the array into two halves:  
        mid = int(len(arr)/2)
		
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

		#2. Call mergeSort for first half 
        merge_sort(lefthalf)
		#3. Call mergeSort for second half
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
		#4. Merge the two halves sorted in step 2 and 3:
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i = i + 1
            else:
                arr[k] = righthalf[j]
                j = j + 1
            k = k + 1
		#Copy the remaining elements 
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j = j + 1
            k = k + 1
#arr = [11,2,5,4,7,6,8,1,23]
arr = [11,2,5,4 ]
merge_sort(arr)
arr