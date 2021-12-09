import os
with open(os.getcwd() + "\day8\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

# 0: 6
# 1: 2
# 2: 5
# 3: 5
# 4: 4
# 5: 5
# 6: 6
# 7: 3
# 8: 7
# 9: 6

# easy: 1-2, 4-4, 7-3, 8-7
# 5-panel: 2, 3, 5
#   -> if contains chars of 1, then 3
#   -> if contains chars of 4 minus chars of 1 (fouronediff), then 5
#   -> else 2
# 6-panel: 0, 6, 9
#   -> if contains chars of 4, then 9
#   -> if contains chars of 7, then 0
#   -> else 6

sum = 0
for string in input:
  signal_pattern, output_values = string.split("|")
  signal_pattern = signal_pattern.strip().split()
  output_values = output_values.strip().split()

  key = {}

  # getting keys for obvious numbers
  for signal in signal_pattern:
    val = None
    if len(signal) == 2:
      val = 1
    if len(signal) == 4:
      val = 4
    if len(signal) == 3:
      val = 7
    if len(signal) == 7:
      val = 8
    if val:
      key[val] = "".join(sorted(signal))

  # keys for 5- and 6-bar numbers
  four = set(key[4])
  one = set(key[1])
  fourdiffone = "".join(sorted(one.symmetric_difference(four)))
  for signal in signal_pattern:
    if len(signal) == 5:
      if all(char in signal for char in key[1]):
        key[3] = "".join(sorted(signal))
      elif all(char in signal for char in fourdiffone):
        key[5] = "".join(sorted(signal))
      else:
        key[2] = "".join(sorted(signal))
    if len(signal) == 6:
      if all(char in signal for char in key[4]):
        key[9] = "".join(sorted(signal))
      elif all(char in signal for char in key[7]):
        key[0] = "".join(sorted(signal))
      else:
        key[6] = "".join(sorted(signal))

  # flip dictionary
  inv_key = {v: k for k, v in key.items()}

  # decode output values with our key
  output = ""
  for signal in output_values:
    val = inv_key["".join(sorted(signal))]
    output += str(val)

  sum += int(output)

print(sum)

