"""
Breadth First Search or BFS for a Graph

Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree (See method 2 of this post). The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array. For simplicity, it is assumed that all vertices are reachable from the starting vertex. 

For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0, we look for all adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don’t mark visited vertices, then 2 will be processed again and it will become a non-terminating process. A Breadth First Traversal of the following graph is 2, 0, 3, 1.
"""
# we can give input as either as adj matrix or adj list 
from queue import Queue
adjlist = {
    "A":["B","D"],
    "B":["C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["F","G"]
}
visited = {}
level = {}
parent = {}
bfs = []
queue = Queue()

for i in adjlist.keys():
    visited[i] = False
    level[i] = -1
    parent[i] = None

snode = "A"
visited[snode] = True
level[snode] = 0
queue.put(snode)

while not queue.empty():
    u = queue.get()
    bfs.append(u)

    for v in adjlist[u]:
        if not visited[v]:
            visited[v] = True
            level[v] = level[u] + 1
            parent[v] = u
            queue.put(v)
print("the bfs :",bfs)
print(level["G"]) # to find the height/ level

# for the path from source node to a given node
 
v = "G"
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(path)
