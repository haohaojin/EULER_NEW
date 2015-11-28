import time
start_time = time.time()

problem = 600851475143
largest = 0

while problem != 1:
    for i in range(2,problem+1):
        if problem % i == 0:
            largest = max(i, largest)
            problem = int(problem/i)
            break

print(largest)
print("--- %s seconds ---" % (time.time() - start_time))