from collections import deque
import sys

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    cubes = set()
    minX = sys.maxsize
    maxX = -sys.maxsize
    minY = sys.maxsize
    maxY = -sys.maxsize
    minZ = sys.maxsize
    maxZ = -sys.maxsize
    
    for line in lines:
        nums = [int(x) for x in line.split(",")]
        x = nums[0]
        y = nums[1]
        z = nums[2]
        minX = min(x, minX)
        minY = min(y, minY)
        minZ = min(z, minZ)
        maxX = max(x, maxX)
        maxY = max(y, maxY)
        maxZ = max(z, maxZ)
        cubes.add((x, y, z))
    
    offsets = [
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1)
    ]
    
    possible = {}
    total = 0
    for xPos, yPos, zPos in cubes:
        for xOffset, yOffset, zOffset in offsets:
            x = xPos + xOffset
            y = yPos + yOffset
            z = zPos + zOffset
            if (x, y, z) not in cubes:
                if (x, y, z) in possible:
                    possible[(x, y, z)] += 1
                else:
                    possible[(x, y, z)] = 1
                total += 1

    allNotEnclosed = set()
    numNotEnclosed = 0
    for xPos, yPos, zPos in possible.keys():
        enclosed = True
        q = deque()
        v = set()
        q.append((xPos, yPos, zPos))
        steps = 0
        while len(q) > 0:
            steps += 1
            x, y, z = q.pop()
            if (x, y, z) in cubes:
                continue
            v.add((x, y, z))
            if (x, y, z) in allNotEnclosed:
                enclosed = False
                break
            if x < minX or y < minY or z < minZ or x > maxX or y > maxY or z > maxZ:
                enclosed = False
                break
            for xOffset, yOffset, zOffset in offsets:
                if (x + xOffset, y + yOffset, z + zOffset) not in v:
                    q.append((x + xOffset, y + yOffset, z + zOffset))
        print((xPos, yPos, zPos), steps, enclosed)
        if not enclosed:
            allNotEnclosed.update(v)
            numNotEnclosed += possible[(xPos, yPos, zPos)]
    print(len(possible), total, numNotEnclosed)
    
if __name__ == "__main__":
    main()