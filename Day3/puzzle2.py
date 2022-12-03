s = "abcdefghijklmnopqrstuvwxyz" + ("abcdefghijklmnopqrstuvwxyz").upper()

def main():
    file = open("input.txt", "r");
    
    total = 0
    while True:
        a = file.readline().strip()
        b = file.readline().strip()
        c = file.readline().strip()
        if not c:
            break
        #print(a, b, c)
        onlyA = set()
        for aChar in a:
            onlyA.add(aChar)
        aAndB = set()
        for bChar in b:
            if bChar in onlyA:
                aAndB.add(bChar)
        for cChar in c:
            if cChar in aAndB:
                #print(cChar)
                total += s.index(cChar) + 1
                break
    print(total)

if __name__ == "__main__":
    main()