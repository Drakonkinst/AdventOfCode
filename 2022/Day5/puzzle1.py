def move(stack, f, t):
    #print(f, "to", t)
    fArr = stack[f]
    tArr = stack[t]
    tArr.append(fArr.pop())

def main():
    file = open("input.txt", "r");
    lines = [line for line in file.readlines()]
    
    stacks = []
    li = 0
    for line in lines:
        if not line[1].isnumeric():
            index = 1
            stack = []
            while index < len(line):
                if line[index] == ' ':
                    stack.append("")
                else:
                    stack.append(line[index])
                index += 4
            #print(stack)
            stacks.append(stack)
            li += 1
        else:
            break
    
    stacks2 = []
    for i in range(len(stacks[0])):
        stack = []
        for j, _ in reversed(list(enumerate(stacks))):
            if len(stacks[j][i]) > 0:
                stack.append(stacks[j][i])
            else:
                break
        stacks2.append(stack)
        print(stack)
    
    li += 2
    while li < len(lines):
        instr = lines[li].split(" ")
        n = int(instr[1])
        f = int(instr[3]) - 1
        t = int(instr[5]) - 1
        for i in range(n):
            move(stacks2, f, t)
        li += 1
    
    s = ""
    for item in stacks2:
        s += item[-1]
    print(s)

if __name__ == "__main__":
    main()