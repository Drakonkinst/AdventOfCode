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
    queue.append((S, 0))
    visited.add(S)
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
        
        
    print(shortestPath)
    

if __name__ == "__main__":
    main()