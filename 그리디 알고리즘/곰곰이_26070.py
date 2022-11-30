# 푸는중

want = list(map(int,input().split()))

have = list(map(int,input().split()))

acc = [0] * len(want)
cnt = 0
for i in range(len(want)):
    if have[i] >= want[i]:
        cnt += (have[i] - want[i])
    acc[i] = have[i] - want[i]
for i in range(len(acc)):
    if acc[i] > 0:
        temp = acc[i] // 3
        if i == len(acc) - 1:
            acc[0] = acc[0] + temp
            cnt += temp
        else:
            acc[i+1] = acc[i+1] + temp
        
        acc[i] = temp
        



