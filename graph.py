from pprint import pprint
from collections import deque
def BFS(graph , source):
    Min_Distance = {source:0}
    Parent_Tree = {source:None}
    l_prev = deque([source])
    l_current = deque()
    current_distance = 1
    while l_prev:
        for u in l_prev:
            for v in graph[u]:
                if v in Parent_Tree:
                    continue
                l_current.append(v)
                Min_Distance[v] = current_distance
                Parent_Tree[v] = u
        current_distance += 1
        l_prev = l_current
        l_current = deque()

    for v in graph:
        if v not in Min_Distance:
            Min_Distance[v] = float("inf")

    return {
        "parent_tree" : Parent_Tree,
        "distances" : Min_Distance,
        
    }

def dfs(Adj, s, parent = None, order = None):        # Adj: adjacency list, s: start
    if parent is None:                               # O(1) initialize parent list
        parent = [None for v in Adj]                 # O(V) (use hash if unlabeled)
        parent[s] = s                                # O(1) root
        order = []                                   # O(1) initialize order array
    for v in Adj[s]:                                 # O(Adj[s]) loop over neighbors
        if parent[v] is None:                        # O(1) parent not yet assigned
            parent[v] = s                            # O(1) assign parent
            dfs(Adj, v, parent, order)               # Recursive call
    order.append(s)                                  # O(1) amortized
    return parent, order

def full_dfs(Adj):                                   # Adj: adjacency list
    parent = [None for v in Adj]                     # O(V) (use hash if unlabeled)
    order = []                                       # O(1) initialize order list
    for v in range(len(Adj)):                        # O(V) loop over vertices
        if parent[v] is None:                        # O(1) parent not yet assigned
            parent[v] = v                            # O(1) assign self as parent (a root)
            dfs(Adj, v, parent, order)               # DFS from v (BFS can also be used)
    return parent, order

def DFS(graph , source):
    P = {source:None}
    order = []
    
    def visit(s):
        for v in graph[s]:
            if v not in P:
                P[v] = s
                visit(v)
        order.append(s)

    visit(source)
    return P , order

def Shortest_path_Tree(source , graph , weights , short_paths):
    # init pt and s -> None
    pt = {
        source: None
    }
    finite_short_paths = {x:short_paths[x] for x in short_paths if float("-inf") < short_paths[x] < float("inf")}
  
    for u in finite_short_paths:
        for v in graph[u]:
            if v not in pt and finite_short_paths[v] == finite_short_paths[u] + weights[(u,v)]:
                pt[v] = u

def DAG_Relaxation(graph , source):
    d = {vertex:float("inf") for vertex in graph}
    d[source] = 0
    _ , order = DFS(graph , source)
    order.reverse()
    for u in order:
        for v in graph[u]:
            if d[v] > d[u] + graph[u][v]: d[v] = d[u] + graph[u][v]
    return d

def bellman_ford(graph , source): #under process
    #prune the graph  and make a super node
    #               super ---(0 or inf)--- reachable nodes (0,x) ---w(x,y)--- adj of nodes x (1,y)
    _ , order = DFS(graph , source)
    graphh= {(0,x):{(1,y):graph[x][y] for y in graph[x]}|{(1,x):0} for x in order} | {(1,x):{} for x in order}# crazy idea!!
    graphh["super"] = {(0,x):0 if x == source else float("inf") for x in order}

    pprint(graphh)
    print("\n\n")

    #run dag now from super node
    for _ in range(len(order)):
        d = DAG_Relaxation(graphh , "super")
        graphh["super"] = {(0,x):d[(1,x)] for x in order}
        pprint(graphh)
        print("\n\n")
        pprint(d)
        print("\n\n")

    pprint(graphh)
    print("\n\n")
    pprint(d)

    shortest_distance = {x:d[(0,x)] if (0,x) in d else float("inf") for x in graph}

    new_graph = graph.copy()
    new_graph["super"] = {u:0 for u in order if d[(1,u)] < d[(0,u)]}
    _,rfw = DFS(new_graph , "super")
    for u in rfw:
        shortest_distance[u] = float("-inf")
  
    return shortest_distance
        

def bellman_ford_mit(Adj, s):                               # Adj: adjacency list, w: weights, s: start
    # initialization
    infinity = float('inf')                                 # number greater than sum of all + weights
    d = [infinity for _ in Adj]                             # shortest path estimates d(s, v)
    parent = [None for _ in Adj]                            # initialize parent pointers
    d[s], parent[s] = 0, s                                  # initialize source
    # construct shortest paths in rounds
    V = len(Adj)                                            # number of vertices
    for _ in range(V - 1):                                  # relax all edges in (V - 1) rounds
        for u in range(V):                                  # loop over all edges (u, v)
            for v in Adj[u]:                                # relax edge from u to v
                if d[v] > d[u] + Adj[u][v]:
                    d[v] = d[u] + Adj[u][v]
                    parent[v] = u
    # check for negative weight cycles accessible from s
    for u in range(V):                                      # Loop over all edges (u, v)
        for v in Adj[u]:
            if d[v] > d[u] + Adj[u][v]:                     # If edge relax-able, report cycle
                raise Exception("Ack! There is a negative weight cycle!")
    return d, parent

import heapq
def dijkstra(graph , source): #working
    h = [(0,source)]
    dist = {v:0 if v == source else float("inf") for v in graph}
    while h:
        d , u = heapq.heappop(h)
        if d > dist[u]: continue
        for v in graph[u]:
            if dist[v] > d + graph[u][v]:
                dist[v] = d + graph[u][v]
                heapq.heappush(h, (dist[v] , v))
    return dist



def johnson(graph):
    gx = graph.copy()
    gx["x"] = {vertex: 0 for vertex in graph}
    dx , _ = bellman_ford_mit(graph , "x") #abort when find NWC

    gx = {x:{y:graph[x][y] + dx[x] - dx[y] for y in graph[x]} for x in graph}

    apsp = {v:None for v in graph}
    for v in graph:
        dis = dijkstra(gx , v)
        apsp[v] = {vertex:dis[vertex] - dx[v] + dx[vertex] for vertex in dis}

    return apsp




def main():
    graph = {
        0: {1:-5 ,2:6},
        1: {2:-4},
        2: {3:3},
        3: {1:-1},

    }
    pprint(bellman_ford(graph,0))
if __name__ == "__main__":
    main()