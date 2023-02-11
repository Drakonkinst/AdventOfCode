import sys

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    i = 0
    sensors = []
    allTaken = set()
    minX = sys.maxsize
    maxX = -sys.maxsize
    maxDist = -1
    while i < len(lines):
        line = lines[i]
        words = line.split(" ")
        sX = int(words[2][2:-1])
        sY = int(words[3][2:-1])
        bX = int(words[8][2:-1])
        bY = int(words[9][2:])
        minX = min(minX, sX, sY)
        maxX = max(maxX, sX, sY)
        dist = abs(sX - bX) + abs(sY - bY)
        maxDist = max(maxDist, dist)
        sensors.append((sX, sY, dist))
        #allTaken.add((sX, sY))
        allTaken.add((bX, bY))
        #print(sX, sY, bX, bY)
        i += 1
        
    y = 2000000
    minX -= maxDist
    maxX += maxDist
    x = minX
    n = 0
    total = 0
    print(minX, maxX)
    while x <= maxX:
        #print(n)
        if (x, y) not in allTaken:
            isNot = False
            for s in sensors:
                dist = abs(x - s[0]) + abs(y - s[1])
                if dist <= s[2]:
                    isNot = True
                    break
            if isNot:
                total += 1
        x += 1
        n += 1
    print(total, n)

if __name__ == "__main__":
    main()