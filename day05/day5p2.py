import os
with open(os.getcwd() + "\day5\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

# get width and height (x max, y max)
import re
max_x = 0
max_y = 0
for string in input:
  foundvals = re.findall(r'\d+', string)
  foundvals = [int(i) for i in foundvals]
  for val in foundvals:
    if foundvals.index(val) % 2 == 0:  # is 0 or 2, aka x coords
      if val > max_x:
        max_x = val
    else:
      if val > max_y:
        max_y = val

array = [[0]*(max_x+1) for y in range(max_y+1)]

line_list = [string.split(" -> ") for string in input]
for line in line_list:

  x1, y1 = [int(i) for i in line[0].split(',')]
  x2, y2 = [int(i) for i in line[1].split(',')]
  if x1 == x2:  # vertical line
    for i in range(min(y1, y2), max(y1, y2)+1):
      array[i][x1] += 1
  elif y1 == y2:  # horizontal line
    for i in range(min(x1, x2), max(x1, x2)+1):
      array[y1][i] += 1
  else:  # diagonal line
    slope = int((y2 - y1) / (x2 - x1))
    start_x = min(x1, x2)
    if start_x == x1:
      myy = y1
    else:
      myy = y2
    for i in range(start_x, max(x1, x2) + 1):
      array[myy][i] += 1
      myy += slope

total = 0
[total := total + 1 for row in array for value in row if value > 1]

print(total)