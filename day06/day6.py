import os
with open(os.getcwd() + "\day6\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

fishes = input[0].split(",")
fishes = [int(i) for i in fishes]

# print("Initial state: ", fishes)

DAYS = 80

# each day:
for day in range(1, DAYS+1):

  # print("on day:", day)

  # check for zeros + spawn fish
  for i in range(len(fishes)):
    if fishes[i] == 0:
      fishes[i] = 7
      fishes.append(9)
  
  # decrease all fish by 1
  for i in range(len(fishes)):
    fishes[i] -= 1

  # print("After {:3} days:".format(day), fishes)

print(len(fishes))