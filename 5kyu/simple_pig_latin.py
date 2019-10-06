# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
  splitWords = text.split(" ")
  pigList = []
    
    
  for word in splitWords:
    if word in "!,.?":
      pigList.append(word)
    else:
      pigList.append(word[1:] + word[:1] + "ay")

  return " ".join(pigList)

print(pig_it("Hello o world !"))