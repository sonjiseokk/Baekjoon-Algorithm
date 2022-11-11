# 문제
# 그리디 + 정렬문제이다.
# ATM을 기다리는 줄이 존재하고 각각 이용시간이 다르다면 N명이 모두 종료하였을 때의 최소시간을 구하는 문제이다.

# 조건
# 1. 문제와 같이 각각 이용자의 이용시간이 다르다.
# 2. 입력은 이용시간만 받는다. 즉, 첫번째로 받는 입력은 첫번째 이용자의 이용시간이다.

# 풀이
# 1. 대기시간을 고려해야 하므로, 가장 빨리 끝내는 사람이 가장 빨리 이용해야 대기시간이 줄어든다.
# 2. 따라서 이용시간 기준으로 정렬한다.
# 3. 이후 이전 이용시간을 이중포문을 통해 계속 계산하고 더해주어 최종 값을 도출한다.


n = int(input())
times = list(map(int,input().split()))

table = [[i,0] for i in range(1,n+1)]
for i in range(n):
    table[i][1] = times[i]

table.sort(key = lambda x:x[1])

# print(table)
count = 0
for i in range(len(table)):
    temp = 0
    for j in range(i):
        temp += table[j][1] 
    
    count += table[i][1] + temp
print(count)