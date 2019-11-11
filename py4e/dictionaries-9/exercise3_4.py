# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

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
      occurence[splitLine[1]] = occurence.get(splitLine[1], 0) + 1

# Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

maxValue = []

for key in occurence:
  if maxValue == [] or maxValue[1] < occurence[key]:
    maxValue = [key, occurence[key]]

print(maxValue[0], maxValue[1])