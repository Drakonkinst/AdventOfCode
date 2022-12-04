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
        setA = set()
        setB = set()
        setC = set()
        for aChar in a:
            setA.add(aChar)
        for bChar in b:
            setB.add(bChar)
        for cChar in c:
            setC.add(cChar)
        allThree = setA.intersection(setB.intersection(setC))
        for ch in allThree:
            total += s.index(ch) + 1
    print(total)

if __name__ == "__main__":
    main()