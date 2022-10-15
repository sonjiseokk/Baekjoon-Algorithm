# n = int(input())
# a = list(map(int,input().split()))
n = 10
a = [1,2,0,1,3,2,1,5,4,2]
#    0   
dp = [10001] * (n)
dp[0] = 0
count = 0

def solution(a):
    for i in range(n):
        for j in range(1, a[i]):
            if i + j >= n:
                dp[n-1] = min(dp[n-1],dp[i]+1)
            else:
                dp[i+j] = min(dp[i+j],dp[i]+1)

    return dp[n-1]

print(solution(a))