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
    maxFound = -1
    while i < len(grid):
        j = 0
        while j < len(grid[0]):
            # Look from i, j
            
            # Up
            k = i - 1
            up = 0
            while k >= 0:
                up += 1
                if grid[k][j] >= grid[i][j]:
                    break
                k -= 1
            
            # Down
            k = i + 1
            down = 0
            while k < len(grid):
                down += 1
                if grid[k][j] >= grid[i][j]:
                    break
                k += 1
            
            # Left
            k = j - 1
            left = 0
            while k >= 0:
                left += 1
                if grid[i][k] >= grid[i][j]:
                    break
                k -= 1
            
            # Right
            k = j + 1
            right = 0
            while k < len(grid[0]):
                right += 1
                if grid[i][k] >= grid[i][j]:
                    break
                k += 1
            
            score = up * down * left * right
            if score > maxFound:
                maxFound = score
            j += 1
        i+= 1

    print(maxFound)

if __name__ == "__main__":
    main()