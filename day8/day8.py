import os
with open(os.getcwd() + "\day8\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

# 1: 2
# 4: 4
# 7: 3
# 8: 7

sum = 0
for string in input:
  output_values = string.split("|")[1].strip().split()
  for val in output_values:
    if len(val) in [2, 4, 3, 7]:
      sum += 1

print(sum)