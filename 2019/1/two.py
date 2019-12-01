import sys

def fuelsFuel(fuel):
    add = (fuel / 3) - 2
    if add <= 0:
        return 0
    else:
        return add + fuelsFuel(add)

sum = 0

for line in sys.stdin:
    fuel = (int(line) / 3) - 2
    add = fuelsFuel(fuel)
    sum = sum + fuel + add

print(sum)
