# 문제
# 입력값을 3과 5로 요리조리 나눈 몫의 합을 최소화 하는 문제

# 조건 1. 정확하게 못 나눈다면 -1 출력
# 조건 2. 몫의 합은 항상 최소화 되어야함.

# 일단 5로 나누는 것이 분명히 몫의 합을 최소화 하는 것이기때문에 5로 나누어지면 그냥 출력
# 그렇지 않은 경우엔 하나라도 3으로 나누어 진다는 소리이기에 n
# num을 -3 하면서 3으로 나누는 경우를 카운팅 

# -3 빼진 값이 5로 나누어지면 합쳐서 출력
# -3 빼진 값이 1까지 내려간다면 즉, while문을 다 돌고도 못찾았다면 -1 출력
# -3 빼진 값이 3으로만 나누어진다면 카운팅된 숫자 출력

num = int(input())

if num % 5 == 0:
    print(num//5)
else:
    third_case = 0
    while num >= 0:
        num -= 3
        third_case +=1

        if num % 5 == 0:
            third_case += (num // 5)
            print(third_case)
            break
        elif num == 1:
            print(-1)
            break
        elif num == 0:
            print(third_case)
            break