# This is DEFINITELY not the most efficient solution
# for part 2, I create a "flow table" - instead of height values at each x, y position, I have a tuple to the point which the x, y point flows to
# then I run through every point in the heightmap, seeing if any point's flow point is in a given set of points (set starts with just the low point)
# I then run through every point over and over until the point set does not grow anymore
# this is a pretty bruteforce method, compared to the (likely?) most efficient of BFS

import os
with open(os.getcwd() + "\day9\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

vals = []
for string in input:
  string = [int(char) for char in string]
  vals.append(string)
# access with vals[y][x]

low_points = []

for y in range(len(vals)):
  for x in range(len(vals[0])):
    # upper check
    if y > 0 and vals[y][x] >= vals[y-1][x]:
      continue
    # lower check
    if y < len(vals) - 1 and vals[y][x] >= vals[y+1][x]:
      continue
    # left check
    if x > 0 and vals[y][x] >= vals[y][x-1]:
      continue
    # right check
    if x < len(vals[0]) - 1 and vals[y][x] >= vals[y][x+1]:
      continue
    
    low_points.append((x, y))

def gen_flow_table():
  import copy
  flow = copy.deepcopy(vals)
  # calculation of flow point for each point
  for y in range(len(vals)):
   for x in range(len(vals[0])):
      # if point height is 9, do not consider
      if vals[y][x] == 9:
        flow[y][x] = None
        continue
      # getting allowed neighbors
      n_deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
      ns = []
      for d in n_deltas:
        nx = x+d[0]
        ny = y+d[1]
        if (nx < 0) or (ny < 0) or (nx > len(vals[0]) - 1) or (ny > len(vals) - 1):
          continue
        ns.append((nx, ny))
      # using neighbors to get flow point of given x,y
      low_nv = float('inf')
      low_nx = -1
      low_ny = -1
      for n in ns:
        nv = vals[n[1]][n[0]]
        if nv < low_nv:
          low_nv = nv
          low_nx = n[0]
          low_ny = n[1]
      low_n = (low_nx, low_ny)
      flow[y][x] = low_n
  # return
  return flow

flow = gen_flow_table()

b_size_list = []
for point in low_points:
  p_set = {point}
  while True:
    added = False
    for y in range(len(vals)):
      for x in range(len(vals[0])):
        if flow[y][x] in p_set:
          if (x, y) not in p_set:
            p_set.add((x, y))
            added = True
    if not added:
      break
  b_size_list.append(len(p_set))

b_size_list.sort(reverse=True)
print(b_size_list[0] * b_size_list[1] * b_size_list[2])