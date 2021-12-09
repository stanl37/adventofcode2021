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

def good_neighbor(p, p_seen) -> list[tuple]: 
  x, y = p[0], p[1]
  proper_flow = True
  # upper check
  if y > 0:
    n_up = vals[y-1][x]
  else:
    n_up = 10
  # lower check
  if y < len(vals) - 1:
    n_down = vals[y+1][x]
  else:
    n_down = 10
  # left check
  if x > 0:
    n_left = vals[y][x-1]
  else:
    n_left = 10
  # right check
  if x < len(vals[0]) - 1:
    n_right = vals[y][x+1]
  else:
    n_right = 10
  

def find_basin(point):
  global vals
  points_to_check = []
  points_seen = []
  points_to_check.append(point)
  while good_neighbor(point):
    pass
  

print(low_points)