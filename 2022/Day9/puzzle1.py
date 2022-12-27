def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    visited = set()
    visited.add((0, 0))
    headX = 0
    headY = 0
    tailX = 0
    tailY = 0
    for line in lines:
        cmd = line.split(" ")
        direction = cmd[0]
        value = int(cmd[1])
        firstMove = True
        for i in range(value):
            # Move head
            if direction == "R":
                headX += 1
            elif direction == "U":
                headY += 1
            elif direction == "L":
                headX -= 1
            elif direction == "D":
                headY -= 1
            
            # Move tail
            dist = max(abs(headX - tailX), abs(headY - tailY))
            if dist > 1:
                if direction == "R":
                    tailX = headX - 1
                    tailY = headY
                elif direction == "U":
                    tailX = headX
                    tailY = headY - 1
                elif direction == "L":
                    tailX = headX + 1
                    tailY = headY
                elif direction == "D":
                    tailX = headX
                    tailY = headY + 1
            visited.add((tailX, tailY))
    print((headX, headY))
    print(len(visited))

if __name__ == "__main__":
    main()