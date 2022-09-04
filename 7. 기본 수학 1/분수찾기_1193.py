# 문제
# 이것도 규칙을 찾기 위해서 많은 시간을 고민했지만 결국 찾지못해 인터넷을 보게되었다..
# 그래도 벌집보다는 접근 방식이 아예 달랐기에 덜 아쉽긴 하다.

# 1. 결과 값을 나열해서 생각해보자. 나열한다면
# 1/1 | 1/2 2/1 | 3/1 2/2 1/3 | 1/4 2/3 3/2 4/1 ....
# 2. 이를 바탕으로 해석하면 인덱스가 홀수일 때엔 top이 -1되고 짝수일 대엔 bottom이 -1이 된다.
# 3. 이것을 if문을 통해 해석하면 값을 구해낼 수 있다.

n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line%2 == 0: #짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))