fib = [1, 2]
result = 2

for i in range(50):
    fib.append(fib[i] + fib[i + 1])
    if (fib[i] + fib[i + 1]) <= 4000000 and (fib[i] + fib[i + 1]) % 2 == 0:
        result += (fib[i] + fib[i + 1])

print(result)