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
    exp = [0]
    s = ""
    result = [0 for e in range(maxExp)]
    for i in range(1, maxExp + 1):
        arr.append((5 ** (i - 1)) * 3)
        arr.append((5 ** (i - 1)) * 4)
        arr.append(5 ** i)
        arr.append(5 ** i + (5 ** (i - 1)) * 3)
        arr.append(5 ** i + (5 ** (i - 1)) * 4)
        arr.append((5 ** i) * 2)
        sym.append((1, -2))
        sym.append((1, -1))
        sym.append((1, 0))
        sym.append((2, -2))
        sym.append((2, -1))
        sym.append((2, 0))
        exp.append(i)
        exp.append(i)
        exp.append(i)
        exp.append(i)
        exp.append(i)
        exp.append(i)

    i = len(arr) - 1
    while i >= 0:
        div = dec // arr[i]
        dec %= arr[i]
        
        while div > 0:
            result[maxExp - exp[i] - 1] += sym[i][0]
            if sym[i][1] != 0:
                result[maxExp - exp[i]] += sym[i][1]
            div -= 1
        i -= 1
    for j in range(len(result) - 1, 0, -1):
        if result[j] == 3:
            result[j] = -2
            result[j - 1] += 1
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
    #print(toSnafu(11))
    
if __name__ == "__main__":
    main()