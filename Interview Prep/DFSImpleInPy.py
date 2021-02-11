"""
DFS(graph traversal technique) imple in python
"""
adjlist = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["B","F"],
    "D":[],
    "E":["F"],
    "F":[]
}
color = {}
trav_time = {}
parent = {}
dfs = []

for val in adjlist.keys():
    color[val] = "W" # W G B to identify notvisited, partial, fully
    parent[val] = None
    trav_time[val] = [-1,-1]

time = 0
#result = []
def DFS(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs.append(u)    

    for val in adjlist[u]:
        if color[val] == "W":
            color[val] = "G"
            parent[val] = u
            DFS(val)
    color[u] = "B"
    trav_time[u][1] = time
    time += 1

DFS("A")
dfs.reverse()
print(dfs)
#print(parent)
#print(trav_time)

