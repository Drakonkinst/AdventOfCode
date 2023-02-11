def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    grid = []
    bools = []
    for line in lines:
        row = []
        boolRow = []
        for ch in line:
            row.append(int(ch))
            boolRow.append(False)
        print(row)
        grid.append(row)
        bools.append(boolRow)

    i = 0
    total = 0
    while i < len(grid):
        j = -1
        while j < len(grid[0]) - 1:
            j += 1
            # Look towards i, j
            
            # Up
            k = 0
            maxSoFar = -1
            while k < i:
                if grid[k][j] > maxSoFar:
                    maxSoFar = grid[k][j]
                k += 1
            if k == i and grid[i][j] > maxSoFar:
                total += 1
                #print(i, j, "UP")
                continue
            
            # Down
            k = len(grid) - 1
            maxSoFar = -1
            while k > i:
                if grid[k][j] > maxSoFar:
                    maxSoFar = grid[k][j]
                k -= 1
            if k == i and grid[i][j] > maxSoFar:
                total += 1
                #print(i, j, "DOWN")
                continue
            
            # Left
            k = 0
            maxSoFar = -1
            while k < j:
                if grid[i][k] > maxSoFar:
                    maxSoFar = grid[i][k]
                k += 1
            if k == j and grid[i][j] > maxSoFar:
                #print(i, j, "LEFT")
                total += 1
                continue
            
            # Right
            k = len(grid[0]) - 1
            maxSoFar = -1
            while k > j:
                if grid[i][k] > maxSoFar:
                    maxSoFar = grid[i][k]
                k -= 1
            if k == j and grid[i][j] > maxSoFar:
                #print(i, j, "RIGHT")
                total += 1
                continue
        i += 1

    print(total)

if __name__ == "__main__":
    main()