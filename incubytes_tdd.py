from functools import reduce
import re

'''
This method will output the sum of numbers in a given string
'''
def add(inpStr: str) -> int:
    sumValue = 0

    if inpStr == '':
        return sumValue 
    
    # Declaring the default delimiter comma
    delimiter = "," 

    # This checks if there is a custom delimiter when string starts with "//"
    if inpStr.startswith("//"):
        delimiter_part, inpStr = inpStr.split('\n', 1) #This separated the string into parts
        # one with delimiter and the other is the string.
        custom_delimiters = re.findall(r'\[(.*?)\]', delimiter_part) #This finds the delimiters in 
        # the first part of the input string

        ''' If there are multiple delimiters we join them with the OR operator. If not we use the 
        delimiter from third character onwards removing "//"'''
        if custom_delimiters:
            delimiter = '|'.join(map(re.escape, custom_delimiters))
        
        else:
            delimiter = re.escape(delimiter_part[2:])
    
    inpStr = re.sub(r'\n', delimiter, inpStr) #This substitutes all newline chars with delimiters
    number_list = re.split(delimiter, inpStr) # Then we split the string using the delimiters as the separators
    
    numValues = list(map(lambda x: int(x), number_list) ) # We use map to convert the numbers from string to int type

    negatives = [num for num in numValues if num < 0] #Check for negative integers
    if negatives:
        raise ValueError(f"Negative numbers are not allowed {negatives}")
    
    sumValue = reduce(lambda x,y: x+y if y <=1000 else x,numValues,0) # reduce to get the sum of all numbers
    # in the list if the numbers are less than or equal to 1000.
    return sumValue

outValue = add("//[***]\n1***2000***3")
print(f'sum value is ------------>{outValue}')