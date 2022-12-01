def main():
    file = open("input.txt", "r");
    lines = file.readlines()
    
    maxSum = 0
    currSum = 0
    for line in lines:
        if not line.strip():
            if currSum > maxSum:
                maxSum = currSum
            currSum = 0
        else:
            currSum += int(line)
    print(maxSum)

if __name__ == "__main__":
    main()