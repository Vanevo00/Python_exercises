# Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

# Constraints
# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

def valid_parentheses(string):
    # filter brackets
    def checkForBrackets(sign):
      if sign == "(" or sign == ")":
        return True
      else:
        return False

    strList = list(string)
    filteredList = list(filter(checkForBrackets, strList))
    
    openBracketCount = 0

    for bracket in filteredList:
      if bracket == "(":
        openBracketCount += 1
      elif bracket == ")" and openBracketCount < 1:
        return False
      elif bracket == ")" and openBracketCount >= 1:
        openBracketCount -= 1

    if openBracketCount != 0:
      return False
    else:
      return True
      

  
print(valid_parentheses("pes(()24)()()"))