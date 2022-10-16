# 문제
# dp를 통해 입력받은 배열 인덱스들에게 최소 점프 수를 할당해 출력하는 문제이다.

# 조건
# 1. 최소 점프 수를 출력하면 된다. 단 도달하지 못할 경우 -1을 출력한다.

# 풀이
# 완전한 이해가 되지못해 추후 작성하겠습니다....


n = int(input())

a = list(map(int,input().split())) 
big = 1000000
a.insert(0,0)

dp = [big for _ in range(n+1)]
dp[1] = 0
count = 0
for i in range(1,n+1):
    if dp[i] != big:
        temp = a[i]
        for j in range(1,temp+1):
            if i+j > n:
                continue
            dp[i+j] = min(dp[i] + 1, dp[i+j])

if dp[n] != big:
    print(dp[n])
else:
    print(-1)