s = "abcdefghijklmnopqrstuvwxyz" + ("abcdefghijklmnopqrstuvwxyz").upper()

def main():
    file = open("input.txt", "r");
    
    total = 0
    while True:
        a = file.readline()
        b = file.readline()
        c = file.readline()
        if not c:
            break
        #print(a, b, c)
        onlyA = set()
        for aChar in a:
            if aChar != '\n':
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