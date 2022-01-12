accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

# motivation - watch a simple idea become code
class Solution:
    def accountsMerge(self, accounts):

        # build graph
        from collections import defaultdict
        names_dict = {}
        graphs = defaultdict(list)
        for ind , account_list in enumerate(accounts):
            print(account_list)

            #print(index, val)
            key = 'acct' + str(ind)
            for index, val in enumerate(account_list):

                if index == 0:
                    names_dict[key] = val
                else:
                    graphs[key].append(val)

        # find
        def find(x):
            if x!= parents[x]:
                parents[x] = x

            return parents[x ]

        # union
        def union(key , emails):
            pass

        parents = defaultdict(list)
        # populate the parents
        for key,val in enumerate(graphs):

            for index, emails in enumerate(graphs[val]):
                parents[emails] = val






s = Solution()
s.accountsMerge(accounts)