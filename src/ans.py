""" 
3. Whitespace Analyzer (Expands on 2-7)

Task: Write a Python script where you assign a string to a 
variable that includes leading, trailing, and internal whitespace 
(spaces, tabs, and newlines). Create a function that reports the 
count of each type of whitespace at both the beginning and end of the string, 
without altering the original string. Then, print the string after stripping the whitespace.

Key Concepts: String methods, function creation, loop or conditional logic.
"""

def insertOrIncrement(map, key_to_insert):
    if key_to_insert in map:
        map[key_to_insert] = map[key_to_insert] + 1
    else:
        map[key_to_insert] = 1
    return map

def checkKindOfWhitespace(indivChar):
    return indivChar == ' ' or indivChar == '\t' or indivChar == '\n'

def whitespace_analyzer(input_string):
    leading = {}
    trailing = {}
    for indivChar in input_string:
        if not indivChar.isalnum():
            if checkKindOfWhitespace(indivChar):
                leading = insertOrIncrement(leading, indivChar)
        else:
            break
    
    for i in range(len(input_string) - 1, -1, -1):
        indivChar = input_string[i]
        if not indivChar.isalnum():
            if checkKindOfWhitespace(indivChar):
                trailing = insertOrIncrement(trailing, indivChar)
        else:
            break
    
    return leading, trailing, input_string.strip()