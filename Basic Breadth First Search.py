graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def bfs(graph, start ):
    queue = []
    queue.append(start)
    visited = set()
    visited_list =[]
    while queue:
        curr = queue.pop(0)
        print(curr)
        visited.update(curr)
        visited_list.append(curr)

        for item in graph[curr]:
            if item not in visited:
                queue.append(item)

    print(visited_list)

bfs(graph , 'A')


