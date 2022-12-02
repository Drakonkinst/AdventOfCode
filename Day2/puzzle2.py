def answer(a, b):
    if a == "A":
        if b == "X":
            return "Z"
        if b == "Y":
            return "X"
        return "Y"
    if a == "B":
        if b == "X":
            return "X"
        if b == "Y":
            return "Y"
        return "Z"
    if a == "C":
        if b == "X":
            return "Y"
        if b == "Y":
            return "Z"
        return "X"
        
def outcome(b):
    if b == "X":
        return 0
    if b == "Y":
        return 3
    if b == "Z":
        return 6

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
        a = answer(opp, you)
        total += numPoints(a) + outcome(you)
    print(total)

if __name__ == "__main__":
    main()