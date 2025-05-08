TITLE: Implement A* Algorithm for any game search problem

Code:
def astaralgo(start_node, stop_node):
# Open set stores nodes to be evaluated open_set = set([start_node])
# Closed set stores already evaluated nodes closed_set = set()

# Dictionary to store the cost from start_node to each node g = {}
# Dictionary to store parent nodes to reconstruct path parents = {}
# Cost from start to start is 0 g[start_node] = 0
# Start node is its own parent parents[start_node] = start_node

while len(open_set) > 0: n = None

# Select the node with the lowest f(n) = g(n) + h(n) for v in open_set:
if n is None or g[v] + heuristic(v) < g[n] + heuristic(n): n = v

# If we reached the goal node, reconstruct and return the path if n == stop_node:
path = []
while parents[n] != n: path.append(n)
n = parents[n] path.append(start_node) path.reverse()
print("Path found: {}".format(path)) return path

# If no more neighbors exist, continue to next iteration if Graph_nodes[n] is None:
continue

# Iterate through neighbors of the current node for (m, weight) in get_neighbors(n):
# If neighbor is neither in open_set nor closed_set, add it if m not in open_set and m not in closed_set:
open_set.add(m) parents[m] = n

g[m] = g[n] + weight else:
# If we found a shorter path to m, update g(m) and parent if g[m] > g[n] + weight:
g[m] = g[n] + weight parents[m] = n
# If m is already evaluated, move it back to open_set if m in closed_set:
closed_set.remove(m) open_set.add(m)

# Remove current node from open_set and add to closed_set open_set.remove(n)
closed_set.add(n)

# If we exit the loop, no path was found print("Path does not exist!")
return None
# Function to get neighbors of a node def get_neighbors(v):
if v in Graph_nodes: return Graph_nodes[v]
else:
return None
# Heuristic function (Estimated cost from node to goal) def heuristic(n):
H_dist = { 'A': 10,
'B': 5,
'C': 50,
'D': 2,
'E': 6,
'G': 0, # Goal node has heuristic 0
}
return H_dist[n]

# Graph representation (Adjacency list) Graph_nodes = {
'A': [('B', 3), ('E', 4)],
'B': [('C', 2), ('G', 7)],
'C': [('D', 5)], # C now has an outgoing edge
'E': [('D', 5)],
'D': [('G', 2)],
}
# Execute A* Algorithm astaralgo('A', 'G')
