import os
with open(os.getcwd() + "\day4\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

rand_seq = input.pop(0).split(',')
rand_seq = [int(i) for i in rand_seq]

def checkWins(grids):
  for grid in grids:
    if checkWin(grid):
      return grid

def checkWin(grid):
  # row win
  for row in grid:
    win = True
    for item in row:
      if item != "x":
       win = False
    if win:
      return win
  # col win
  for i in range(0, len(row)):
    win = True
    for row in grid:
      if row[i] != "x":
        win = False
    if win:
      return win

def checkNumber(number):
  global grids
  for grid in grids:
    for row in grid:
      for i in range(0, len(row)):
        if row[i] != 'x' and int(row[i]) == number:
          row[i] = 'x'

grids = []  # list of 2d arrays (list of lists of lists)
temp_grid = []
row_index = 0
for line in input:  
  if row_index == 5:
    grids.append(temp_grid)
    temp_grid = []
    row_index = 0
  temp_grid.append(line)
  row_index += 1
grids.append(temp_grid)
for grid in grids:
  for i in range(0, len(grid)):
    grid[i] = grid[i].split()

for number in rand_seq:
  checkNumber(number)
  if grid := checkWins(grids):
    break

sum = 0
for row in grid:
  for item in row:
    if item != 'x':
      sum += int(item)

print(sum * number)