from collections import deque

def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    n = 0
    lookup = {}
    for line in lines:
        words = line.split(" ")
        name = words[0][:-1]
        if len(words) <= 2:
            # Expression
            lookup[name] = {
                "isExpr": False,
                "val": int(words[1])
            }
        else:
            lookup[name] = {
                "isExpr": True,
                "val1": words[1],
                "op": words[2],
                "val2": words[3]
            }
            # Value
        n += 1
    
    q = deque()
    q.append("root")
    
    while len(q) > 0:
        name = q.pop()
        node = lookup[name]
        if node["isExpr"]:
            val1 = node["val1"]
            val2 = node["val2"]
            val1Node = lookup[val1]
            val2Node = lookup[val2]
            if not val1Node["isExpr"] and not val2Node["isExpr"]:
                op = node["op"]
                result = -1
                if op == "+":
                    result = val1Node["val"] + val2Node["val"]
                elif op == "-":
                    result = val1Node["val"] - val2Node["val"]
                elif op == "*":
                    result = val1Node["val"] * val2Node["val"]
                elif op == "/":
                    result = val1Node["val"] // val2Node["val"]
                else:
                    assert False
                lookup[name] = {
                    "isExpr": False,
                    "val": result
                }
                continue
            q.append(name)
            if val1Node["isExpr"]:
                q.append(val1)
            if val2Node["isExpr"]:
                q.append(val2)
    
    print("N", n, "ROOT", lookup["root"])

if __name__ == "__main__":
    main()