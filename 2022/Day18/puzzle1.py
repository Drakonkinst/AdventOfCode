def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    cubes = set()
    
    for line in lines:
        nums = [int(x) for x in line.split(",")]
        cubes.add((nums[0], nums[1], nums[2]))
    
    offsets = [
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1)
    ]
    
    total = 0
    for xPos, yPos, zPos in cubes:
        for xOffset, yOffset, zOffset in offsets:
            x = xPos + xOffset
            y = yPos + yOffset
            z = zPos + zOffset
            if (x, y, z) not in cubes:
                total += 1
    print(total)
    
if __name__ == "__main__":
    main()