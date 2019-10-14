# https://www.py4e.com/html3/07-files

filename = input("Enter file name: ")

try:
  fhand = open(filename)
except:
  print("invalid name:", filename)
  exit()

for line in fhand:
  print(line.upper())