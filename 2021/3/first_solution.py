import sys

count = 0
diagnostic = []

for line in sys.stdin:
  if len(diagnostic) == 0:
    diagnostic = [0] * (len(line) - 1)

  index = 0
  for bit in line:
    if bit == "1":
      diagnostic[index] += 1
    index += 1

  count += 1

gammaRate = 0
epsilonRate = 0

for number in diagnostic:
  if number > count - number:
    gammaRate <<= 1
    gammaRate += 1
    epsilonRate <<= 1
  else:
    epsilonRate <<= 1
    epsilonRate += 1
    gammaRate <<= 1

print(gammaRate * epsilonRate)