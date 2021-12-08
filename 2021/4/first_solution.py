import sys

rowsAndColumns = []
rows = []

numbers = sys.stdin.readline().strip().split(",")

for line in sys.stdin:
  if line.strip() == "":
    continue
  
  row = line.strip().replace("  ", " ").split(" ")
  rows.append(row)
  rowsAndColumns.append(set(row))

  if len(rows) == 5:
    column = None
    for i in range(0, 5):
      column = [ rows[0][i], rows[1][i], rows[2][i], rows[3][i], rows[4][i] ]
      rowsAndColumns.append(set(column))
    rows = []

winnerBoardIndex = 0
lastNumber = 0

for number in numbers:
  for index, rs in enumerate(rowsAndColumns):
    rs.discard(number)
    if len(rs) == 0:
      winnerBoardIndex = index // 10
      lastNumber = number
      break
  else:  # only execute when it's no break in the inner loop
    continue
  break

score = 0
for i in range(0, 5):
  score += sum(map(int, rowsAndColumns[i + (winnerBoardIndex * 10)]))

print(score * int(lastNumber))
