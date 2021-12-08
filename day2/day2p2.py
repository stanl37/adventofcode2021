import os
with open(os.getcwd() + "\day2\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]

horizontal = 0
depth = 0
aim = 0

for string in input:
  cmd = string.split(" ")[0]
  dist = int(string.split(" ")[1])
  if cmd == "forward":
    horizontal += dist
    depth += aim * dist
  if cmd == "up":
    aim -= dist
  if cmd == "down":
    aim += dist

print(horizontal * depth)