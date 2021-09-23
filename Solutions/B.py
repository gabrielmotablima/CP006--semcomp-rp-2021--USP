def is_prime(n):
    if (n==2) or (n==3):
        return True
    if n==1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

if __name__ == "__main__":
    results = []
    while True:
        # try:
        num = int(input())
        if num == 0:
            break
        bag = []
        for i in range(num):
            bag.append(int(input()))
        val = int(input())
        summ = 0
        for i in range(num-1, -1, 0-val):
            summ+=bag[i]
            print(bag[i])
        if is_prime(summ):
            results.append("You're a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            results.append("Bad boy! I'll hit you.")
        # except EOFError:
        #     break
    for result in results:
        print(result)