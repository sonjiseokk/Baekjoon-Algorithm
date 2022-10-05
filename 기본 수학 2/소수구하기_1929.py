# 문제
# 에라토스테네스의 체를 사용하여 소수들을 전부 출력하는 프로그램

# 조건
# 1. 1이상 1,000,000 이하의 소수가 하나 이상 존재하는 수만 입력됨.
# 2. 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 풀이
# 1. 입력받은 최소값과 최대값을 통해 for문을 구성한다.
# 2. 에라토스테네스의 체를 사용하여 최소값과 최대값의 사이 값이 소수인지 아닌지 판별한다.
# 3. 소수이면 sosu 리스트에 append 하고 다음엔 sort() 하여 출력한다. 

import math

min_input, max_input = map(int,(input().split()))

flag = 0
sosu = []
for case in range(min_input,max_input+1):
    flag = 0
    a = int(math.sqrt(case))
    if case == 1:
        flag = 1
    for x in range(2, a + 1):
        if case % x == 0:
            flag = 1
            break
    if flag == 0:
        sosu.append(case)

sosu.sort()
for i in sosu:
    print(i)
