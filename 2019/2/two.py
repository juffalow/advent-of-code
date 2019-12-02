import sys

def compute(numbers):
  for i in range(0, len(numbers), 4):
    if numbers[i] == 1:
      numbers[numbers[i + 3]] = numbers[numbers[i + 1]] + numbers[numbers[i + 2]]
    if numbers[i] == 2:
      numbers[numbers[i + 3]] = numbers[numbers[i + 1]] * numbers[numbers[i + 2]]
    if numbers[i] == 99:
      break

def bruteforce(numbers):
  for i in range(0, 100):
    for j in range(0, 100):
      memory = numbers.copy()
      memory[1] = i
      memory[2] = j
      compute(memory)
      if (memory[0] == 19690720):
        return memory

for line in sys.stdin:
  array = line.split(",")
  numbers = [int(i) for i in array]

print(bruteforce(numbers))
