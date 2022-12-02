# 문제
# n이 주어지고 n 크기만큼의 [0] * n 배열을
# 입력받은 B배열로 변경시키는 최소한의 연산을 계산하는 문제이다.
# 연산 방법은 1. 배열 요소 하나를 +1 시키기, 2. 모든 배열 요소를 두 배 곱하기
# 거꾸로 생각하면 1로 만들기와 같은 대표적인 그리디 알고리즘 문제와 같아서 
# 그리디 알고리즘 문제라는 걸 알수있다.

# 조건
# 1. 배열의 크기 N은 1<= n <= 50 이다.
# 2. 배열에 들어있는 값은 0보다 크거나 같고 1000보다 작다

# 풀이
# 1. 앞서 말했듯 1로 만들기와 같은 그리디 알고리즘이나 배열이라는 것이 다른 점이다.
# 2. 그리디 알고리즘을 사용한다면 일단 현재 수를 최대한 많이 줄여야 한다.
# 2-1. 따라서 모두가 짝수인지 체크하고 만약 1이라면 바로 0을 만들어주고 cnt를 증가시킨다.
# 3. 짝수라면 모든 배열 요소를 2로 나누어 주고, 아니라면 홀수인 요소를 짝수로 만들어준다.
# 4. 계속해서 루프를 돌다가 a == b 즉, 모든 배열 요소가 0이 되면 종료되고 cnt를 출력한다.

length = int(input())
b = list(map(int,input().split()))

a = [0] * length
cnt = 0
while True:
    if a == b:
        break
    flag = 0
    for i in range(len(b)):
        if b[i] % 2 == 0:
            flag +=1
        if b[i] == 1:
            b[i] -=1
            cnt+=1
    if flag == len(b):
        for j in range(len(b)):
            b[j] /= 2
        cnt +=1
    else:
        for j in range(len(b)):
            if b[j] % 2 != 0:
                b[j] -= 1
                cnt +=1
    
print(cnt)