def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    total = 0
    for line in lines:
        items = line.split(",")
        pair1 = items[0].split("-")
        pair2 = items[1].split("-")
        a = int(pair1[0])
        b = int(pair1[1])
        c = int(pair2[0])
        d = int(pair2[1])
        
        if (a <= c <= b) or (a <= d <= b) or (c <= a <= d) or (c <= b <= d):
            total += 1
    print(total)

if __name__ == "__main__":
    main()