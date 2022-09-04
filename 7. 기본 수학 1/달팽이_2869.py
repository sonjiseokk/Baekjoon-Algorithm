# 문제
# A미터 올라가고 B미터 내려간다면 며칠만에 입력값만큼 갈 수 있는지 알아내는 문제
# 조건 1. 정상에 올라간 후엔 미끄러지지 않는다.
# 조건 2. 목표 미터는 엄청 큰 수이므로 최적화해야 한다.

# 조건 2 때문에 input() 함수 대신 sys를 사용했고, 간단한 계산식을 통해 해결했다.

import sys

a,b, v = map(int,sys.stdin.readline().split())

i = (v-b) / (a-b)

if i == int(i):
    print(int(i))
else:
    print(int(i)+1)