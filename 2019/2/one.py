import sys

def compute(numbers):
  for i in range(0, len(numbers), 4):
    if numbers[i] == 1:
      numbers[numbers[i + 3]] = numbers[numbers[i + 1]] + numbers[numbers[i + 2]]
    if numbers[i] == 2:
      numbers[numbers[i + 3]] = numbers[numbers[i + 1]] * numbers[numbers[i + 2]]
    if numbers[i] == 99:
      break

for line in sys.stdin:
  array = line.split(",")
  numbers = [int(i) for i in array]
  compute(numbers)
  print(numbers)
