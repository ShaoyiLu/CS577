import re
from collections import deque

def bfs(graph, source, target, parent):
    queue = deque()
    queue.append(source)
    parent[source] = -1
    while queue:
        u = queue.popleft()
        for v in range(len(graph)):
            if parent[v] == -1 and graph[u][v] > 0:
                parent[v] = u
                queue.append(v)
                if v == target:
                    return True
    return False

def max_flow(graph, source, target):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, target, parent):
        path_flow = float('inf')
        s = target
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = target
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
        parent = [-1] * len(graph)
    return max_flow

def bipartite_matching(m, n, edges):
    graph = [[0] * (m+n+2) for _ in range(m+n+2)]
    source = 0
    target = m+n+1
    for i in range(1, m+1):
        graph[source][i] = 1
    for j in range(m+1, m+n+1):
        graph[j][target] = 1
    for i, j in edges:
        graph[i][j+m] = 1
    max_matching = max_flow(graph, source, target)
    if max_matching == m and m == n:
        perfect_matching = 'Y'
    else:
        perfect_matching = 'N'
    return max_matching, perfect_matching

num_instances = int(input())
for _ in range(num_instances):
    # Read input using regular expressions to handle multiple spaces and leading/trailing spaces
    line = input().strip()
    m, n, q = map(int, re.split(r'\s+', line))
    edges = []
    for _ in range(q):
        line = input().strip()
        i, j = map(int, re.split(r'\s+', line))
        edges.append((i, j))
    max_matching, perfect_matching = bipartite_matching(m, n, edges)
    print(max_matching, perfect_matching)
