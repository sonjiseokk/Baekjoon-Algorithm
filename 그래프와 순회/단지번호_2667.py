from collections import deque
# 문제
# 2차원 배열로 입력받는 정보들을 DFS나 BFS를 통해 없애나가면서 1의 갯수를 찾는 문제이다.
# 처음 생각으론 2차원 배열로 그래프를 그대로 표현하려 했지만 쉽지않아 BFS를 통한 방법으로 선회했다.

# 조건
# 1. 처음에는 단지 수, 그리고 다음 줄 부터는 오름차순으로 출력해야 한다.

# 풀이
# 1. 010101 이런 식으로 된 입력을 리스트로 받아온다.
# 2. BFS를 돌린 결과물을 result에 추가한다.
# 3. BFS는 일단 들어옴과 동시에 해당하는 좌표 값을 0으로 수정하고
# 4. dy, dx라는 상하좌우로 이동할 좌표 값을 더해주어 nx,ny를 만들어낸다.
# 5. 만약 인덱스를 초과할 수 있으므로 if문을 달아주고
# 6. 1이라면 큐에 해당 좌표를 추가해주어 그 좌표 주변에도 1이 있지 않을까 탐색한다.
# 7. 이런식으로 큐를 돌고나면 첫번째 단지가 모두 0으로 변하고 다음 이중 for문에서 다른 단지를 탐색하게 된다.


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(i,j):
    count = 1
    queue = deque()
    queue.append((i,j))
    graph[i][j] = 0
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny,nx))
                count+=1
    return count
n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

result =[]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i,j))

result.sort()

print(len(result))
print(*result,sep="\n")

    # [0,1,1,0,1,0,0],
    # [0,1,1,0,1,0,1],
    # [1,1,1,0,1,0,1],
    # [0,0,0,0,1,1,1],
    # [0,1,0,0,0,0,0],
    # [0,1,1,1,1,1,0],
    # [0,1,1,1,0,0,0]