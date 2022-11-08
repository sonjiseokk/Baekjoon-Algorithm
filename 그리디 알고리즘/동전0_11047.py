# 문제
# 그리디의 기본형인 동전문제이다.

# 조건
# 1. 동전의 개수는 1 <= N <= 10, 동전의 가치는 1<= K <= 1억이다.

# 풀이
# 1. 입력받으면서 k보다 높은 값은 num에 저장하지 않아 연산과정을 줄인다.
# 2. 내림차순으로 정렬한다.
# 3. 그리디 개념에 따라 제일 큰 값으로 나누면 최소값이 나올것이기에
# 3-1. num에 저장된 큰 동전의 가치로 나누기 시작하여 count를 더해나가고 k를 나머지로 수정한다.

n, k = map(int,input().split())

num = []
for _ in range(n):
    temp = int(input())
    if temp<=k:
        num.append(temp)
num.reverse()
count = 0
for i in range(len(num)):
    if (k // num[i])>0:
        count += k // num[i]
        k = k % num[i]

print(count)


