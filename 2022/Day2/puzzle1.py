def whoWins(a, b):
    if a == "A":
        if b == "X":
            return 3
        if b == "Y":
            return 6
        return 0
    if a == "B":
        if b == "X":
            return 0
        if b == "Y":
            return 3
        return 6
    if a == "C":
        if b == "X":
            return 6
        if b == "Y":
            return 0
        return 3

def numPoints(a):
    if a == "X":
        return 1
    if a == "Y":
        return 2
    return 3

def main():
    file = open("input.txt", "r");
    lines = file.readlines()
    
    total = 0
    for line in lines:
        arr = line.split(" ")
        opp = arr[0].strip()
        you = arr[1].strip()
        total += numPoints(you) + whoWins(opp, you)
    print(total)

if __name__ == "__main__":
    main()