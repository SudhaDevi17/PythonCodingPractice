# Python program to print all permutations with
# duplicates allowed
res = set()
def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
	if l==r:
		res.add(( toString(a) ))
	else:
		for i in range(l,r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function
string = "A"+"B"
n = len(string)
a = list(string)

permute(a, 0, n-1)
print("The winning chances are ", len(res)+1, res)
# This code is contributed by Bhavya Jain
