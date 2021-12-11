import sys
from collections import deque

positions = list(map(int, sys.stdin.readline().strip().split(",")))
maxPosition = max(positions)
minPosition = min(positions)
total = 999999999

for x in range(minPosition, maxPosition + 1):
  fuel = 0
  for position in positions:
    fuel += (float(abs(x - position)) / 2) * (1 + abs(x - position))

  if fuel < total:
    total = fuel

print(total)
