
# Inspired by hyper-neutrino's solution

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]

    i = 0
    s = set()
    maxHeight = 0
    while i < len(lines):
        line = lines[i]
        points = line.split(" -> ")
        coords = []
        for point in points:
            coord = point.split(",")
            x = int(coord[0])
            y = int(coord[1])
            maxHeight = max(maxHeight, y)
            coords.append((x, y))
        
        for j in range(len(coords) - 1):
            a = coords[j]
            b = coords[j + 1]
            if a[0] == b[0]:
                start = a[1] if a[1] < b[1] else b[1]
                end = b[1] if a[1] < b[1] else a[1]
                while start <= end:
                    s.add((a[0], start))
                    start += 1
            else:
                start = a[0] if a[0] < b[0] else b[0]
                end = b[0] if a[0] < b[0] else a[0]
                while start <= end:
                    s.add((start, a[1]))
                    start += 1
        i += 1
        
    total = 0
    maxHeight += 2
    while (500, 0) not in s:
        x = 500
        y = 0
        while True:
            if y + 1 >= maxHeight:
                break
            if (x, y + 1) not in s:
                y += 1
            elif (x - 1, y + 1) not in s:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in s:
                y += 1
                x += 1
            else:
                break
        s.add((x, y))
        total += 1
    print("TOTAL", total)

if __name__ == "__main__":
    main()