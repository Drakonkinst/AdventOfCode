from collections import deque

MAX_DEPTH = 24

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    i = 0
    total = 0
    for line in lines:
        words = line.split(" ")

        name = int(words[1][:-1])
        oreOre = int(words[6])
        clayOre = int(words[12])
        obsidianOre = int(words[18])
        obsidianClay = int(words[21])
        geodeOre = int(words[27])
        geodeObsidian = int(words[30])
        
        q = deque()
        q.append((0, 1, 0, 0, 0, 0, 0, 0, 0, True, True, False, False))
        maxVal = 0
        bestPerStep = []
        for _ in range(MAX_DEPTH):
            bestPerStep.append(0)
        
        n = 0
        visited = set()
        while len(q) > 0:
            x = q.pop()
            n += 1
            # if x in visited:
            #     continue   
            # visited.add(x)
            
            step, oreBot, clayBot, obsidianBot, geodeBot, ore, clay, obsidian, geode, willBuildOre, willBuildClay, willBuildObsidian, willBuildGeode = x
            
            if step >= MAX_DEPTH:
                if geode > maxVal:
                    maxVal = geode
                    print("NEW MAX", maxVal, n, (oreBot, clayBot, obsidianBot, geodeBot), (ore, clay, obsidian, geode))
                continue
        
            if ore < 0 or clay < 0 or obsidian < 0 or geode < 0:
                print("ERROR", step, (oreBot, clayBot, obsidianBot, geodeBot), (ore, clay, obsidian, geode))
                return
            
            y = (oreBot, clayBot, obsidianBot, geodeBot, ore, clay, obsidian, geode)
            if y in visited:
                continue
            visited.add(y)
            
            minutesLeft = MAX_DEPTH - step
            geodesPossible = geode + geodeBot * minutesLeft + ((minutesLeft) * (minutesLeft - 1) // 2)
            
            if geodesPossible < bestPerStep[step]:
                continue
            if geode > bestPerStep[step]:
                bestPerStep[step] = geode
            
            nextOre = ore + oreBot
            nextClay = clay + clayBot
            nextObsidian = obsidian + obsidianBot
            nextGeode = geode + geodeBot
            
            canBuildOre = ore >= oreOre
            canBuildClay = ore >= clayOre
            canBuildObsidian = ore >= obsidianOre and clay >= obsidianClay
            canBuildGeode = ore >= geodeOre and obsidian >= geodeObsidian
            
            shouldBuildOre = oreBot < oreOre or oreBot < clayOre or oreBot < obsidianOre or oreBot < geodeOre
            shouldBuildClay = clayBot < obsidianClay
            shouldBuildObsidian = obsidianBot < geodeObsidian
            
            toAdd = []
            if willBuildGeode and canBuildGeode:
                toAdd.append((step + 1, oreBot, clayBot, obsidianBot, geodeBot + 1, nextOre - geodeOre, nextClay, nextObsidian - geodeObsidian, nextGeode, True, True, True, True))
                willBuildGeode = False
            
            if willBuildObsidian and canBuildObsidian and shouldBuildObsidian:
                toAdd.append((step + 1, oreBot, clayBot, obsidianBot + 1, geodeBot, nextOre - obsidianOre, nextClay - obsidianClay, nextObsidian, nextGeode, True, True, True, True))
                willBuildObsidian = False
            
            if willBuildClay and canBuildClay and shouldBuildClay:
                toAdd.append((step + 1, oreBot, clayBot + 1, obsidianBot, geodeBot, nextOre - clayOre, nextClay, nextObsidian, nextGeode, True, True, True, True))
                willBuildClay = False

            if willBuildOre and canBuildOre and shouldBuildOre:
                toAdd.append((step + 1, oreBot + 1, clayBot, obsidianBot, geodeBot, nextOre - oreOre, nextClay, nextObsidian, nextGeode, True, True, True, True))
                willBuildOre = False
                
            # Can always do nothing
            toAdd.append((step + 1, oreBot, clayBot, obsidianBot, geodeBot, nextOre, nextClay, nextObsidian, nextGeode, willBuildOre, willBuildClay, willBuildObsidian, willBuildGeode))
            for x in reversed(toAdd):
                q.append(x)
            
        quality = name * maxVal
        total += quality
        i += 1
        print("NAME", name, "MAX", maxVal, "QUALITY", quality, "TOTAL", total)
    print("FINAL TOTAL", total)

if __name__ == "__main__":
    main()