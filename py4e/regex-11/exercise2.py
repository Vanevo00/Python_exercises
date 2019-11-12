# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

import re

filename = input("Enter file name: ")

try:
  fhand = open(filename)
except:
  print("invalid name:", filename)
  exit()

nums = []

for line in fhand:
  line = line.rstrip()
  newRevision = re.findall('^New Revision: [0-9]+', line)
  if newRevision:
    nums.append(int(newRevision[0].split(':')[1]))

print(int(sum(nums) / len(nums)))