def tripleStep1(n):
    a , b = 1, 2
    if n==1 :
        return a
    res = [ 0 for i in range(n)]
    res[0] , res[1] = 1 , 2
    for i in range(2, n):
        res[i] = res[i-1] + res[i-2]

    return res[-1]

print(tripleStep1(4))

def tripStep2(n):
    if n ==1 :
        return 1
    a , b = 1, 2
    for i in range(2 , n):
        temp = b
        b = a+b
        a = temp
    return b
print(tripStep2(4))

def tripleStep3(n):
    ways = 0
    if n == 1 :
        return 1
    if n==2 :
        return 2

    ways+= tripleStep3(n-1) + tripleStep3(n-2)
    return ways
print(tripleStep3(4))

def tripleStep4(n):
    dic = {1:1 , 2:2 }
    if n not in dic:
        dic[n] = tripleStep4(n-2) + tripleStep4(n-1)
    return dic[n]
print(tripleStep4(4))