m,n,k = map(int,input().split())
dp = [[0]*(n+1) for _ in range(m+1)]
for _ in range(k):
    a,b = map(int,input().split())
    dp[a][b] = 1

# dp = [
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,1,0,0],
#     [0,1,1,0,1,0,0,1,1],
#     [0,0,0,0,0,0,0,0,1],
#     [0,0,0,1,1,1,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
# ]
count = 0
collect = 0
start = 1
i = 1
temp = 1
while True:
    check = 0
    for x in dp:
        check+=sum(x)
    if check == 0:
        count+=1
        break
    
    org = collect
    for j in range(start,n+1):
        if i == m and j == n:
            count +=1
            temp = 1
            i = 1
            collect = 0
            break
        if sum(dp[i][j:]) > 0:
            if dp[i][j] == 1:
                dp[i][j] = 0
                temp = j
                collect +=1
        else:
            i+=1
            if i > m:
                i = m
                temp = j+1
            elif org == collect:
                temp = j
            break
    
    start = temp

print(count)