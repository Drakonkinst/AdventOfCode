s = "abcdefghijklmnopqrstuvwxyz" + ("abcdefghijklmnopqrstuvwxyz").upper()

def main():
    file = open("input.txt", "r");
    lines = file.readlines()
    lines[-1] += "\n"
    
    total = 0
    for line in lines:
        mid = len(line.strip()) // 2
        a = line[0:mid]
        b = line[mid:-1]
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