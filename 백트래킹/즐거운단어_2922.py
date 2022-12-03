# 문제
# 백트래킹 문제이다.
# _ 에 모음을 대입하고 조건을 만족하는 문자열만 카운팅 해야한다.
# 상근이가 좀 미친사람같다.

# 조건
# 1. 단어의 길이는 최대 100이다.
# 2. 모음(A,E,I,O,U)이 연속해서 3번 나오지 않아야 한다. 
# 3. 자음(모음을 제외한 나머지 알파벳)이 연속해서 3번 나오지 않아야 한다.
# 4. L을 반드시 포함해야 한다.

# 풀이
# 1. 먼저 모음과 자음을 전부 정의해 둔다.
# 2. 이후 _를 찾으면 백트래킹을 돌게하고, 백트래킹은 _에 "A" 또는 "B"를 삽입한다.
# 2-1. 이유는 A와 B는 각각 모음 자음이기 때문이다.
# 3. 그러면서 another_s 에 연산과정을 줄이기위해 A와 B를 통해 지금 대체한 문자가 모음인지 자음인지 기록해둔다.
# 4. 만약 백트래킹을 통해 _를 다 없애고 나면 verify 함수를 통해 연속된 문자열이 있는지 확인한다.
# 5. 조건을 만족한다면 another_s를 통해 자음과 모음을 각각 계산해주고 이를 리턴하면 정답처리를 받을 수 있다.


def verify(s):
    if 'L' not in s: return False # L이 없으면 false
    for i in range(len(s) - 2):
        if s[i] in mo and s[i + 1] in mo and s[i + 2] in mo: return False # 모음 3개 연속인 경우 false
        if s[i] in ja and s[i + 1] in ja and s[i + 2] in ja: return False # 자음 3개 연속인 경우 false
    return True

def backtrack(s,start,another_s):
    global cnt
    if '_' not in s:
        if verify(s):
            temp = 1
            for j in another_s:
                if j == 'A':
                    temp *= 5
                if j == 'B':
                    temp *= 20
                if j == 'L':
                    temp*=1
            cnt += temp
            return
    
    for i in range(start,len(s)):
        if s[i] == '_':
            s = s[:i] + 'A' + s[i+1:] 
            backtrack(s,start+1,another_s+'A')     
            s = s[:i] + 'B' + s[i+1:] 
            backtrack(s,start+1,another_s+'B')     
            s = s[:i] + 'L' + s[i+1:] 
            backtrack(s,start+1,another_s+'L')
            return      
s = input()
cnt = 0
mo = ['A','E','I','O','U']
ja = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
flag = False
for i in range(len(s)):
    if s[i] == '_': # S에서 처음으로 _ 발견하면 그때부터 재귀 시작
        flag = True
        backtrack(s, i, '')
        break
if not flag: 
    ans = 1 # S에서 _가 한개도 없는 경우

print(cnt)