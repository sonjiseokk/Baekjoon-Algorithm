# 문제

# 사실 에라토스테네스의 체를 사용해야 하지만 이 당시엔 알지 못했다.
# 그래서 인터넷에서 결국 찾아보았고, 인터넷의 코드와 상당히 유사하다.

# 조건 1. 2보다 큰 모든 짝수는 두 소수의 합은 골드바흐의 수이다.
# 조건 2. 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다.
# 조건 3. 입력값은 10000이 최대치이다.
# 조건 4. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

# 풀이
# 1. 최대한 시간을 단축하기 위해 케이스를 전부 입력받아 max를 저장해놓는다.
# 2. max 만큼 check_list에 True를 저장해놓는다.
# 3. 에라토스테네스의 체를 사용하여 골드바흐의 수를 제외한 다른 수(인덱스)를 False로 변환한다.
# 4. 입력값을 반으로 나누고 서로 양방향으로 한칸씩 멀어지면서 조건 4를 만족하는 골드바흐의 수를 찾는다.

import math

max_case = int(input())
case = []
for i in range(max_case):
    num = int(input())
    case.append(num)

case_max_num = max(case)
check_list = [True for _ in range(case_max_num+1)]

a = int(math.sqrt(case_max_num))
for x in range(2, a + 1):
    if check_list[x] == True:
        j = 2
        while x * j <= case_max_num:
            check_list[x*j] = False
            j+=1
check_list[0] = False
check_list[1] = False

for case_num in case:
    a = case_num // 2
    b = a
    for _ in range(10000):
        if check_list[a] and check_list[b]:
            print(a,b)
            break
        a-=1
        b+=1
