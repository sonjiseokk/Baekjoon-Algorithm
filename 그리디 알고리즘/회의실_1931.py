# 문제
# 그리디 + 정렬문제이다.

# 조건
# 1. 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 2. 회의의 시작시간과 끝나는 시간이 같을 수도 있다.

# 풀이
# 1. 입력 받은 값들을 리스트에 저장한다.
# 2. 시작 시간을 기준으로 정렬한다. 이 과정에서 람다 함수를 사용한다.
# 3. 그 상태에서 끝나는 시간을 기준으로 정렬한다. 이러면 시작시간이 작은 순서가 유지되면서 끝나는 시간이 짧은 값이 위로간다.
# 4. 이 정렬된 리스트에서 end 시간을 계속 추적하면서 그리디하게 값을 찾는다.

n = int(input())

fcfs = []
for _ in range(n):
    x,y = map(int,input().split())
    fcfs.append([x,y])

count = 1
fcfs.sort(key = lambda x:x[0])
fcfs.sort(key=lambda x:x[1])

end = fcfs[0][1]

for i in range(1,len(fcfs)):
    if fcfs[i][0] >= end:
        count+=1
        end = fcfs[i][1]

print(count)
