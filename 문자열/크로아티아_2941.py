# 문제
# 원리는 간단하다. 크로아티아 알파벳의 형식을 찾아 그 형식이 있으면 카운팅 하면 된다.

# 1. 크로아티아 알파벳을 모두 저장해둔다.
# 2. count 함수를 통해 해당되는 값을 카운팅 하여 출력한다.
# 3. 기본 알파벳도 갯수에 포함되어야 하므로 전체 길이에서 크로아티아 알파벳의 갯수만 뺀다.

user_input = input()

change_words = ['c=','c-','dz=','d-','lj','nj','s=','z=']
result = 0
for word in change_words:
    result+=user_input.count(word)


print(len(user_input)-result)