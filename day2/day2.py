import os
with open(os.getcwd() + "\day2\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]

horizontal = 0
depth = 0

for string in input:
  cmd = string.split(" ")[0]
  dist = int(string.split(" ")[1])
  if cmd == "forward":
    horizontal += dist
  if cmd == "up":
    depth -= dist
  if cmd == "down":
    depth += dist

print(horizontal * depth)