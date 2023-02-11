import sys
import math
from collections import deque

symbols = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2
}

vals = ["=", "-", "0", "1", "2"]

def toDec(snafu):
    exp = 0
    total = 0
    for i in range(len(snafu) - 1, -1, -1):
        ch = snafu[i]
        total += symbols[ch] * (5 ** exp)
        exp += 1
    return total
    
def toSnafu(dec):
    maxExp = math.ceil(math.log(dec, 5))
    arr = [1]
    sym = [(1, 0)]
    exps = [0]
    s = ""
    result = [0 for _ in range(maxExp)]
    for exp in range(1, maxExp + 1):
        thisExp = 5 ** exp
        nextExp = 5 ** (exp - 1)
        arr.append(nextExp * 3)
        arr.append(nextExp * 4)
        arr.append(thisExp)
        arr.append(thisExp + (nextExp * 3))
        arr.append(thisExp + (nextExp * 4))
        arr.append(thisExp * 2)
        sym.append((1, -2))
        sym.append((1, -1))
        sym.append((1, 0))
        sym.append((2, -2))
        sym.append((2, -1))
        sym.append((2, 0))
        for _ in range(6):
            exps.append(exp)

    i = len(arr) - 1
    while i >= 0:
        div = dec // arr[i]
        dec %= arr[i]
        
        while div > 0:
            index = maxExp - exps[i] - 1
            result[index] += sym[i][0]
            if sym[i][1] != 0:
                result[index + 1] += sym[i][1]
            div -= 1
        i -= 1

    # Perform corrections
    for j in range(len(result) - 1, 0, -1):
        if result[j] == 3:
            result[j] = -2
            result[j - 1] += 1
        elif result[j] == 4:
            result[j] = -1
            result[j - 1] += 1
        elif result[j] > 2:
            assert False
    
    # Create the string
    s = "".join([vals[val + 2] for val in result])
    return s
    

def main():
    file = open("input.txt", "r")
    lines = [line.strip() for line in file.readlines()]
    
    n = 0
    total = 0
    for line in lines:
        dec = toDec(line)
        #print(line, "->", dec)
        total += dec
        n += 1
    print(total)
    print(toSnafu(total))
    
if __name__ == "__main__":
    main()