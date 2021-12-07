import sys
import operator

def compute(binaries, bit, index, compare):
  if len(binaries) == 1:
    return binaries[0]

  trueBit = []
  falseBit = []
  result = None

  for binary in binaries:
    if binary[index] == bit:
      trueBit.append(binary)
    else:
      falseBit.append(binary)
  
  if compare(len(trueBit), len(falseBit)):
    result = compute(trueBit, bit, index + 1, compare)
  else:
    result = compute(falseBit, bit, index + 1, compare)

  return result


lines = []
for line in sys.stdin:
  lines.append(line.strip())


oxygenGeneratorRating = compute(lines, "1", 0, operator.ge)
co2ScrubberRating = compute(lines, "0", 0, operator.le)

print(int(oxygenGeneratorRating, 2) * int(co2ScrubberRating, 2))
