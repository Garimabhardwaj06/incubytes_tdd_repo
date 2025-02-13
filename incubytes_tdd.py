from functools import reduce

def add(inpStr: str) -> int:
    sumValue = 0
    if inpStr == '':
        return sumValue
    
    delimiter = ","
    inpStr = inpStr.split(delimiter)
    sumValue = reduce(lambda x,y: x+y, map(lambda x: int(x),inpStr) )
    return sumValue


outValue = add("1")
print(f'sum value is ------------>{outValue}')