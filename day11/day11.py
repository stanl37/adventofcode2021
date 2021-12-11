import os
with open(os.getcwd() + "\day11\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

vals = []
for string in input:
  string = [int(char) for char in string]
  vals.append(string)
# access with vals[y][x]

def step() -> int:
  # energy increases for everyone
  for y in range(len(vals)):
    for x in range(len(vals[0])):
      vals[y][x] += 1
  tot_flashes = 0
  # checking flashes
  flashes = 1
  while flashes:
    flashes = 0
    for y in range(len(vals)):
      for x in range(len(vals[0])):
        if vals[y][x] > 9:
          vals[y][x] = -100
          flashes += 1
          n_deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
          for d in n_deltas:
            
            # check for validity
            nx = x+d[0]
            ny = y+d[1]
            if (nx < 0) or (ny < 0) or (nx > len(vals[0]) - 1) or (ny > len(vals) - 1):
              continue

            vals[ny][nx] += 1
    tot_flashes += flashes
  # fixing flashes
  for y in range(len(vals)):
    for x in range(len(vals[0])):
      if vals[y][x] < 0:
        vals[y][x] = 0
  # return
  return tot_flashes

STEPS = 100
tot = 0
for i in range(STEPS):
  tot += step()
print(tot)


