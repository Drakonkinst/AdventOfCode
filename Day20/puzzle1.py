from collections import deque

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    original = []
    copy = []
    lookup = {}
    freq = {}
    n = 0
    for line in lines:
        val = int(line)
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1
        x = (val, freq[val])
        original.append(x)
        copy.append(x)
        lookup[x] = n
        n += 1
    
    numMix = 1
    for m in range(numMix):
        for i in range(n):
            #print(copy)
            toMove = original[i]
            val = toMove[0]
            
            if val % n == 0:
                continue

            # This part only works because the input only circles a max of 2 times
            # So 2 iterations will do it
            toMoveIndex = lookup[toMove]
            timesCircled = (toMoveIndex + val) // n
            timesCircledAgain = (toMoveIndex + val + timesCircled) // n
            newIndex = (toMoveIndex + val + timesCircledAgain) % n
            
            if newIndex == toMoveIndex:
                continue

            step = 1 if newIndex > toMoveIndex else -1
            for j in range(toMoveIndex, newIndex, step):
                movingVal = copy[j + step]
                copy[j] = movingVal
                lookup[movingVal] = j
            copy[newIndex] = toMove
            lookup[toMove] = newIndex
            #print(toMove, "moves from", toMoveIndex, "to", newIndex, "->", copy, timesCircled)
        #print("FINAL", copy)

        zeroIndex = lookup[(0, 1)]
        n1 = copy[(zeroIndex + 1000) % n][0]
        n2 = copy[(zeroIndex + 2000) % n][0]
        n3 = copy[(zeroIndex + 3000) % n][0]

        print([x[0] for x in copy])
        print(zeroIndex, n1, n2, n3, "TOTAL", n1 + n2 + n3)

if __name__ == "__main__":
    main()