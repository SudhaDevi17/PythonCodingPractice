def mincoin(n, coins, t):
    if t == 0:
        return 1

    if n == 0:
        return 0

    res = mincoin(n - 1, coins, t)
    if coins[n - 1] <= t:
        res += mincoin(n, coins, t - coins[n - 1])
    return res


print(mincoin(3, [1, 2, 3], 4))