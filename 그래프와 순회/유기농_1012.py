from collections import deque

# 문제
# 단지번호_2667 과 비슷한 문제이다.
# 단 그래프가 주어지는 게 아닌 1을 직접 입력받아 넣어주는 방식이다. 

# 조건
# 1. case를 여러 번 입력받을 수 있음에 주의하자.

# 풀이
# 1. 입력받은 좌표값들을 전부 1로 바꾸어준다.
# 2. BFS를 돌아 단지번호 때와 같이 1들을 0으로 초기화한다.
# 3. 단 여기선 단지번호 때의 "단지 수" 만을 출력하는 프로그램이기 때문에 count는 함수 호출 전에 더해준다.
# 4. dy, dx라는 상하좌우로 이동할 좌표 값을 더해주어 nx,ny를 만들어낸다.
# 5. 만약 인덱스를 초과할 수 있으므로 if문을 달아주고
# 6. 1이라면 큐에 해당 좌표를 추가해주어 그 좌표 주변에도 1이 있지 않을까 탐색한다.
# 7. 이런식으로 큐를 돌고나면 첫번째 단지가 모두 0으로 변하고 다음 이중 for문에서 다른 배추 심은 땅을 탐색하게 된다.
# 8. 마지막으로 count를 출력해주고 다시 for문을 돌아 케이스를 새로 생성한다.

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    graph[i][j] = 0
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny,nx))

case = int(input())

for _ in range(case):
    m,n,k = map(int,input().split())
    graph = [[0 for _ in range(m)] for i in range(n)]
    
    for i in range(k):
        q,w = map(int,input().split())
        graph[w][q] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count +=1
                bfs(i,j)
    
    print(count)