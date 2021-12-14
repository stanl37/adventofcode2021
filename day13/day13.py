import os
with open(os.getcwd() + "\day13\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

coords = []
folds = []
for string in input:
  if "fold along" in string:
    folds.append(string)
  else:
    coords.append(string)

vals = []
max_x = 0
max_y = 0
for string in coords:
  x, y = string.split(",")
  x = int(x); y = int(y)
  if x > max_x: max_x = x
  if y > max_y: max_y = y
for y in range(max_y + 1):
  vals.append([0]*(max_x + 1))
for string in coords:
  x, y = string.split(",")
  x = int(x); y = int(y)
  vals[y][x] = 1
# access with vals[y][x]

def fold_y(coord):
  global vals
  up = vals[:coord]
  down = vals[coord+1:]
  down.reverse()

  delta = len(up) - len(down)

  for y,row in enumerate(down):
    for x,val in enumerate(row):
      if down[y][x]:
        up[delta + y][x] = 1
  vals = up

def fold_x(coord):
  global vals
  left = []
  right = []
  for y,row in enumerate(vals):
    left.append(row[:coord])
    right.append(row[coord+1:])
  for row in right:
    row.reverse()

  delta = len(left[0]) - len(right[0])

  for y,row in enumerate(right):
    for x,val in enumerate(row):
      if right[y][x]:
        left[y][delta + x] = 1
  vals = left

def fold(axis, coord):
  # axis: direction of fold (ex: 'y')
  #    -> x folds: folding LEFT (right half folds over to left)
  #    -> y folds: folding UP (bottom half folds up to top)
  # coord: coordinate to fold on (ex: 7)

  if axis == 'y':
    fold_y(coord)

  if axis == 'x':
    fold_x(coord)

def printvals():
  for row in vals:
    string = ""
    for item in row:
      if item:
        string += "⬜"
      else:
        string += "⬛"
    print(string)

for cmd in folds:
  print(cmd)
  axis, coord = cmd.split(" ")[2].split("=")
  fold(axis, int(coord))

  printvals()

  dots = 0
  for row in vals:
    dots += row.count(1)

  print(dots)