from collections import defaultdict

class Graph:
    def __init__(self, num_v):
        self.num_v = num_v
        self.edge = defaultdict(list)

    def add_edge(self, u , v ):
        self.edge[u].append(v)

class Parent:
    def __init__(self, parent , rank):
        self.parent = parent
        self.rank = rank

def find(parents , node ):
    if parents[node].parent!= node:
        parents[node].parent = find(parents, parents[node].parent)
    return parents[node].parent

def union(parents, u , v ):

    if parents[u].rank > parents[v].rank:
        parents[v].parent= u
        parents[u].rank +=1
    elif parents[v].rank > parents[u].rank:
        parents[u].parent = v
        parents[v].rank +=1
    else:
        parents[v].parent= u
        parents[v].rank +=1

def isCycle(graph):
    parents = []

    # create parents list
    for v in range(graph.num_v):
        parents.append(Parent(v,0))

    for u in graph.edge:
        rep_u = find(parents , u)

        for v in graph.edge[u]:
            rep_v = find(parents, v )

            if rep_u == rep_v:
                return True

            else:
                union(parents , u , v )

g = Graph(3)

g.add_edge(0,1 )
g.add_edge(1,2)
g.add_edge(0,2)

if isCycle(g):
    print("there is cycle here")

else:
    print("There  is no cycle in the graph")







