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
    while i < len(grid):
        maxVal = -1
        j = 0
        while j < len(grid[0]):
            if grid[i][j] > maxVal:
                bools[i][j] = True
                maxVal = grid[i][j]
            j += 1
        maxVal = -1
        j -= 1
        while j >= 0:
            if grid[i][j] > maxVal:
                bools[i][j] = True
                maxVal = grid[i][j]
            j -= 1
        i += 1
    i = 0
    while i < len(grid[0]):
        maxVal = -1
        j = 0
        while j < len(grid):
            if grid[j][i] > maxVal:
                bools[j][i] = True
                maxVal = grid[j][i]
            j += 1
        maxVal = -1
        j -= 1
        while j >= 0:
            if grid[j][i] > maxVal:
                bools[j][i] = True
                maxVal = grid[j][i]
            j -= 1
        i += 1
    
    total = 0
    for boolRow in bools:
        print(boolRow)
        for boolVal in boolRow:
            if boolVal:
                total += 1
    print(total)

if __name__ == "__main__":
    main()