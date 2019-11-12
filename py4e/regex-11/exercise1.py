# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
import re

filename = input("Enter file name: ")

try:
  fhand = open(filename)
except:
  print("invalid name:", filename)
  exit()

regex = input("Enter a regular expression: ")
count = 0

for line in fhand:
  if re.search(regex, line):
    count += 1

print(filename + " had " + str(count) + " lines that matched " + regex)