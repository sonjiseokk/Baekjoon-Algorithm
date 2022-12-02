while True:
    n = int(input())
    if n == 0:
        break
    
    dp = [0]*(n+1)

    dp[0] = 1

    for i in range(1,n):
        temp = (2*(2*i+1))
        dp[i] = dp[i-1] * (temp / (i+2))
     
    print(int(dp[n-1]))