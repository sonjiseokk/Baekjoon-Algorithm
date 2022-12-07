# 문제
# 작은 두 원소끼리 더한게 또 다른 원소가 되어 연산을 하는 문제이다.
# 계속 그리디하게 최소 원소들을 합쳐야 하므로 heapq를 사용했다.

# 조건
# 1. (1 ≤ N ≤ 100,000)
# 2. 주어지는 수들은 1000 이하임.

# 풀이
# 1. 입력받은 수들을 heapq에 push함.
# 2. 임시 배열을 생성하고 반복문을 돌림.
# 3. dex에서 최소 원소 하나를 빼고 arr에 넣음.
# 4. arr의 길이가 2 이상이 되면 dex에 합친 값을 넣고 res에도 더해줌 + arr을 초기화함.
# 5. 계속 연산하면 정답 처리를 받게됨.

import heapq
n = int(input())

dex = []
for i in range(n):
    heapq.heappush(dex,int(input()))

arr = []
res = 0
while len(dex) >= 1 or len(arr) >= 2:
    if len(arr) >= 2:
        heapq.heappush(dex,sum(arr))
        res += sum(arr)
        arr = []
    x = heapq.heappop(dex)
    heapq.heappush(arr,x)


print(res)

