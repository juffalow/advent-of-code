import sys

sum = 0

for line in sys.stdin:
    fuel = (int(line) / 3) - 2
    sum = sum + fuel
print(sum)
