# 문제
# a[i] * b[i]를 최소화하는 문제이다.
# 제일 작은 놈을 제일 큰 놈과 곱해야 최소화가 되므로 정렬만 하면 된다.

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

sum1 = 0
for i, x in enumerate(a):
    sum1 += (x * b[i])

print(sum1)