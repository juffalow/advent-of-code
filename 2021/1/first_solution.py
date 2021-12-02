import sys

isFirst = True
previousLine = 0
increasesCount = 0

for line in sys.stdin:
    if isFirst == True:
      previousLine = int(line)
      isFirst = False
      continue
    
    if int(line) > previousLine:
      increasesCount = increasesCount + 1
    previousLine = int(line)

print(increasesCount)
