import sys

currentTriplet = []
increasesCount = 0

for line in sys.stdin:
    if len(currentTriplet) < 3:
      currentTriplet.append(int(line))
      continue

    first = currentTriplet.pop(0)

    if sum(currentTriplet) + int(line) > sum(currentTriplet) + first:
      increasesCount += 1

    currentTriplet.append(int(line))

print(increasesCount)
