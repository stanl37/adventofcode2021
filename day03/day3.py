import os
with open(os.getcwd() + "\day3\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]

line_length = len(input[0])

gamma_rate = ""
tally0 = 0
tally1 = 0
for i in range(0, line_length):
  for string in input:
    if string[i] == "0":
      tally0 += 1
    else:
      tally1 += 1
  if tally0 > tally1:
    gamma_rate += "0"
  else:
    gamma_rate += "1"
  tally0 = 0
  tally1 = 0

epsilon_rate = ""
for c in gamma_rate:
  if c == "0":
    epsilon_rate += "1"
  else:
    epsilon_rate += "0"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(gamma_rate * epsilon_rate)