def isPrime(problem):
    temp = []
    while problem != 1:
        for i in range(2,problem+1):
            if problem % i == 0:
                temp.append(i)
                problem = int(problem/i)
                break
    if len(temp) == 1:
        return True
    else:
        return False



prime = []
ct = 0

while ct < 10002:
    for i in range(2,9999999999):
        if isPrime(i):
            ct += 1
            print(str(ct) + ' - ' + str(i))
            prime.append(i)

