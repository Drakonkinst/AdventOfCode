abc = "ABC"
xyz = "XYZ"
M = [
    ["Z", "X", "Y"],
    ["X", "Y", "Z"],
    ["Y", "Z", "X"]
]

def answer(a, b):
    return M[abc.index(a)][xyz.index(b)]
        
def outcomePoints(a):
    return xyz.index(a) * 3

def numPoints(a):
    return xyz.index(a) + 1

def main():
    file = open("input.txt", "r");
    lines = file.readlines()
    
    total = 0
    for line in lines:
        arr = line.split(" ")
        opp = arr[0].strip()
        outcome = arr[1].strip()
        you = answer(opp, outcome)
        total += numPoints(you) + outcomePoints(outcome)
    print(total)

if __name__ == "__main__":
    main()