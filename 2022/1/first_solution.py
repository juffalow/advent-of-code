import sys

elves = []
elf = 1
calories = 0

for line in sys.stdin:
  if line.strip() == "":
    elves.append(calories)
    elf += 1
    calories = 0
    continue

  calories += int(line)

elves.sort(reverse = True)

print(elves[0])
