import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")

def main():
    # State:
    # mana, hp, shieldEffect, poisonEffect, rechargeEffect, bossHealth, manaSpent, playerTurn
    bossHealth, bossDamage = ints(file.read())
    q = deque([(500, 50, 0, 0, 0, bossHealth, 0, True)])

    magicMissile = 53
    drain = 73
    shield = 113
    poison = 173
    recharge = 229
    minCost = min(magicMissile, drain, shield, poison, recharge)
    v = set()
    
    while len(q) > 0:
        state = q.popleft()
        if state in v:
            continue
        v.add(state)
        mana, hp, shieldEffect, poisonEffect, rechargeEffect, bossHp, manaSpent, playerTurn = state
        
        # Resolve effects
        if shieldEffect > 0:
            shieldEffect -= 1

        if poisonEffect > 0:
            bossHp -= 3
            poisonEffect -= 1
            
        if rechargeEffect > 0:
            mana += 101
            rechargeEffect -= 1
        
        # Hard mode
        if playerTurn:
            hp -= 1
        
        # Check win and lose conditions
        if hp <= 0 or mana < minCost:
            continue

        if bossHp <= 0:
            print("WIN", manaSpent)
            return
        
        if playerTurn:
            # Think about casting each spell
            if mana > magicMissile:
                q.append((mana - magicMissile, hp, shieldEffect, poisonEffect, rechargeEffect, bossHp - 4, manaSpent + magicMissile, not playerTurn))
            if mana > drain:
                q.append((mana - drain, hp + 2, shieldEffect, poisonEffect, rechargeEffect, bossHp - 2, manaSpent + drain, not playerTurn))
            if mana > shield and shieldEffect <= 0:
                q.append((mana - shield, hp, 6, poisonEffect, rechargeEffect, bossHp, manaSpent + shield, not playerTurn))
            if mana > poison and poisonEffect <= 0:
                q.append((mana - poison, hp, shieldEffect, 6, rechargeEffect, bossHp, manaSpent + poison, not playerTurn))
            if mana > recharge and rechargeEffect <= 0:
                q.append((mana - recharge, hp, shieldEffect, poisonEffect, 5, bossHp, manaSpent + recharge, not playerTurn))
        else:
            # Boss turn
            dmg = bossDamage
            if shieldEffect > 0:
                dmg = max(1, bossDamage - 7)
            hp -= dmg
            q.append((mana, hp, shieldEffect, poisonEffect, rechargeEffect, bossHp, manaSpent, not playerTurn))
        
if __name__ == "__main__":
    main()