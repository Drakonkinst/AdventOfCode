import json
from functools import cmp_to_key

def compareH(l, r):
    return compare(l[0], r[0])

def compare(l, r):
    li = 0
    ri = 0
    if type(l) == int and type(r) == int:
        if l < r:
            return 1
        elif l > r:
            return -1
    elif type(l) != int and type(r) != int:
        n = min(len(l), len(r))
        for i in range(n):
            res = compare(l[i], r[i])
            if res != 0:
                return res
        if len(l) < len(r):
            return 1
        if len(l) > len(r):
            return -1
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
    packets = []
    for line in lines:
        if len(line) <= 0:
            continue
        packet = json.loads(line)
        packets.append(packet)
    packets.append([[2]])
    packets.append([[6]])
    s = sorted(packets, key = cmp_to_key(compare))

    total = 1
    for i in range(len(s)):
        v = s[i]
        n = len(s) - i
        if v == [[2]] or v == [[6]]:
            total *= n
    print(total)

if __name__ == "__main__":
    main()