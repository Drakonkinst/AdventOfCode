import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    for line in lines:
        (originalRecord, keyStr) = words(line)
        originalRecord += "." # Always end on a valid spring
        key = positive_ints(keyStr)
        validArrangements = 0
        q = deque()
        q.append((originalRecord, 0, 0, 0))
        while q:
            (record, numDamaged, recordIndex, keyIndex) = q.pop()
            
            # Check if end of record
            if recordIndex >= len(record):
                if keyIndex < len(key):
                    # Invalid
                    continue
                validArrangements += 1
                continue
            
            recordChar = record[recordIndex]
            if recordChar == ".":
                if numDamaged == 0:
                    q.append((record, numDamaged, recordIndex + 1, keyIndex))
                else:
                    if numDamaged == key[keyIndex]:
                        q.append((record, 0, recordIndex + 1, keyIndex + 1))
                    else:
                        # Invalid
                        continue
            elif recordChar == "#":
                if keyIndex >= len(key):
                    # Invalid, should not be encountering any more damaged parts
                    continue
                q.append((record, numDamaged + 1, recordIndex + 1, keyIndex))
            elif recordChar == "?":
                recordWithValid = record[:recordIndex] + "." + record[recordIndex + 1:]
                recordWithDamaged = record[:recordIndex] + "#" + record[recordIndex + 1:]
                q.append((recordWithValid, numDamaged, recordIndex, keyIndex))
                q.append((recordWithDamaged, numDamaged, recordIndex, keyIndex))
        total += validArrangements
    print(total)

if __name__ == "__main__":
    main()