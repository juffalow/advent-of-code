import sys

forward = 0
depth = 0

for line in sys.stdin:
    [ direction, value ] = line.split(" ")

    if direction == "forward":
      forward += int(value)
    
    if direction == "down":
      depth += int(value)
    
    if direction == "up":
      depth -= int(value)

print(forward, depth, forward * depth)
