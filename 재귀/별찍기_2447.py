# 문제
# 재귀를 사용하여 별을 찍으면 되는 설명은 아주 간단한데 어려운 문제다.
# 결국 혼자의 힘으로 풀진 못했고 인터넷의 힘을 빌렸다...

# 조건
# 1. N은 3의 거듭제곱이다.

# 풀이
# 1. 9가 입력되었다고 가정해보자. 그럼 draw_stars(3)이 실행 될 것이다. 
# 2. 똑같이 재귀로 돌아 끝에 *이 반환될 것이고 draw_stars(3)은 그걸 기반으로 모양을 만들 것이다.
# 3. 처음으로 돌아와 맨 처음 함수는 draw_stars(3)이 만든 모양을 3번 곱하여 모양을 하나 더 만드는 데 이것이 정답이다.



def draw_stars(n):
  if n==1:
    return ['*']

  Stars=draw_stars(n//3)
  L=[]

  for star in Stars:
    L.append(star*3)
  for star in Stars:
    L.append(star+' '*(n//3)+star)
  for star in Stars:
    L.append(star*3)

  return L

N=int(input())
print('\n'.join(draw_stars(N)))