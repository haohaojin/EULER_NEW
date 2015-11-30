# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 从2开始检查，质数直接放进去，其他分解后放入非重复项
# 建立1个list，key对应因数，value对应个数

#
list = range(2,21)
factor_list = []
factor_dict = {}
key = []
value = []

for i in list:
    problem = i
    problem_factor = []
    while problem != 1:
        for i in range(2,problem+1):
            if problem % i == 0:
                problem_factor.append(i)
                problem = int(problem/i)
                break
    factor_list.append(problem_factor)

print(factor_list)