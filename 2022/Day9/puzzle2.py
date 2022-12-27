def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    visited = set()
    visited.add((0, 0))
    headX = 0
    headY = 0
    tails = []
    tailDirs = []
    for i in range(9):
        tails.append((0, 0))
        tailDirs.append("")

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
            hX = headX
            hY = headY
            for j in range(len(tails)):
                tX = tails[j][0]
                tY = tails[j][1]
                aX = tX
                aY = tY
                dX = hX - tX
                dY = hY - tY
                
                dist = max(abs(dX), abs(dY))
                
                if dX > 1 and dY == 0:
                    aX += 1
                elif dX < -1 and dY == 0:
                    aX -= 1
                elif dY > 1 and dX == 0:
                    aY += 1
                elif dY < -1 and dX == 0:
                    aY -= 1
                elif dist > 1:
                    # Not touching and not in same row or column:
                    if dX > 0:
                        aX += 1
                    else:
                        aX -= 1
                    
                    if dY > 0:
                        aY += 1
                    else:
                        aY -= 1
                    
                tails[j] = (aX, aY)
                hX = aX
                hY = aY
            tail = tails[-1]
            visited.add((tail[0], tail[1]))
    print(tails)
    print(len(visited))

if __name__ == "__main__":
    main()