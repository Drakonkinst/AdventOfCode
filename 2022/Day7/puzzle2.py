class Node:
    def __init__(self, path):
        self.path = path
        self.fileSize = 0
        self.children = []

MIN = 30000000
MAX = 70000000

def calc(dirs, path, totals):
    curr = dirs[path]
    total = curr.fileSize
    for child in curr.children:
        total += calc(dirs, child, totals)
    totals[path] = total
    return total
    
def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    index = 0
    currDir = ""
    dirs = {}
    while index < len(lines):
        line = lines[index]
        cmd = line.split(" ")
        if cmd[1] == "cd": 
            name = cmd[2]
            if name == "..":
                currDir = currDir[:currDir[:-1].rfind("/") + 1]
            elif name == "/":
                currDir = "/"
            else:
                nextDir = currDir + cmd[2] + "/"
                if not nextDir in dirs:
                    dirs[nextDir] = Node(nextDir)
                    dirs[currDir].children.append(nextDir)
                currDir = nextDir
            if not currDir in dirs:
                dirs[currDir] = Node(currDir)
        elif cmd[1] == "ls":
            index += 1
            total = 0
            while index < len(lines):
                cmd2 = lines[index].split(" ")
                if cmd2[0] == "$":
                    break
                elif cmd2[0] == "dir":
                    nextDir = currDir + cmd2[1] + "/"
                    if not nextDir in dirs:
                        dirs[nextDir] = Node(nextDir)
                        dirs[currDir].children.append(nextDir)
                else:
                    size = int(cmd2[0])
                    total += size
                    name = cmd2[1]
                index += 1
            dirs[currDir].fileSize = total
            index -= 1
        else:
            print("ERROR")
        index += 1
    
    totals = {}
    totalSize = calc(dirs, "/", totals)
    unused = MAX - totalSize
    needed = MIN - unused
    print(needed)
    
    minVal = MAX
    for k, v in totals.items():
        if v < needed:
            continue
        if v < minVal:
            minVal = v
    print(minVal)

if __name__ == "__main__":
    main()