import sys

def decode(play):
  return {
    "A": 0,
    "X": 0,
    "B": 1,
    "Y": 1,
    "C": 2,
    "Z": 2,
  }[play]

def add(a, b):
  result = a + b
  if result >= 3:
    return result - 3
  
  return result

sum = 0

for line in sys.stdin:
  [ opponent, me ] = line.strip().split(" ")

  opponent = decode(opponent)
  me = decode(me)

  if opponent == me:
    outcome = 3

  if add(opponent, 1) == me:
    outcome = 6

  if add(opponent, 2) == me:
    outcome = 0

  sum += me + 1 + outcome

print(sum)
