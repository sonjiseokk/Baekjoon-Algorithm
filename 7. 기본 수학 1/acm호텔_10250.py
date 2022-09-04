# 문제
# 정해진 구조에 정해진 규칙을 따라가 해당값을 출력하는 프로그램

# 조건 1. 높이와 너비는 항상 입력받는다.
# 조건 2. 방은 1호 기준으로 층수만 올라가면서 늘어나는 방식이다.

# 풀이
# 층수만 올라가는 방식이기에 들어온 순서를 높이와 나누어준다.
# 나눈 나머지는 층수일 것이고, 몫은 이전 호를 다 채웠다는 의미이기에 1과 더해 일치시킨다.

# 나머지가 없다면 최대 층수와 같다는 의미이기에 최대 층수와 일치시키고, 호수는 몫으로 바꾼다.
# 호수가 10보다 작다면 0을 넣어준다 ex) 9 -> 09
# 처리가 끝났으니 층수와 호수를 출력한다.

test_case = int(input())

for i in range(test_case):
    h, w, n = map(int,input().split())

    floor = n % h
    room = 1 + (n//h)

    if n % h == 0:
        floor = h
        room = n//h
    if room<10:
        print(floor,'0',room,sep='')
    else:
        print(floor,room,sep='')