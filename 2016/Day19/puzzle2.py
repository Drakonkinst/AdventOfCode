import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyDeque:
    def __init__(self):
        self.front = None
        self.back = None
        self.middle = None
        self.count = 0
    
    def init(self, data):
        node = Node(data)
        self.front = node
        self.back = node
        self.middle = node
        self.count = 1
        
    def clear(self):
        self.front = None
        self.back = None
        self.middle = None
        self.count = 0
        
    def append(self, data):
        # Special case: n = 0 and n = 1
        if self.empty():
            self.init(data)
            return
        
        # Add node and change pointers as normal
        node = Node(data)
        self.back.next = node
        node.prev = self.back
        self.back = node
        self.count += 1
        
        # Also change middle pointer if needed
        if self.count % 2 == 0:
            self.middle = self.middle.next
        
    def appendleft(self, data):
        # Special case: n = 0
        if self.empty():
            self.init(data)
            return
        
        # Add node and change pointers as normal
        node = Node(data)
        self.front.prev = node
        node.next = self.front
        self.front = node
        self.count += 1
        
        # Also change middle pointer if needed
        if self.count % 2 == 0:
            self.middle = self.middle.next
    
    def pop(self):
        # Special cases: n = 0 and n = 1
        if self.empty():
            return None
        data = self.back.data
        if self.count == 1:
            self.clear()
            return data
        
        # Change normal front/back pointers
        self.back.prev.next = None
        self.back = self.back.prev
        self.count -= 1
        
        # Also change middle pointer if needed
        if self.count % 2 != 0:
            self.middle = self.middle.prev
        return data
    
    def popleft(self):
        # Special cases: n = 0 and n = 1
        if self.empty():
            return None
        data = self.front.data
        if self.count == 1:
            self.clear()
            return data
        
        # Change normal front/back pointers
        self.front.next.prev = None
        self.front = self.front.next
        self.count -= 1
        
        # Also change middle pointer if needed
        if self.count % 2 != 0:
            self.middle = self.middle.next
        return data
    
    def popmiddle(self):
        # Special cases: n = 0, n = 1, n = 2
        if self.empty():
            return None
        data = self.middle.data
        if self.count == 1:
            self.clear()
            return data
        if self.middle == self.front:
            return self.popleft()
        
        self.middle.prev.next = self.middle.next
        self.middle.next.prev = self.middle.prev
        self.count -= 1
        
        if self.count % 2 == 0:
            self.middle = self.middle.prev
        else:
            self.middle = self.middle.next

        return data
        
        return data
    
    def empty(self):
        return self.count <= 0
        
    def __str__(self):
        if self.empty():
            return "[]"
        curr = self.front
        items = [self.front.data]
        while curr != self.back:
            curr = curr.next
            items.append(curr.data)
        return str(items)
    
    def __len__(self):
        return self.count
        
        
def main():
    numElves = int(lines[0])
    #numElves = 7
    elves = MyDeque()
    
    print("Creating deque")
    for i in range(numElves):
        elves.append(i + 1)
    print("Deque created")
    assert elves.middle.data == numElves // 2 + 1
    
    # Loop until there are only 2 Elves left
    #print("START", elves)
    while len(elves) > 2:
        elves.popmiddle()
        #print("POPMIDDLE", elves)
        # Rotate to the left
        elves.append(elves.popleft())
        #print("ROTATE", elves)
        if len(elves) % 100000 == 0:
            print(len(elves))
    print("FINAL TWO", elves)
    # The leftmost elf always win
    print("ANS", elves.popleft())
    

if __name__ == "__main__":
    main()