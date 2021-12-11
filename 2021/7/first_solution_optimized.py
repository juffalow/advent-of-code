#!/usr/bin/env python3

import sys
from statistics import median

positions = list(map(int, sys.stdin.readline().strip().split(",")))
median = median(positions)

fuel = 0
for position in positions:
  fuel += abs(median - position)

print(fuel)
