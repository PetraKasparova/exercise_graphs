#V = {P1, P2, P3, P4, P5}
#E = {{P1, P2}, {P1, P3}, {P2, P3}, {P3, P4}, {P4, P5}}
#TASK1
edges = [("P1", "P2"),("P1", "P3"),("P2", "P3"),("P3", "P4"),("P4", "P5")]

def build_adjacency_list(edges, directed=False):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

graph = build_adjacency_list(edges)
#print(graph)
#print(build_adjacency_list(edges, True))
#print(build_adjacency_list(edges, False))

#graph_finished = build_adjacency_list(edges, True)

def degrees(graph):
    result_degrees = {}
    for vertex in graph:
        result_degrees[vertex] = len(graph[vertex])
    return result_degrees
#print(degrees(graph))

def in_out_degree(graph):
    in_degree = {}
    out_degree = {}
    for vertex in graph:
        in_degree[vertex] = 0
        out_degree[vertex] = len(graph[vertex])
    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor not in out_degree:
                out_degree[neighbor] += 1
    return in_degree, out_degree

print(in_out_degree(graph))


#TASK3
def dfs(graph, start):
    visited = set()
    order = []
    for neighbor in sorted(graph[start]):
        if neighbor not in visited:
            visited.add(neighbor)
            order.append(neighbor)
    return order

print(dfs(graph, "P1"))

def connected_components(graph):
    visited = set()
    components = []

