from collections import deque

def main():
    file = open("input.txt", "r")
    lines = [line.strip() for line in file.readlines()][1:-1]
    
    n = 0
    width = len(lines[0]) - 2
    height = len(lines)
    left = [set() for _ in range(height)]
    right = [set() for _ in range(height)]
    up = [set() for _ in range(width)]
    down = [set() for _ in range(width)]
    
    def is_cell_open(x, y, timePlusOne):
        # We assume no blizzards ever reach start or end
        if x == 0 and y == -1:
            return True
        if x == width - 1 and y == height:
            return True
        if not (0 <= x < width and 0 <= y < height):
            return False
        # Pad for modulo
        heightPadding = timePlusOne * height
        widthPadding = timePlusOne * width
        if (x + timePlusOne + widthPadding) % width in left[y]:
            return False
        if (x - timePlusOne + widthPadding) % width in right[y]:
            return False
        if (y + timePlusOne + heightPadding) % height in up[x]:
            return False
        if (y - timePlusOne + heightPadding) % height in down[x]:
            return False
        return True
    
    def printBoard(time):
        s = str(time) + "\n"
        heightPadding = time * height
        widthPadding = time * width
        for y in range(0, height):
            for x in range(0, width):
                arr = []
                if (x + time + widthPadding) % width in left[y]:
                    arr.append("<")
                if (x - time + widthPadding) % width in right[y]:
                    arr.append(">")
                if (y + time + heightPadding) % height in up[x]:
                    arr.append("^")
                if (y - time + heightPadding) % height in down[x]:
                    arr.append("v")
                if len(arr) == 0:
                    s += "."
                elif len(arr) == 1:
                    s += arr[0]
                else:
                    s += str(len(arr))
            s += "\n"
        print(s)
    
    for y in range(len(lines)):
        line = lines[y][1:-1]
        x = 0
        for ch in line:
            if ch == '>':
                right[y].add(x)
            elif ch == '<':
                left[y].add(x)
            elif ch == '^':
                up[x].add(y)
            elif ch == 'v':
                down[x].add(y)
            x += 1
    
    # Start to End
    q = deque()
    visited = set()
    startState = (1, 0, -1)
    q.append(startState)
    visited.add(startState)
    finalMinute = -1
    
    neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0], [0, 0]]
    while len(q) > 0:
        minute, x, y = q.popleft()
        
        if x == width - 1 and y == height:
            finalMinute = minute - 1
            break
        for offset in neighbors:
            nextX = x + offset[0]
            nextY = y + offset[1]
            if is_cell_open(nextX, nextY, minute):
                state = (minute + 1, nextX, nextY)
                if state not in visited:
                    visited.add(state)
                    q.append(state)
    assert finalMinute > -1
    print("A", finalMinute)

    # End to Start
    q = deque()
    visited = set()
    startState = (finalMinute, width - 1, height)
    q.append(startState)
    visited.add(startState)
    finalMinute = -1
    
    neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0], [0, 0]]
    while len(q) > 0:
        minute, x, y = q.popleft()
        
        if x == 0 and y == -1:
            finalMinute = minute - 1
            break
        for offset in neighbors:
            nextX = x + offset[0]
            nextY = y + offset[1]
            if is_cell_open(nextX, nextY, minute):
                state = (minute + 1, nextX, nextY)
                if state not in visited:
                    visited.add(state)
                    q.append(state)
    assert finalMinute > -1
    print("B", finalMinute)
    
    # Start to End (Again)
    q = deque()
    visited = set()
    startState = (finalMinute, 0, -1)
    q.append(startState)
    visited.add(startState)
    finalMinute = -1
    
    neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0], [0, 0]]
    while len(q) > 0:
        minute, x, y = q.popleft()
        
        if x == width - 1 and y == height:
            finalMinute = minute - 1
            break
        for offset in neighbors:
            nextX = x + offset[0]
            nextY = y + offset[1]
            if is_cell_open(nextX, nextY, minute):
                state = (minute + 1, nextX, nextY)
                if state not in visited:
                    visited.add(state)
                    q.append(state)
    assert finalMinute > -1
    print("ANS", finalMinute)
if __name__ == "__main__":
    main()