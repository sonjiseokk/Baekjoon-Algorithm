# 문제
# 생각보다 간단한 문제이다. 몸무게와 키가 주어지는데 
# A와 B를 비교해서 둘다 우위면 덩치가 크다. 하나라도 아니면 덩치가 크다고 인정이 되지 않는다.

# 조건
# 1. 입력에 나열된 순서 그대로 출력해야 한다.

# 풀이
# 1. 입력값들을 전부 이차원 배열로 입력받는다.
# 2. 키와 몸무게(여기선 [0]과 [1]이다)를 입력값들과 전부 비교한다. 
# 3. 키와 몸무게가 전부 낮은 경우 해당 인덱스에 해당하는 check 값을 1 높인다.

max_case = int(input())

all_list = [list(map(int, input().split())) for _ in range(max_case)]

check = [1]*max_case
for i in range(max_case):
    for j in range(max_case):
        if all_list[i][0] != all_list[j][0] and all_list[i][1] != all_list[j][1]:
            if all_list[i][0] > all_list[j][0] and all_list[i][1] > all_list[j][1]:
                check[j]+=1

print(*check)

