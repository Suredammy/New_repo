def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(
                graph, node, end, path
            )  # Recursive call until the first path is found
            if newpath:
                return newpath
    return None


graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D"],
    "D": ["C"],
    "E": ["F"],
    "F": ["C"],
}

print(find_path(graph, "A", "D"))


def find_all_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


print(find_all_path(graph, "A", "D"))


def find_smallest_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    smallest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_smallest_paths(
                graph, node, end, path
            )  # Recursive call until the first path is found
            if newpath:
                if not smallest or len(newpath) < len(smallest):
                    smallest = newpath
    return smallest


print(find_smallest_paths(graph, "A", "D"))
import itertools
from collections import deque


def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for node in graph[at]:
            if node not in dist:
                dist[node] = [dist[at], node]
                q.append(node)
    ans = dist[end]
    a = list(itertools.chain(*ans))
    return a


print(find_shortest_path(graph, "A", "D"))
