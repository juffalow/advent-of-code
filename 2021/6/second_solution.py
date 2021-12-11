import sys
from collections import deque

oldFishDays = [0 for x in range(7)]
newFishDays = [0 for x in range(9)]

fishes = sys.stdin.readline().strip().split(",")

for fish in fishes:
  if int(fish) > 6:
    newFishDays[int(fish)] += 1
  else:
    oldFishDays[int(fish)] += 1

oldFishDaysQueue = deque(oldFishDays)
newFishDaysQueue = deque(newFishDays)

for x in range(1, 257):
  newFishCount = oldFishDaysQueue[0]
  newOldFishCount = newFishDaysQueue[0]
  newFishDaysQueue[0] = 0
  oldFishDaysQueue.rotate(-1)
  newFishDaysQueue.rotate(-1)
  newFishDaysQueue[8] += newFishCount + newOldFishCount
  oldFishDaysQueue[6] += newOldFishCount

print(sum(oldFishDaysQueue) + sum(newFishDaysQueue))
