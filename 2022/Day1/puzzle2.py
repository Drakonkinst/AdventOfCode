def main():
    file = open("input.txt", "r");
    lines = file.readlines()
    lines.append("")
    
    top1 = 0
    top2 = 0
    top3 = 0
    currSum = 0
    for line in lines:
        if not line.strip():
            if currSum > top1:
                top3 = top2
                top2 = top1
                top1 = currSum
            elif currSum > top2:
                top3 = top2
                top2 = currSum
            elif currSum > top3:
                top3 = currSum
            currSum = 0
        else:
            currSum += int(line)
    print(top1 + top2 + top3)

if __name__ == "__main__":
    main()