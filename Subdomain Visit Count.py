import collections
def DomainVisitCount(domains):
    ans  = collections.Counter()
    for domain in domains:
        num , domainstr = domain.split()
        domainlist = domainstr.split('.')
        num = int(num)
        for i in range(len(domainlist)):
            out = '.'.join(domainlist[i:])
            ans['.'.join(domainlist[i:])] = num
            print(ans)

DomainVisitCount(["9001 discuss.leetcode.com"])