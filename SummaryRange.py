def SummaryRange(self, nums):
    ranges = []
    for n in nums:
        if not ranges or n> ranges[-1][-1]+1 :
            ranges+=[]
        ranges[-1][1:] = n

    print("ranges list value are" , ranges)

    print('->'.join(map(str , r)) for r in ranges)