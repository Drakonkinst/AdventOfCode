s = "abcdefghijklmnopqrstuvwxyz" + ("abcdefghijklmnopqrstuvwxyz").upper()

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    total = 0
    for line in lines:
        mid = len(line.strip()) // 2
        a = line[:mid]
        b = line[mid:]
        aChars = set()
        for aChar in a:
            aChars.add(aChar)
        for bChar in b:
            if bChar in aChars:
                total += s.index(bChar) + 1
                #print(s.index(bChar) + 1)
                break
    print(total)

if __name__ == "__main__":
    main()