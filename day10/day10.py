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

illegals = []
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
        illegals.append(char)

scores = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}
total = 0
for illegal in illegals:
  total += scores[illegal]

print(total)