import os
with open(os.getcwd() + "\day[FIX]\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

# input = input[0].split(",")
# input = [int(i) for i in input]
for string in input:
  pass