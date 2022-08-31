# 문제
# 입력받은 수를 조건식에 넣어 상금을 계산하는 문제
# 비교식을 통해 해결하면 된다.

a,b,c = map(int,(input().split(' ')))
reward = 0
if a == b == c :
    reward = 10000 + (a * 1000)
elif a== b or a == c or b == c:
    if a == b:
        reward = 1000 + (a*100)
    if a == c:
        reward = 1000 + (a*100)
    if b == c:
        reward = 1000 + (b*100)

else:
    big_num = max(a,b,c)
    reward = big_num * 100

print(reward)
    