import heapq
def assignBikes(  workers, bikes):
    distances = []  # distances[worker] is tuple of (distance, worker, bike) for each bike
    for i, (x, y) in enumerate(workers):
        distances.append([])
        for j, (x_b, y_b) in enumerate(bikes):
            distance = abs(x - x_b) + abs(y - y_b)
            distances[-1].append((distance, i, j))
        distances[-1].sort(reverse=True)  # reverse so we can pop the smallest distance

    result = [None] * len(workers)
    used_bikes = set()
    queue = [distances[i].pop() for i in range(len(workers))]  # smallest distance for each worker
    heapq.heapify(queue)

    while len(used_bikes) < len(workers):
        _, worker, bike = heapq.heappop(queue)
        if bike not in used_bikes:
            result[worker] = bike
            used_bikes.add(bike)
        else:
            heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike

    return result


print(assignBikes([[0,0],[2,1]],
[[1,2],[3,3]]))