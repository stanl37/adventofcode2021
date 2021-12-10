# i'm reminded of the leetcode problem of matching parentheses

import os
with open(os.getcwd() + "\day10\input.txt", "r") as f:
  input = f.readlines()
input = [input.strip() for input in input]
input = [i for i in input if i]

openers = ('(', '[', '{', '<')
closers = (')', ']', '}', '>')
c_to_o_key = {
  ')': '(',
  ']': '[',
  '}': '{',
  '>': '<'
}

corrupteds = []
# removing corrupted strings
for string in input:
  # making a stack
  from collections import deque
  stack = deque()
  index = 0
  for char in string:
    if char in openers:
      stack.append(char)
    if char in closers:
      val = stack.pop()
      if c_to_o_key[char] != val:
        corrupteds.append(string)

incompletes = [string for string in input if string not in corrupteds]

fixers = []
for incomplete in incompletes:
  stack = deque()
  index = 0
  for char in incomplete:
    if char in openers:
      stack.append(char)
    if char in closers:
      val = stack.pop()

  o_to_c_key = {v: k for k, v in c_to_o_key.items()}
  fixer = []
  while stack:
    char = stack.pop()
    fixer.append(o_to_c_key[char])
  fixers.append(fixer)

scores = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}
def calc_score(fixer):
  running = 0
  for char in fixer:
    running *= 5
    running += scores[char]
  return running

fixer_scores = []
for fixer in fixers:
  score = calc_score(fixer)
  fixer_scores.append(score)

fixer_scores.sort()

import statistics
print(statistics.median(fixer_scores))