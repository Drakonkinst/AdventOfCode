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
        # Create list of intervals for this value of Y only
        intervals = []
        for sX, sY, bX, bY in sensors:
            dX = abs(sX - bX)
            dY = abs(sY - bY)
            dist = dX + dY
            # Calculate how long the interval must be at this Y value, possible
            # since this is manhattan distance
            intervalAtY = dist - abs(sY - y)
            
            if intervalAtY < 0:
                continue
            
            minX = sX - intervalAtY
            maxX = sX + intervalAtY
            intervals.append((minX, maxX))
        # Sort intervals - critical for compression algorithm so it knows it can move on
        # Sorts by minX first, then maxX. minX sorting is the most important here
        # Since it is used to determine if a new interval should start
        intervals.sort()
        
        # Interval compression algorithm
        q = []
        for minX, maxX in intervals:
            # No other intervals, add
            if len(q) <= 0:
                q.append([minX, maxX])
                continue

            currMin = q[-1][0]
            currMax = q[-1][1]
            
            # Check if this can extend the current interval
            # Or if it needs to be a new one
            if minX > currMax + 1:
                q.append([minX, maxX])
                continue
            # Extend current interval
            q[-1][1] = max(currMax, maxX)
        
        x = 0
        for minX, maxX in q:
            if x < minX:
                print("ANS", x * width + y)
                return
            
            x = maxX + 1
            if x > width:
                break
        
        # Show progress
        if y % every == 0:
            print(y)

if __name__ == "__main__":
    main()