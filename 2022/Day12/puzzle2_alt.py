elev = "abcdefghijklmnopqrstuvwxyz"

def canMove(a, b):
    return b - a <= 1

def main():
    file = open("input.txt", "r")
    lines = [line.strip() for line in file.readlines()]
    
    x = 0
    y = 0
    grid = []
    S = []
    E = None
    for line in lines:
        row = []
        x = 0
        for ch in line:
            if ch == "S" or ch == "a":
                S.append((x, y))
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
    for s in S:
        queue.append((s, 0))
        visited.add(s)
    shortestPath = None
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while len(queue) > 0:
        item = queue.pop(0)
        x = item[0][0]
        y = item[0][1]
        steps = item[1]
        val = grid[y][x]
        if x == E[0] and y == E[1]:
            shortestPath = steps
            break
        
        for n in neighbors:
            newX = x + n[0]
            newY = y + n[1]
            if newX < 0 or newY < 0 or newX >= len(grid[0]) or newY >= len(grid):
                continue
            if (newX, newY) in visited:
                continue
            newVal = grid[newY][newX]
            if (newVal - val) <= 1:
                queue.append(((newX, newY), steps + 1))
                visited.add((newX, newY))
    print(shortestPath)
    

if __name__ == "__main__":
    main()