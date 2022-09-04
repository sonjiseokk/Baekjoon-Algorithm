# 문제
# 골드바흐와 비슷한 문제이다.
# 똑같이 체크리스트를 만들지만 골드바흐는 파티션을 출력하고 이건 입력값 이하의 개수를 출력한다.

# 조건
# 1. n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력
# 2. 0이 입력되면 입력이 중단된다.

# 풀이
# 1. 설명과 같이 골드바흐처럼 체크리스트를 만든다.
# 2. 0이 입력되어야 중단되므로 무한루프문을 돌게하고 조건 1을 만족하는 조건문을 넣는다

import math

max = 246913

check_list = [True for _ in range(max+1)]

a = int(math.sqrt(max))
for x in range(2, a + 1):
    if check_list[x] == True:
        j = 2
        while x * j <= max:
            check_list[x*j] = False
            j+=1
    check_list[0] = False
    check_list[1] = False

while True:
    num = int(input())
    if num == 0:
        break
    
    min_input = num
    max_input = 2*num
    count = 0
    for i in range(min_input+1,max_input+1):
        if check_list[i] == True:
            count +=1

    print(count)


