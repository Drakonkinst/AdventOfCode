

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    width = 200
    height = 200
    offsetX = -400
    offsetY = 0

    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        grid.append(row)

    i = 0
    while i < len(lines):
        line = lines[i]
        points = line.split(" -> ")
        coords = []
        for point in points:
            coord = point.split(",")
            x = int(coord[0]) + offsetX
            y = int(coord[1]) + offsetY
            #print(x, y)
            coords.append((x, y))
        
        for j in range(len(coords) - 1):
            a = coords[j]
            b = coords[j + 1]
            if a[0] == b[0]:
                start = a[1] if a[1] < b[1] else b[1]
                end = b[1] if a[1] < b[1] else a[1]
                while start <= end:
                    #print(a[0], start)
                    grid[start][a[0]] = 2
                    start += 1
            else:
                start = a[0] if a[0] < b[0] else b[0]
                end = b[0] if a[0] < b[0] else a[0]
                while start <= end:
                    #print(start, a[1])
                    grid[a[1]][start] = 2
                    start += 1
        i += 1
        
    done = False
    total = 0
    while not done:
        x = 500 + offsetX
        y = 0 + offsetY
        while True:
            if y + 1 >= height:
                done = True
                break
            if grid[y + 1][x] == 0:
                y += 1
            elif grid[y + 1][x - 1] == 0:
                y += 1
                x -= 1
            elif grid[y + 1][x + 1] == 0:
                y += 1
                x += 1
            else:
                break
        grid[y][x] = 1
        total += 1 
    #for r in grid:
        #print(r)
    print("TOTAL", total - 1)

if __name__ == "__main__":
    main()