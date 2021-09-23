def fat(n):
    if n<2:
        return 1
    else:
        return n*fat(n-1)

if __name__ == "__main__":
    results = []
    while True:
        try:
            line = list(map(int, input().split()))
            if line[0] == line[1]:
                results.append(2*fat(line[0]))
            else:
                results.append(fat(line[0]) + fat(line[1]))
        except EOFError:
            break
    
    for i in range(len(results)):
        if i != len(results)-1:
            print(results[i])
        else:
            print(results[i])