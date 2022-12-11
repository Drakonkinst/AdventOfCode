class Monkey:
    def __init__(self, num, items, isAdd, isSelf, byValue, test, ifTrue, ifFalse):
        self.num = num
        self.items = items
        self.isAdd = isAdd
        self.isSelf = isSelf
        self.byValue = byValue
        self.test = test
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.count = 0
    
    def doThing(self, monkeys):
        toRemove = []
        for item in self.items:
            worry = item
            value = self.byValue
            if self.isSelf:
                value = item
            if self.isAdd:
                worry += value
            else:
                worry *= value
            worry //= 3
            if worry % self.test == 0:
                if self.ifTrue != self.num:
                    monkeys[self.ifTrue].items.append(worry)
                    toRemove.append(item)
            else:
                if self.ifFalse != self.num:
                    monkeys[self.ifFalse].items.append(worry)
                    toRemove.append(item)
            self.count += 1
        for item in toRemove:
            self.items.remove(item)

def make_monkey(lines):
    num = int(lines[0][len("Monkey ")])
    itemsStr = lines[1][len("Starting items: "):]
    items = [int(i) for i in itemsStr.split(", ")]
    opArgs = lines[2].split(" ")
    isAdd = opArgs[4] == "+"
    
    isSelf = opArgs[-1] == "old"
    if isSelf:
        byValue = -9999
    else:
        byValue = int(opArgs[-1])
    
    test = int(lines[3].split(" ")[-1])
    ifTrue = int(lines[4].split(" ")[-1])
    ifFalse = int(lines[5].split(" ")[-1])
    return Monkey(num, items, isAdd, isSelf, byValue, test, ifTrue, ifFalse)
        
def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    monkeys = []
    i = 0
    while i < len(lines):
        monkeys.append(make_monkey(lines[i:i+6]))
        i += 7
    
    for i in range(20):
        for m in monkeys:
            m.doThing(monkeys)
        for m in monkeys:
            print(m.num, m.items)
        print()
    
    counts = []
    for m in monkeys:
        counts.append(m.count)
        print(m.num, m.count)
    counts.sort(reverse = True)
    n = 1
    for i in range(2):
        n *= counts[i]
    print(n)
    

if __name__ == "__main__":
    main()