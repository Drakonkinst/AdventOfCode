import sys
import math

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    i = 0
    grid = []
    width = 4000000
    #width = 20
    cell = 10000
    #cell = 1
    numCells = width // cell + 1
    avgDist = 0
    print("CELL: ", cell, numCells)
    for i in range(numCells):
        row = []
        for j in range(numCells):
            row.append([])
        grid.append(row)
    i = 0
    while i < len(lines):
        line = lines[i]
        words = line.split(" ")
        sX = int(words[2][2:-1])
        sY = int(words[3][2:-1])
        bX = int(words[8][2:-1])
        bY = int(words[9][2:])
        dX = abs(sX - bX)
        dY = abs(sY - bY)
        dist = dX + dY
        avgDist += dist
        minCellX = max(0, (sX - dist) // cell)
        minCellY = max(0, (sY - dist) // cell)
        maxCellX = min(numCells - 1, (sX + dist) // cell)
        maxCellY = min(numCells - 1, (sY + dist) // cell)
        #print((sX, sY, dist), (minCellX, maxCellX), (minCellY, maxCellY))
        
        n = 0
        cX = minCellX
        while cX <= maxCellX:
            cY = minCellY
            while cY <= maxCellY:
                grid[cX][cY].append((sX, sY, dist, dX, dY))
                n += 1
                cY += 1
            cX += 1
        #print(dX, dY, minCellX, minCellY, maxCellX, maxCellY, n)
        i += 1
    
    z = []
    for i in range(numCells):
        for j in range(numCells):
            if(len(grid[i][j]) == 0):
                z.append((i, j))
    print("Z", z)
    
    toRemove = []
    toSearch = []
    for cX in range(numCells):
        for cY in range(numCells):
            minX = cX * cell
            maxX = min((cX + 1) * cell - 1, width)
            minY = cY * cell
            maxY = min((cY + 1) * cell - 1, width)
            good = True
            for k in grid[cX][cY]:
                # Check if manhattan diamond encloses square
                sDX = k[3] / 2 * math.sqrt(2)
                sDY = k[4] / 2 * math.sqrt(2)
                if k[0] - sDX < minX and maxX < k[0] + sDX and k[1] - sDY < minY and maxY < k[1] + sDY:
                    toRemove.append((cX, cY))
                    good = False
                    break
            if good:
                toSearch.append((cX, cY))
    print("TOREMOVE", len(toRemove), "OUT OF", numCells * numCells)
    for t in toRemove:
        grid[t[0]][t[1]] = None
    
    n = 0
    for t in toSearch:
        cX = t[0]
        cY = t[1]
        print(cX, cY)
        cells = grid[cX][cY]
        if cells is not None:
            minX = cX * cell
            maxX = min((cX + 1) * cell - 1, width)
            minY = cY * cell
            maxY = min((cY + 1) * cell - 1, width)
            x = minX
            while x <= maxX:
                y = minY
                while y <= maxY:
                    good = True
                    for s in cells:
                        dX = abs(x - s[0])
                        dY = abs(y - s[1])
                        dist = dX + dY
                        if dist <= s[2]:
                            if s[4] - dY > 0:
                                y += s[4] - dY - 1
                            good = False
                            break
                    if good:
                        print("ANS:", x, y, x * width + y)
                        return
                    y += 1
                x += 1
        n += 1
        print(n, "/", len(toSearch))

if __name__ == "__main__":
    main()