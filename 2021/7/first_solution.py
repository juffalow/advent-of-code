import sys
from collections import deque

positions = list(map(int, sys.stdin.readline().strip().split(",")))
maxPosition = max(positions)
minPosition = min(positions)
total = 999999999

for x in range(minPosition, maxPosition + 1):
  fuel = 0
  for position in positions:
    fuel += abs(x - position)

  if fuel < total:
    total = fuel

print(total)
