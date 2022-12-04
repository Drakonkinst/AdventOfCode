def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    total = 0
    for line in lines:
        items = line.split(",")
        pair1 = items[0].split("-")
        pair2 = items[1].split("-")
        #print(pair1)
        #print(pair2)
        a = int(pair1[0])
        b = int(pair1[1])
        c = int(pair2[0])
        d = int(pair2[1])
        #print(a, b, c, d)
        if a <= c and d <= b:
            total += 1
        elif c <= a and b <= d:
            total += 1
    print(total)

if __name__ == "__main__":
    main()