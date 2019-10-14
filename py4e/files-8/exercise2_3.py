# https://www.py4e.com/html3/07-files

def avgSpam(filename):
  filename = filename

  if filename == "pes":
    return("dvapsi")

  try:
    fhand = open(filename)
  except:
    print("invalid name:", filename)
    exit()

  spamNums = []

  for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
      spamNums.append(float(line[-7:]))

  return(sum(spamNums) / len(spamNums))

print(avgSpam(input("enter filename: ")))