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
    nlen = len(str(k))

    if nlen % 2 == 1:
        for f in range(0,int((nlen-1)/2)):
            first_half += str(k)[f]
        for s in range(int((nlen+1)/2),nlen):
            second_half += str(k)[s]
        for t in range(0,int((nlen-1)/2)):
            reversed_second_half += second_half[int((nlen-1)/2) - t - 1]
        if first_half == reversed_second_half:
            all_result.append(k)
    else:
        for f in range(0,int(nlen/2)):
            first_half += str(k)[f]
        for s in range(int(nlen/2),nlen):
            second_half += str(k)[s]
        for t in range(0,int(nlen/2)):
            reversed_second_half += second_half[int(nlen/2) - t - 1]
        if first_half == reversed_second_half:
            all_result.append(k)

print(max(all_result))
print("--- %s seconds ---" % (time.time() - start_time))
