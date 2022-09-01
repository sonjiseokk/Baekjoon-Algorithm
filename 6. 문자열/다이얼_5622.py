# 문제
# 처음에는 굉장히 난해한 문제라 바로 해결하지 못했었다.

# 접근방식으론
# 1. 알파벳들을 인덱스에 할당한다.
# 2. 입력이 들어오면 그걸 토대로 if문을 통해 찾는다
# 3. 해당되는 인덱스에 3을 더하여 그림대로 출력하도록 한다.

grandma_input = input()

num = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
count = 0
for i in range(len(grandma_input)):
    for j in num:
        if grandma_input[i] in j:
            count+=num.index(j)+3

print(count)