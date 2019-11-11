filename = input("Enter file name: ")
occurence = {}

try:
  fhand = open(filename)
except:
  print("invalid name:", filename)
  exit()

for line in fhand:
  stripLine = line.strip()
  if stripLine.startswith('From'):
    splitLine = stripLine.split()
    if len(splitLine) > 2:
      occurence[splitLine[2]] = occurence.get(splitLine[2], 0) + 1

print(occurence)