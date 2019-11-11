# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

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
      email = splitLine[1].split('@')
      occurence[email[1]] = occurence.get(email[1], 0) + 1


maxValue = []

for key in occurence:
  if maxValue == [] or maxValue[1] < occurence[key]:
    maxValue = [key, occurence[key]]

print(maxValue[0], maxValue[1])