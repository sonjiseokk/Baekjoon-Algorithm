# 문제
# 그리디 + 파싱 문제이다.

# 조건
# 1. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.

# 풀이
# 1. https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=occidere&logNo=220833166496
# 2. 원리는 여기서 참조했다. 즉, - 뒤에 나오는 값을 다 더하면 되는 문제이다.
# 3. 따라서 - 기준으로 파싱하고 나오는 값들을 또 + 기준으로 파싱하여 숫자만 빼낸다.
# 3-1 . 55-50+40 를 기준으로 arr에는 [55,50,40] 이 남게 된다.
# 4. arr 첫번째 값은 두번째 for문을 통해 전부 더해진 값이므로
# 4-1. 55+50-10+20 <- 이런식으로 들어오더라도 arr[0] = 105 이다. 즉, -가 나오기 전 최소화된 값이다.
# 5. 계산을 거치면 최소값이 산출된다.


fx = input().split('-')

arr = []
for x in fx:
    sum_n = 0
    num = x.split('+')
    for i in num:
        sum_n+=int(i)
    arr.append(sum_n)

temp = arr[0]

for i in range(1,len(arr)):
    temp -= arr[i]

print(temp)