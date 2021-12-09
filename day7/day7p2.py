import os
with open(os.getcwd() + "\day7\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

positions = input[0].split(",")
positions = [int(i) for i in positions]

max_val = max(positions)

best_fuel = float('inf')
for i in range(max_val):
  fuel = 0
  for pos in positions:
    steps = abs(pos - i)
    fuel += (steps * (steps + 1)) / 2
  if fuel < best_fuel:
    best_fuel = fuel
    # print("fuel{} i{}".format(best_fuel, i))

print(best_fuel)

# note to self, the best value was indeed the mean. except it was not with rounding (for my data, 464.54 was mean, 464 was most efficient, not 465)
# better solution is to test for values expanding outward from the mean instead of from 0->max