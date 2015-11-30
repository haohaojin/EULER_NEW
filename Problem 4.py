import time
start_time = time.time()

all = []
all_result = []
for i in range(100, 1000):
    for j in range (100, 1000):
        all.append(i*j)

for k in all:
    first_half = ''
    second_half = ''
    reversed_second_half = ''
    nlen = 0
    #print(k)
    nlen = len(str(k))
    #print(str(nlen))
    if nlen % 2 == 1:
        for f in range(0,int((nlen-1)/2)):
            first_half += str(k)[f]
        #print(first_half)

        for s in range(int((nlen+1)/2),nlen):
            second_half += str(k)[s]
        #print(second_half)

        for t in range(0,int((nlen-1)/2)):
            reversed_second_half += second_half[int((nlen-1)/2) - t - 1]
        #print(reversed_second_half)

        if first_half == reversed_second_half:
            all_result.append(k)
    #else:

print(all_result)
print("--- %s seconds ---" % (time.time() - start_time))
