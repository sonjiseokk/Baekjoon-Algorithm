# 문제
# 기존 회의실(1931) 문제와 비슷해보이나 다른 문제이다.
# 주어진 시간들을 전부 돌렸을 때, 필요한 최소 강의실의 수를 구하는 문제다.
# 1~3 , 2~4 가 주어진다면 강의실 수는 2개 -> 이런 식으로 계산하면 된다.

# 조건
# 1. 강의의 개수는 1 <= n <= 100,000개 이다.
# 2. 한 강의실은 2개 이상의 강의가 진행될 수 없다.
# 3. 종료 시간과 시작 시간이 같은 건 상관이 없다.
# 4. 강의 시작시간과 종료시간은 10억이하의 정수이다. -> O(n^2)의 시간복잡도로는 해결 불가능 

# 풀이
# 1. 시간의 최대값이 매우 큰 수이므로, heapq라는 라이브러리를 사용해 속도를 높혀야한다.
# 2. 넘버 값은 사실상 필요없기 때문에, 시작시간과 종료시간만 heapq에 푸시한다.
# 3. heappop이 되면 안에 있는 리스트 중의 최소값만 O(nlogn)으로 팝되므로 첫번째 값을 pop한다.
# 4. 이후 종료값을 pri_queue에 저장한다.
# 5. while문 안에서 만약 끝나는 최소값이 start 시간보다 작다면 pri_queue에 있는 수업이 종료된 것이므로 pop한다.
# 
# 큰 맥락으로 list_class에서 시작시간이 제일 짧은 값이 pop되고
# 이중 end 값만 pri_queue에 push 해놓고 
# 들어오는 start 값이 pri_queue에 있는 제일 짧은 end 값보다 큰 경우엔 강의가 종료된 것이라 생각하면 되므로
# 이를 pop하고나서 pri_queue의 길이를 출력하면 그게 답이 된다. 

import heapq
n = int(input())

list_class = []
pri_queue = []
for i in range(n):
    num, start,end = map(int,input().split())
    heapq.heappush(list_class, [start,end])

start, end = heapq.heappop(list_class)
heapq.heappush(pri_queue,end)

while list_class:
    start, end = heapq.heappop(list_class)
    if pri_queue[0] <= start:
        heapq.heappop(pri_queue)
    heapq.heappush(pri_queue,end)

print(len(pri_queue))

