# 문제
# 그리디 문제이나 신경써야할 요소가 3개인 문제이다.
# 백준 기준으로 서브태스크 문제라 부분점수가 존재한다.
# 첫 줄에 노드의 갯수가 주어지고, 둘째 줄에 노드 사이의 거리비용, 셋째 줄에는 비용이 주어진다.
# 총 거리 비용은 같으나 그 거리 비용을 충전하는 노드비용이 노드마다 주어져있어 이를 최소화하는 문제이다.

# 조건
# 1. 최소화된 비용을 출력하는게 목적이다.

# 풀이
# 1. 결국 현재 접근가능한 최소 비용인 곳에서 최대한 많이 충전해나가야 하므로
# 2. 현재 접근 가능한 최소 비용인 곳의 비용을 계속 최신화 시켜주면서 나아간다.
# 3. 첫 노드는 불가항력적으로 최소비용이 되므로 now_low_cost는 첫 노드의 비용이다.
# 4. 적절히 line_cost들을 곱해나가면 정답이 처리된다.


city_num = int(input())

lines_cost= list(map(int,input().split()))

oil_cost= list(map(int,input().split()))

min_cost = 0
now_low_cost = oil_cost[0]
for i in range(city_num-1):
    if now_low_cost > oil_cost[i]:
        now_low_cost = oil_cost[i]
    
    min_cost += (now_low_cost*lines_cost[i])

print(min_cost)