# 문제
# 아쉽게도 접근 방식이 잘못되어 꽤 고생한 문제다.
# 실패 요인은 cnt의 공차를 찾지 못했던 게 너무 아쉬운 요인이다.

# 1. 초기에 start와 distance의 값을 2,1로 설정(1은 중앙이기에 시작은 2부터이므로 distance도 1)
# 2. 루프문을 돌면서 start에 cnt를 더하면 한 줄의 최대값이 나타나므로 반복한다.
# 3. 입력값을 찾았을 때 break하고 거리를 출력한다.

num = int(input())

start = 2
distance = 1

cnt = 6

while(1):
    if num == 1:
        break
    elif start + cnt > num:
        distance+=1
        break
    else:
        start += (cnt)
        cnt +=6
        distance+=1

print(distance)
