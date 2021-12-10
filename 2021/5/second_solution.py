import sys

size = 1000
diagram = [[0 for x in range(size)] for y in range(size)]

for line in sys.stdin:
  ventsLine = line.strip().split(" ")
  [ x1, y1 ] = ventsLine[0].split(",")
  [ x2, y2 ] = ventsLine[2].split(",")

  x1, x2 = int(x1), int(x2)
  y1, y2 = int(y1), int(y2)

  if x1 != x2 and y1 != y2:
    x = x1
    for y in range(y1, y2 + (1 if y1 < y2 else -1), 1 if y1 < y2 else -1):
      diagram[y][x] += 1
      x += 1 if x1 < x2 else -1

  if x1 > x2:
    x1, x2 = x2, x1
  
  if y1 > y2:
    y1, y2 = y2, y1

  if x1 == x2 or y1 == y2:
    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        diagram[y][x] += 1

points = 0

for x in range(0, size):
  for y in range(0, size):
    if diagram[y][x] > 1:
      points += 1

print(points)
