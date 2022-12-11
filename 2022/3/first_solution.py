import sys

sum = 0

for line in sys.stdin:
  row = line.strip()
  compartment1 = set(list(row[:len(row) // 2]))
  compartment2 = set(list(row[len(row) // 2:]))

  for letter in compartment1:
    if letter in compartment2:
      priority = ord(letter)

      if priority > 90:
        sum += priority - 96
      else:
        sum += priority - 64 + 26
        
print(sum)
