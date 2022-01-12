class Solution:

    def redundant_conn(self, egdes):

        seen = {}
        graph = set()

        # build the graph
        for edge in egdes :
            u,v = edge
            # add to seen?
            graph[u].add(v)

        # dfs traverse the graph
        def dfs(graph):

            for node in graph:
                if node not in seen:
                    seen.add(node)
                    for vertex in graph[node]:
                        dfs(vertex)
                else:
                    return node








