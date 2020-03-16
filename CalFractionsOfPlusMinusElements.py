import  math

def plusMinus(arr):
    n = len(arr)
    lower = fractions(len([i for i in arr if i < 0  ]), n )
    middle = fractions(len([i for i in arr if i==0]) , n )
    upper = fractions(len([ i for i in arr if i > 0]), n)

    print(lower)
    print(middle)
    print(upper)

def fractions(a,b):
    result=  format(a/b , ".6f")
    return(result)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int , input().rstrip().split()))
    print(arr)
    #print(fractions(3,4))
    plusMinus(arr)

