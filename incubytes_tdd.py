from functools import reduce
import re

def add(inpStr: str) -> int:
    sumValue = 0
    if inpStr == '':
        return sumValue
    
    delimiter = ","


    if inpStr.startswith("//"):
        delimiter_part, inpStr = inpStr.split('\n', 1)
        custom_delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
        if custom_delimiters:
            delimiter = '|'.join(map(re.escape, custom_delimiters))
        else:
            delimiter = re.escape(delimiter_part[2:])
    
    inpStr = re.sub(r'\n', delimiter, inpStr)
    number_list = re.split(delimiter, inpStr)
    
    numValues = list(map(lambda x: int(x), number_list) )


    # inpStr = inpStr.replace('\n', delimiter)
    # inpStr = inpStr.split(delimiter)
    
    sumValue = reduce(lambda x,y: x+y, map(lambda x: int(x),numValues) )
    return sumValue


outValue = add("//[***]\n1***2000***3")
print(f'sum value is ------------>{outValue}')