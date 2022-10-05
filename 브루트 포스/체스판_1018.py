# 2/5 
# (1. 아예 못함 2. 조금은 맞춤 3. 거의 다 와서 찾아봄 4. 정답에 가까움(자발적) 5. 자발적 정답임)

# 문제
# 8*8 이상의 판에서 8*8 체스판을 만드려고 하는 문제이다.
# 문제가 복잡하니 직접 보도록 하자.

# 브루트포스 문제이기 때문에 단순하게 말하면 모두 때려박아보면 해결된다..?

# 조건
# 1. 시작은 B일수도 W일수도 있다.
# 2. M과 N은 50보다는 작거나 같은 자연수이다.

# 풀이
# 1. 4중 for문을 사용하려고 한다. i,j 포문에서는 입력받은 판을 8*8로 이리저리 쪼개보는 개념이다.
# 2. x,y 포문에서는 만약 첫 시작이 B라고 가정하자. [x][y]가 0,0 일때 값이 W라면?
# 3. B가 시작이라면 틀린 것이기에 수정해야될 부분이다. 그래서 카운팅을 하게된다.
# 4. 이런식으로 repair 리스트에 전부 추가하다보면 i,j 포문에서 이리저리 쪼개보았던 8*8 판의 최소가 나온다.
# 5. 그걸 그대로 출력한다. 


n,m = map(int,input().split())

board = []
for _ in range(n):
    board.append(input())

repair = []

for i in range(n-7):
    for j in range(m-7):
        first_w = 0
        first_b = 0
        for x in range(i,i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0 :
                    if board[x][y] == 'B':
                        first_w+=1
                    if board[x][y] == 'W':
                        first_b+=1
                else:
                    if board[x][y] == 'B':
                        first_b+=1
                    if board[x][y] == 'W':
                        first_w+=1
        
        repair.append(first_w)
        repair.append(first_b)

print(min(repair))
        