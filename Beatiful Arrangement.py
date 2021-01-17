
n = 3
arr = [i for i in range(1, n+1)]
visited = []
def dfs(num , arr , temp: list):
    for n in arr:
        if n!=num:
            temp.append(n)


    visited.append(temp)
    print(temp, visited)
    return temp

for  i in arr :
    dfs(i , arr , [i])
