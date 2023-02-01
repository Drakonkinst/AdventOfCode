import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

shop = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

bossStats = """
Hit Points: 100
Damage: 8
Armor: 2
"""

playerHp = 100

def parse(data):
    result = []
    for line in data.splitlines():
        nums = ints(line)
        if len(nums) < 3:
            continue
        result.append((nums[-3], nums[-2], nums[-1]))
    return result

def calcStatsFromIndex(wi, ai, r1i, r2i, weapons, armor, rings):
    w = weapons[wi]
    a = None
    r1 = None
    r2 = None
    
    if ai > -1:
        a = armor[ai]
    if r1i > -1:
        r1 = rings[r1i]
    if r2i > -1:
        r2 = rings[r2i]
    
    return calcStats(w, a, r1, r2)

def calcStats(w, a = None, r1 = None, r2 = None):
    cost = w[0]
    dmg = w[1]
    armor = w[2]
    
    if a is not None:
        cost += a[0]
        dmg += a[1]
        armor += a[2]
        
    if r1 is not None:
        cost += r1[0]
        dmg += r1[1]
        armor += r1[2]
    
    if r2 is not None:
        cost += r2[0]
        dmg += r2[1]
        armor += r2[2]
    return (cost, dmg, armor)

def wins(boss, player):
    playerDmg = max(0, player[1] - boss[2])
    bossDmg = max(0, boss[1] - player[2])
    playerHealth = playerHp
    bossHealth = boss[0]
    playerTurns = sys.maxsize if bossDmg == 0 else playerHealth // bossDmg
    bossTurns = sys.maxsize if playerDmg == 0 else bossHealth // playerDmg
    return playerTurns >= bossTurns

def valid_build(wi, ai, r1i, r2i):
    return r1i < 0 or r1i != r2i

def main():
    data = shop.split("\n\n")
    weapons = parse(data[0])
    armor = parse(data[1])
    rings = parse(data[2])
    
    # Sort by cost
    weapons.sort(reverse=True)
    armor.sort(reverse=True)
    rings.sort(reverse=True)
    
    boss = tuple(ints(bossStats))
    q = deque([(0, -1, -1, -1)])
    v = set()
    maxCost = -sys.maxsize
    while len(q) > 0:
        equipment = q.pop()
        
        if equipment in v:
            continue
        v.add(equipment)
        
        wi, ai, r1i, r2i = equipment
        if not valid_build(wi, ai, r1i, r2i):
            continue
            
        player = calcStatsFromIndex(wi, ai, r1i, r2i, weapons, armor, rings)
        cost = player[0]
        if cost < maxCost:
            continue
        
        if not wins(boss, player):
            if cost > maxCost:
                maxCost = cost
        # Try incrementing all indices by 1
        if wi < len(weapons) - 1:
            q.append((wi + 1, ai, r1i, r2i))
        
        if ai < len(armor) - 1:
            q.append((wi, ai + 1, r1i, r2i))
            
        if r1i < len(rings) - 1:
            q.append((wi, ai, r1i + 1, r2i))
            
        if r2i < len(rings) - 1:
            q.append((wi, ai, r1i, r2i + 1))
    print(maxCost)

if __name__ == "__main__":
    main()