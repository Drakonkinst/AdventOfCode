elev = "abcdefghijklmnopqrstuvwxyz"

def canMove(a, b):
    return b - a <= 1

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    x = 0
    y = 0
    grid = []
    S = None
    E = None
    for line in lines:
        row = []
        x = 0
        for ch in line:
            if ch == "S":
                S = (x, y)
                row.append(elev.index("a"))
            elif ch == "E":
                E = (x, y)
                row.append(elev.index("z"))
            else:
                row.append(elev.index(ch))
            x += 1
        y += 1
        grid.append(row)
    
    # Breadth-first search
    queue = []
    visited = set()
    queue.add((S, 0))
    visited.add(S)
    shortestPath = None
    while len(queue) > 0:
        item = queue.pop(0)
        x = item[0][0]
        y = item[0][1]
        steps = item[1]
        val = grid[y][x]
        if x == E[0] and y == E[1]:
            shortestPath = steps
            break
        
        # Up
        if y - 1 >= 0 and canMove(val, grid[y - 1][x]) and (x, y - 1) not in visited:
            queue.append(((x, y - 1), steps + 1))
            visited.add((x, y - 1))
        # Down
        if y + 1 < len(grid) and canMove(val, grid[y + 1][x]) and (x, y + 1) not in visited:
            queue.append(((x, y + 1), steps + 1))
            visited.add((x, y + 1))
        
        # Left
        if x - 1 >= 0 and canMove(val, grid[y][x - 1]) and (x - 1, y) not in visited:
            queue.append(((x - 1, y), steps + 1))
            visited.add((x - 1, y))
        
        # Right
        if x + 1 < len(grid[0]) and canMove(val, grid[y][x + 1]) and (x + 1, y) not in visited:
            queue.append(((x + 1, y), steps + 1))
            visited.add((x + 1, y))
    print(shortestPath)
    

if __name__ == "__main__":
    main()