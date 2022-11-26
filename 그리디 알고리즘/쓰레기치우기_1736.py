# 문제
# 트레저헌터 풀다가 개빡쳐서 비슷한 문제로 시도해보았다.
# 그래프에 쓰레기(1) 이 존재하고 (0,0)에서 시작하되 오른쪽,아래 로만 이동이 가능하다.
# 다 없애려면 로봇이 몇 개가 필요한지 묻는 문제이다.

# 조건
# 1. 딱히 큰게 없다.

# 풀이
# 1. O(N^2)으로 해결할 수 있지만 트레저헌터때문에 개빡쳐서 LIS 문제로 강제 변환하였다.
# 2. 입력받은 그래프의 인덱스를 추출해서 y축 기준으로, x축 기준으로 한번씩 정렬한다.
# 3. get_lis_improved 함수를 통해 LIS로 연결되는 가장 긴 수열을 return한 다음, set으로 형변환하여 빼버린다.
# 4. 다시 list로 바꾸고 다시 정렬한다음 다시 함수 돌린다.
# 5. 굉장히 비효율적이나 앞서 말했듯 트레저헌터땜에 LIS로 가능함을 보이고 싶었다...

n,m = map(int,input().split())

dp = [list(map(int,input().split())) for _ in range(n)]

coin_list = []
for i in range(n):
    for j in range(m):
        if dp[i][j] == 1:
            coin_list.append((i,j))

coin_list.sort(key=lambda x:x[0])
coin_list.sort(key=lambda x:x[1])
def get_lis_improved(lis_list):
    L = [lis_list[0]]

    for i in range(1, len(lis_list)):
        if L[-1][0] <= lis_list[i][0]:
            if L[-1][1] <= lis_list[i][1]:
                L.append(lis_list[i])
    return L

count = 0
while coin_list:
    del_list = get_lis_improved(coin_list)
    coin_list = list(set(coin_list) - set(del_list))
    coin_list.sort(key=lambda x:x[0])
    coin_list.sort(key=lambda x:x[0])
    count+=1

print(count)