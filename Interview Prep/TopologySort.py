"""
Topological Sorting

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

For example, a topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a graph. For example, another topological sorting of the following graph is “4 5 2 3 1 0”. The first vertex in topological sorting is always a vertex with in-degree as 0 (a vertex with no incoming edges).
"""

"""
adjlist = {
    "A":["B","D","E","C"],
    "B":["D"],
    "C":[],
    "D":["C"],
    "E":["C","D"]
}

color = {}
parent = {}
trav_time = {}
dfs = []

for val in adjlist.keys(): 
    color[val] = "W" # W G B
    parent[val] = None
    trav_time[val] = [-1,-1]

time = 0
def DFS(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time

    for val in adjlist[u]:
        if color[val] == "W":
            color[val] = "G"
            parent[val] = u
            DFS(val)
    if u not in dfs:
        dfs.append(u)
    else: 
        return False
    color[u] = "B"        
    trav_time[u][1] = time
    time += 1
result = []
dfs.reverse()
result += dfs
print(dfs)
dfs.clear()

def topsort():
    #visited = [False for i in range(len(adjlist)-1)]
    visited = {}
    for val in adjlist.keys():
        visited[val] = False
    for val in adjlist.keys():
        if(visited[val] == False):
            DFS(val)
            visited[val] = True
            for i in adjlist[val]:
                visited[i] = True

topsort()
result.reverse()
print(result)        
"""
from collections import defaultdict 

class Graph: 
	def __init__(self, vertices): 
		self.graph = defaultdict(list) # dictionary containing adjacency List 
		self.V = vertices # No. of vertices 

	# function to add an edge to graph 
	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	def topologicalSortUtil(self, v, visited, stack): 
		visited[v] = True

		for i in self.graph[v]: 
			if visited[i] == False: 
				self.topologicalSortUtil(i, visited, stack) 

		stack.append(v)
        print(stack)

	def topologicalSort(self): 
		# Mark all the vertices as not visited 
		visited = [False]*self.V 
		stack = [] 

		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i, visited, stack) 

		# Print contents of the stack 
		print(stack[::-1]) # return list in reverse order 

# Driver Code 
g = Graph(6) 
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 

print("Following is a Topological Sort of the given graph")

g.topologicalSort() 


