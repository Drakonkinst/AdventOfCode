import sys
import math

# Inspired by hyper-neutrino's solution
# I do not claim credit for solving this problem, and the following
# code is for learning purposes only.
def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    sensors = []
    width = 4000000
    every = 100000
    
    for line in lines:
        words = line.split(" ")
        sX = int(words[2][2:-1])
        sY = int(words[3][2:-1])
        bX = int(words[8][2:-1])
        bY = int(words[9][2:])
        sensors.append((sX, sY, bX, bY))
            
    for y in range(width + 1):
        #print("Y", y)
        intervals = []
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
        
        x = 0
        for minX, maxX in q:
            #print("X", x)
            if x < minX:
                print("ANS", x * width + y)
                return
            
            x = max(x, maxX + 1)
            if x >= width + 1:
                break
        if y % every == 0:
            print(y)

if __name__ == "__main__":
    main()