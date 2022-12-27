def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    cycle = 1
    X = 1
    total = 0
    for line in lines:
        cmd = line.split(" ")
        if cycle % 40 == 20:
            total += X * cycle
        if cmd[0] == "addx":
            val = int(cmd[1])
            cycle += 1
            if cycle % 40 == 20:
                total += X * cycle
            X += val
        cycle += 1
    print(total)

if __name__ == "__main__":
    main()