abc = "ABC"
xyz = "XYZ"
M = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

def whoWins(a, b):
    return M[abc.index(a)][xyz.index(b)]

def numPoints(a):
    return xyz.index(a) + 1

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