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

sum = 0

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
    sum += vals[y][x] + 1

print(sum)