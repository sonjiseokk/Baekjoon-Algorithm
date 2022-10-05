# 문제
# 하노이 탑의 규칙을 인용하겠다. 결국 하노이탑을 구현하는 프로그램이다.
# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

# 조건
# 1. N (1 ≤ N ≤ 20)이 주어진다.
# 2. 출력값은 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

# 풀이
# 1. 함수를 구성하는데 from,to,other로 인자를 구성한다.
# 2. 결국 하노이탑은 밑에 하나를 지우면서 n-1을 만들기 때문에 num-1을 넘겨주고 재귀를 돌린다.
# 3. 차이점이라면 전역변수를 사용하여 프린트 하였다.

# 출처
# https://www.youtube.com/watch?v=aPYE0anPZqI 하노이탑 다른 문제 설명

global count
count = 0
all_list = []
def menoi(num,fromis,to,other):
    global count
    if num == 0:
        return
    else:
        menoi(num-1,fromis,other,to)
        all_list.append([fromis,to])
        count = count + 1
        menoi(num-1,other,to,fromis)


max_num = int(input())

menoi(max_num,1,3,2)

print(count)

for x in all_list:
    print(*x)
