import sys

forward = 0
depth = 0
aim = 0

for line in sys.stdin:
    [ direction, value ] = line.split(" ")

    if direction == "forward":
      forward += int(value)
      depth += aim * int(value)
    
    if direction == "down":
      aim += int(value)
    
    if direction == "up":
      aim -= int(value)

print(forward, depth, aim, forward * depth)
