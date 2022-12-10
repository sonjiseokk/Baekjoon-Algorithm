import heapq
n = int(input())

room = []
for _ in range(n):
    heapq.heappush(room,list(map(int,input().split())))

start, end = heapq.heappop(room)
check = []
heapq.heappush(check,end)
while room:
    a,b = heapq.heappop(room)
    if check[0] <= a:
        heapq.heappop(check)
    heapq.heappush(check,b)

print(len(check))