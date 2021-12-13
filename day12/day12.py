# had to make my own implementation of a Graph

import os
with open(os.getcwd() + "\day12\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

# set of nodes
nodes = set()
for string in input:
  node1, node2 = string.split("-")
  nodes.update([node1, node2])

# creating graph as a dict (every edge is bidirectional)
edges = dict()
for node in nodes:
  edges[node] = []
for string in input:
  node1, node2 = string.split("-")
  list = edges[node1]
  list.append(node2)
  list2 = edges[node2]
  list2.append(node1)

# generating all paths
# FUNCTIONS FROM: https://www.geeksforgeeks.org/find-paths-given-source-destination/

def get_paths_helper(node, destination, visited, path):
  # mark node as visited
  visited[node] = True
  path.append(node)

  # If current vertex is same as destination, then print current path[]
  if node == destination:
    paths.append(path.copy())
  else:
    # If current vertex is not destination
    # Recur for all the vertices adjacent to this vertex
    for next_node in edges[node]:
      if next_node.islower():
        if not visited[next_node]:
          get_paths_helper(next_node, destination, visited, path)
      else:
        get_paths_helper(next_node, destination, visited, path)

  # Remove current vertex from path[] and mark it as unvisited
  path.pop()
  visited[node] = False

def get_paths(source, destination):
  visited = {node:False for node in nodes}
  path = []
  get_paths_helper(source, destination, visited, path)

paths = []
get_paths('start', 'end')
# print(edges)
# print(nodes)
# print(paths)
print(len(paths))