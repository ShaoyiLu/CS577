from collections import deque

def max_flow(s, t, graph):
    n = len(graph)
    flow = 0
    while True:
        visited = [False] * n
        parent = [-1] * n
        queue = deque()
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.popleft()
            for v, cap in enumerate(graph[u]):
                if not visited[v] and cap > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        if not visited[t]:
            break
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        flow += path_flow
    return flow

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v, cap = map(int, input().split())
        graph[u-1][v-1] += cap
        graph[v-1][u-1] += 0 # backward edge
    print(max_flow(0, n-1, graph))
