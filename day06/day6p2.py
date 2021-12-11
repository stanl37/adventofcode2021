import os
with open(os.getcwd() + "\day6\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

fishes = input[0].split(",")
fishes = [int(i) for i in fishes]

# print("Initial state: ", fishes)

DAYS = 256

fishstates = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}  # keys: fish state. values: number of fish with that state
for fish in fishes:
  fishstates[fish] += 1

# each day:
for day in range(1, DAYS+1):

  print("on day:", day)

  # check for zeros and spawn fish
  fishstates[7] += fishstates[0]
  fishstates[9] += fishstates[0]
  fishstates[0] = 0
  
  # decrease all fish by 1 (shift numbers)
  for i in range(0, 9):
    fishstates[i] = fishstates[i+1]
  fishstates[9] = 0

  # print("After {:3} days:".format(day), fishstates)

print(sum(fishstates.values()))