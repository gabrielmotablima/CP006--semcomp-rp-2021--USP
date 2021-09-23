if __name__ == "__main__":
    pkgs = []
    tmp = 0
    while True:
        line = input()
        if line == '1':
            tmp+=1
            pkgs.append([])
            continue
        if line == '0':
            continue
        value = int(line[-3:])
        size = len(pkgs[tmp-1])
        if size == 0:
            pkgs[tmp-1].append(value)
            continue
        for i in range(size):
            if pkgs[tmp-1][i] > value:
                pkgs[tmp-1].insert(i, value)
                break
            elif i == size-1:
                pkgs[tmp-1].append(value)
                break
                
    for i in range(len(pkgs)):
        for j in pkgs[i]:
            print(f'Package {j:03}')
        if i != len(pkgs-1):
            print('\n')