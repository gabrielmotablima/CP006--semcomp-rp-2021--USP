if __name__ == "__main__":
    in_1 = input()
    num = []
    for i in range(int(in_1)):
        in_x = list(map(int, input().split()))
        num.append(in_x)
    
    maximum = []
    for i in range(int(in_1)):
        num1=num[i][0]
        num2=num[i][1]
        if num1 != num2:
            mdc = 1
        else:
            mdc = num1
        maximum.append(mdc)
       
    for i in range(int(in_1)):
        print(maximum[i])