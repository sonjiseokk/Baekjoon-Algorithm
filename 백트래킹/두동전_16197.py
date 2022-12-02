# 문제
# 백트래킹 문제이다.
# o의 위치가 정해져 있고, 벽이 아닌 곳은 이동이 가능하다.
# 방향키 위,아래,왼쪽,오른쪽 하나를 선택시 o 두개가 같이 움직인다.
# 이중 o 하나만을 떨어뜨리는 최소 경우의 수를 구하는 게 문제이다.

# 조건
# 1. 두 개 동시에 떨어지거나 떨어지지 못하면 -1이 출력된다.

# 풀이
# 1. 벡터 이동 값을 미리 dx,dy를 정의해놓고 그래프를 입력받는다.
# 2. 이후 track_o 함수를 통해 o의 i,j 값 그리고 버튼 수를 저장할 변수를 백트래킹 함수로 넘겨준다.
# 3. 만약 두 개 동시에 떨어진다면, check 값이 2가 되므로 그땐 다른 벡터값을 준다.
# 3-1. 하나만 떨어졌다면 여태 버튼 누른 값과 기존에 저장해둔 cnt값을 min함수로 비교해 최소값을 저장해둔다. (백트래킹이므로)
# 4. 만약 벡터 값을 더해 수정된 x,y 좌표가 벽이라면 다시 원점으로 돌아온다.
# 5. 수정된 x,y 좌표랑 btn+1 을 넘겨주어 백트래킹을 반복한다.

def backtrack(y1,x1,y2,x2,btn):
    global cnt
    if btn >= cnt or btn >= 10:
        return
    for move in range(4):
        check = 0
        n1x = x1 + dx[move]
        n1y = y1 + dy[move]
        n2x = x2 + dx[move]
        n2y = y2 + dy[move]
        check = 0
        if n1x >= m or n1x <0 or n1y >= n or n1y < 0:
            check+=1

        if n2x >= m or n2x <0 or n2y >= n or n2y < 0:
            check+=1

        if check == 2:
            continue

        if check == 1:
            cnt = min(cnt,btn+1)
            return

        if graph[n1y][n1x] == "#":
            n1x = x1
            n1y = y1
        if graph[n2y][n2x] == "#":
            n2x = x2
            n2y = y2

        backtrack(n1y,n1x,n2y,n2x,btn+1)
    
def track_o():
    save =[]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'o':
                save.append((i,j))
    return save

n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(input()))

cnt = 10e9
btn = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cur_o = track_o()
backtrack(cur_o[0][0],cur_o[0][1],cur_o[1][0],cur_o[1][1],btn)

if cnt == 10e9:
    print(-1)
else:
    print(cnt)