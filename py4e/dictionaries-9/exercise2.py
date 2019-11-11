# Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

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