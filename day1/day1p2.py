import os
with open(os.getcwd() + "\day1\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = list(map(int, input))

increaseds = 0
for i in range(1, len(input) - 2):
  prev_sum = input[i - 1] + input[i] + input[i + 1]
  curr_sum = input[i] + input[i + 1] + input[i + 2]
  if curr_sum > prev_sum:
    increaseds += 1

print(increaseds)
