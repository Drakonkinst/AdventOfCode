import json

def compare(l, r):
    li = 0
    ri = 0
    if type(l) == int and type(r) == int:
        if l < r:
            return 2
        elif l > r:
            return 1
    elif type(l) != int and type(r) != int:
        n = min(len(l), len(r))
        for i in range(n):
            res = compare(l[i], r[i])
            if res != 0:
                return res
        if len(l) < len(r):
            return 2
        if len(l) > len(r):
            return 1
    elif type(l) == int:
        res = compare([l], r)
        if res != 0:
            return res
    elif type(r) == int:
        res = compare(l, [r])
        if res != 0:
            return res
    return 0

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    i = 0
    n = 1
    corr = []
    while i < len(lines):
        left = json.loads(lines[i])
        right = json.loads(lines[i + 1])
        
        if compare(left, right) == 2:
            corr.append(n)
        n += 1
        i += 3
    print(corr)
    print(sum(corr))

if __name__ == "__main__":
    main()