from functools import reduce
import re

def add(inpStr: str) -> int:
    sumValue = 0
    if inpStr == '':
        return sumValue
    
    delimiter = ","
    inpStr = inpStr.replace('\n', delimiter)
    inpStr = inpStr.split(delimiter)
    
    sumValue = reduce(lambda x,y: x+y, map(lambda x: int(x),inpStr) )
    return sumValue


outValue = add("1\n2,3")
print(f'sum value is ------------>{outValue}')