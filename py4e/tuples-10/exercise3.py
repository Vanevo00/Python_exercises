# Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

filename = input("Enter file name: ")
occurence = {}

try:
  fhand = open(filename)
except:
  print("invalid name:", filename)
  exit()

for line in fhand:
  stripline = (line.strip().lower())
  for letter in list(stripline):
    if letter.isalpha():
      occurence[letter] = occurence.get(letter, 0) + 1

lst = list()
for key, val in list(occurence.items()):
    lst.append((key, val))

lst.sort()

for key, val in lst:
    print(key, val)