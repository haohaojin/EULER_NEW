sqrt = 0
sum = 0

for i in range(1,101):
    sqrt += i * i
    sum += i

print(int(sum*sum-sqrt))