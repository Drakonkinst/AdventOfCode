import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# Bah, this approach doesn't work
def get_arrangements(record, key):
    counter = Counter(record)
    numUnknowns = counter["?"] if "?" in counter else 0
    numDamaged = counter["#"] if "#" in counter else 0
    validArrangements = 0
    maxDamage = sum(key)
    q = deque()
    q.append((0, 0, 0, 0, counter["?"], maxDamage - numDamaged))
    numIter = 0
    numPermsExplored = 0
    recordLength = len(record)
    keyLength = len(key)
    while q:
        (numDamaged, recordIndex, keyIndex, totalDamaged, unknownsRemaining, unknownDamageRemaining) = q.pop()
        numIter += 1
            
        # Check if end of record
        if recordIndex >= recordLength:
            if keyIndex < keyLength:
                # Invalid
                continue
            validArrangements += 1
            continue
            
        # Optimizations
        remainingLen = recordLength - recordIndex
        remainingDamaged = maxDamage - totalDamaged
        separatorsNeeded = keyLength - keyIndex - 1
        if remainingLen < remainingDamaged + separatorsNeeded:
            continue
        if unknownsRemaining < unknownDamageRemaining:
            continue
            
        recordChar = record[recordIndex]
        if recordChar == ".":
            if numDamaged == 0:
                q.append((numDamaged, recordIndex + 1, keyIndex, totalDamaged, unknownsRemaining, unknownDamageRemaining))
            else:
                if numDamaged == key[keyIndex]:
                    q.append((0, recordIndex + 1, keyIndex + 1, totalDamaged, unknownsRemaining, unknownDamageRemaining))
        elif recordChar == "#":
            if keyIndex < len(key):
                q.append((numDamaged + 1, recordIndex + 1, keyIndex, totalDamaged + 1, unknownsRemaining, unknownDamageRemaining))
        elif recordChar == "?":
            doDamaged = True
            doValid = True
            
            # Optimizations
            if numDamaged > 0:
                if numDamaged < key[keyIndex]:
                    doValid = False
                elif numDamaged >= key[keyIndex]:
                    doDamaged = False
            else:
                if keyIndex >= keyLength:
                    doDamaged = False
                else:
                    # Look ahead. Does it make sense to start one?
                    isAllDamagedOrUnknown = True
                    for j in range(recordIndex + 1, recordIndex + key[keyIndex]):
                        if record[j] == ".":
                            isAllDamagedOrUnknown = False
                            break
                    if not isAllDamagedOrUnknown:
                        doDamaged = False
            if unknownsRemaining == unknownDamageRemaining:
                doValid = False
            if unknownDamageRemaining <= 0:
                doDamaged = False
            
            if doValid:
                if numDamaged == 0:
                    q.append((numDamaged, recordIndex + 1, keyIndex, totalDamaged, unknownsRemaining - 1, unknownDamageRemaining))
                else:
                    if numDamaged == key[keyIndex]:
                        q.append((0, recordIndex + 1, keyIndex + 1, totalDamaged, unknownsRemaining - 1, unknownDamageRemaining))
            if doDamaged:
                if keyIndex < len(key):
                    q.append((numDamaged + 1, recordIndex + 1, keyIndex, totalDamaged + 1, unknownsRemaining - 1, unknownDamageRemaining - 1))
            if doValid and doDamaged:
                #print("P", "".join(record), recordIndex)
                numPermsExplored += 1
    print("NUMITER", numIter, numPermsExplored)
    return validArrangements
def main():
    total = 0
    maxMultiplier = 5
    n = math.factorial(4)
    i = 0
    for line in lines:
        totalForLine = 0
        (originalRecord, keyStr) = words(line)
        originalKey = positive_ints(keyStr)
        
        firstDamagedOrQuestion = min(originalRecord.index("#") if "#" in originalRecord else len(originalRecord), originalRecord.index("?") if "?" in originalRecord else len(originalRecord))
        modifiedSingle = originalRecord[firstDamagedOrQuestion:] + "."
        single = get_arrangements(modifiedSingle, originalKey)
        totalForLine += single ** 5
        print("M1", single)
        
        for multiplier in range(2, maxMultiplier + 1):
            extendedRecord = (originalRecord + "#") * multiplier
            extendedRecord = extendedRecord[:-1] + "."
            extendedKey = originalKey * multiplier
            extended = get_arrangements(extendedRecord, extendedKey)
            combination = extended * (single ** (maxMultiplier - multiplier))
            r = multiplier - 1
            numCombinations = n // (math.factorial(r) * math.factorial(4 - r))
            totalForLine += combination * numCombinations
            #print("C", combination, extended)
            print("M" + str(multiplier), combination * numCombinations)
        i += 1
        print("LINE", i, "=", totalForLine)
        total += totalForLine
    print(total)

if __name__ == "__main__":
    main()