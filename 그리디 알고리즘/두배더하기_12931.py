length = int(input())
b = list(map(int,input().split()))

a = [0] * length
cnt = 0
while True:
    if a == b:
        break
    flag = 0
    for i in range(len(b)):
        if b[i] % 2 == 0:
            flag +=1
        if b[i] == 1:
            b[i] -=1
            cnt+=1
    if flag == len(b):
        for j in range(len(b)):
            b[j] /= 2
        cnt +=1
    else:
        for j in range(len(b)):
            if b[j] % 2 != 0:
                b[j] -= 1
                cnt +=1
    
print(cnt)