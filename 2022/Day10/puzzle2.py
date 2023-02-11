def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    cycle = 1
    X = 1
    total = 0
    crt = ""
    for line in lines:
        cmd = line.split(" ")
        # Cycle
        if cycle % 40 == 20:
            total += X * cycle
        pixel = (cycle - 1) % 40
        if abs(pixel - X) <= 1:
            crt += "#"
        else:
            crt += "."
        if pixel == 39:
            print(crt)
            crt = ""
            
        if cmd[0] == "addx":
            val = int(cmd[1])
            cycle += 1
            # Cycle
            if cycle % 40 == 20:
                total += X * cycle
            pixel = (cycle - 1) % 40
            if abs(pixel - X) <= 1:
                crt += "#"
            else:
                crt += "."
            if pixel == 39:
                print(crt)
                crt = ""
            X += val
            
        cycle += 1
    print(total)

if __name__ == "__main__":
    main()