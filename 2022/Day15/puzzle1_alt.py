import sys
import math

# Inspired by hyper-neutrino's solution
# I do not claim credit for solving this problem, and the following
# code is for learning purposes only.
def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    sensors = []
    y = 2000000
    
    for line in lines:
        words = line.split(" ")
        sX = int(words[2][2:-1])
        sY = int(words[3][2:-1])
        bX = int(words[8][2:-1])
        bY = int(words[9][2:])
        sensors.append((sX, sY, bX, bY))
            
    intervals = []
    known = set()
    for sX, sY, bX, bY in sensors:
        dX = abs(sX - bX)
        dY = abs(sY - bY)
        dist = dX + dY
        intervalAtY = dist - abs(sY - y)
        
        if intervalAtY < 0:
            continue
        
        minX = sX - intervalAtY
        maxX = sX + intervalAtY
        intervals.append((minX, maxX))
        
        if bY == y:
            known.add(bX)
    intervals.sort()
    
    q = []
    for minX, maxX in intervals:
        if len(q) <= 0:
            q.append([minX, maxX])
            continue
        currMin = q[-1][0]
        currMax = q[-1][1]
        if minX > currMax + 1:
            q.append([minX, maxX])
            continue
        q[-1][1] = max(currMax, maxX)
    
    cannot = set()
    for minX, maxX in q:
        for x in range(minX, maxX + 1):
            cannot.add(x)
    print(len(cannot - known))

if __name__ == "__main__":
    main()