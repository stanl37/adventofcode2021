import os
with open(os.getcwd() + "\day2\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]

horizontal = 0
depth = 0

for string in input:
  cmd, dist = string.split(" ")
  dist = int(dist)
  if cmd == "forward":
    horizontal += dist
  elif cmd == "up":
    depth -= dist
  elif cmd == "down":
    depth += dist

print(horizontal * depth)