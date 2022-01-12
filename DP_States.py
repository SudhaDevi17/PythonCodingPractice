# This function returns the number of
# arrangements to form 'n'

# lookup dictionary/hashmap is initialized
def solve(n, lookup={}):
    # Base cases
    # negative number can't be
    # produced, return 0
    if n < 0:
        return 0

    # 0 can be produced by not
    # taking any number whereas
    # 1 can be produced by just taking 1
    if n == 0:
        return 1

    # Checking if number of way for
    # producing n is already calculated
    # or not if calculated, return that,
    # otherwise calulcate and then return
    if n not in lookup:
        lookup[n] = (solve(n - 1) +
                     solve(n - 3) +
                     solve(n - 5))

    return lookup[n]

print(solve(6))