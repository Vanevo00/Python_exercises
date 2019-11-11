# This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

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
      hour = splitLine[5].split(':')[0]
      occurence[hour] = occurence.get(hour, 0) + 1

# Sort the dictionary by key
lst = list()
for key, val in list(occurence.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)