# 문제
# 생각보다 간단한 문제였으나 복잡하게 생각하느라 풀지 못하고 찾아봤던 비운의 문제다.
# 간단하다. 소인수분해의 소인수들을 출력하면 된다.

# 조건
# 1. 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
# 2. 한 줄에 하나씩 오름차순으로 출력한다.
 
# 풀이
# 1. i를 2로 설정하여 2로 나누어지면 2를 출력하고 num을 2로 나눈 수로 변환한다.
# 2. 2로 안 나누어진다면 i+=1 하여 소인수를 찾아본다. 

num = int(input())

i = 2
while num > 1:
    if num % i == 0:
        num = num / i
        print(i)
    else:
        i+=1