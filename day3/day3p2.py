import os
with open(os.getcwd() + "\day3\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]

oxygen_generator_list = input.copy()
fail_list = []
index = 0
tally0 = 0
tally1 = 0
while len(oxygen_generator_list) > 1:
  for string in oxygen_generator_list:
    if string[index] == "0":
      tally0 += 1
    else:
      tally1 += 1
  if tally1 >= tally0:
    most_common_value = "1"
  else:
    most_common_value = "0"
  for string in oxygen_generator_list:
    if string[index] != most_common_value:
      fail_list.append(string)
  for string in fail_list:
    oxygen_generator_list.remove(string)
  tally0 = 0
  tally1 = 0
  index += 1
  fail_list = []
oxygen_generator_rating = int(oxygen_generator_list[0], 2)

co2_scrubber_list = input.copy()
fail_list = []
index = 0
tally0 = 0
tally1 = 0
while len(co2_scrubber_list) > 1:
  for string in co2_scrubber_list:
    if string[index] == "0":
      tally0 += 1
    else:
      tally1 += 1
  if tally1 >= tally0:
    least_common_value = "0"
  else:
    least_common_value = "1"
  for string in co2_scrubber_list:
    if string[index] != least_common_value:
      fail_list.append(string)
  for string in fail_list:
    co2_scrubber_list.remove(string)
  tally0 = 0
  tally1 = 0
  index += 1
  fail_list = []
co2_scrubber_rating = int(co2_scrubber_list[0], 2)

print(oxygen_generator_rating * co2_scrubber_rating)