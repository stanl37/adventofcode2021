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

def have_we_visited_small_twice_already(mynode, visited) -> bool:
  for node in visited:
    if (node.islower()):
      if (visited[node] == 2):
        if (node != mynode):
          return True
  return False


def get_paths_helper(node, destination, visited, path):

  # mark node as visited
  visited[node] += 1
  path.append(node)

  # If current vertex is same as destination, then print current path[]
  if node == destination:
    print(visited, path)
    paths.append(path.copy())
  else:
    # If current vertex is not destination
    # Recur for all the vertices adjacent to this vertex
    for next_node in edges[node]:
      if next_node.islower():
        if next_node == 'end':
          get_paths_helper(next_node, destination, visited, path)
        elif next_node == 'start':
          continue
        elif (visited[next_node] < 1):
          get_paths_helper(next_node, destination, visited, path)
        elif (visited[next_node] < 2) and not have_we_visited_small_twice_already(next_node, visited):
          get_paths_helper(next_node, destination, visited, path)
      else:
        get_paths_helper(next_node, destination, visited, path)

  # Remove current vertex from path[] and mark it as unvisited
  path.pop()
  visited[node] -= 1

def get_paths(source, destination):
  visited = {node:0 for node in nodes}
  path = []
  get_paths_helper(source, destination, visited, path)

paths = []
get_paths('start', 'end')
# print(edges)
# print(nodes)
print(paths)
print(len(paths))