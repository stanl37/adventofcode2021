import os
with open(os.getcwd() + "\day7\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

positions = input[0].split(",")
positions = [int(i) for i in positions]

import statistics
median = statistics.median(positions)

fuel = 0
for pos in positions:
  fuel += abs(pos - median)

print(fuel)