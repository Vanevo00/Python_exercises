# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered
# Input strings s1 and s2 are null terminated.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2):
    s1List = list(s1)
    
    for letter in s2:
      try:
        del s1List[s1List.index(letter)]
      except:
        return False

    return True
    

print(scramble("wkkvuihqwzgzjbpyzu", "qbhuzzoasuovanyruciy"))