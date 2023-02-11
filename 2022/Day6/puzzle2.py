def all_unique(s):
    found = set()
    for ch in s:
        if ch in found:
            return False
        found.add(ch)
    return True
    
def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    index = 0
    n = 14
    line = lines[0]
    while index <= len(line) - n:
        if all_unique(line[index:index+n]):
            break
        index += 1
    print(index + n)

if __name__ == "__main__":
    main()