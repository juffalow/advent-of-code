import sys

sum = 0

group = []

for line in sys.stdin:
  row = line.strip()

  group.append(row)

  if len(group) == 3:
    elf1 = set(list(group[0]))
    elf2 = set(list(group[1]))
    elf3 = set(list(group[2]))

    for letter in elf1:
      if letter in elf2 and letter in elf3:
        priority = ord(letter)

        if priority > 90:
          sum += priority - 96
        else:
          sum += priority - 64 + 26
    
    group.clear()
        
print(sum)
